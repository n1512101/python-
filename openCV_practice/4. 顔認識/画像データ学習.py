import os
import cv2
from PIL import Image
import numpy as np

def getImageAndLabels(path):
    facesSamples = []
    ids = []

    face_detector = cv2.CascadeClassifier("C:/Users/n1512/anaconda3/Lib/site-packages/opencv-4.8.0/data/haarcascades/haarcascade_frontalface_alt.xml")


    id_name_files = [os.path.join(path, f) for f in os.listdir(path)]
    for id_name_file in id_name_files:
        imagePaths = [os.path.join(id_name_file, h) for h in os.listdir(id_name_file)]

        for imagePath in imagePaths:
#             print(os.path.basename(os.path.dirname(imagePath)).split('.')[1])
# getImageAndLabels("./face_data/")

            # ファイル名からユーザーIDを抽出
            id = int(os.path.basename(os.path.dirname(imagePath)).split('.')[0])



            PIL_img = Image.open(imagePath).convert("L")
            img_numpy = np.array(PIL_img, 'uint8')
            faces = face_detector.detectMultiScale(img_numpy)

            for x, y, w, h in faces:
                ids.append(id)
                facesSamples.append(img_numpy[y:y+h, x:x+w])

        print('id:', id)
        print('fs:', facesSamples)
    return facesSamples, ids







#     for imagePath in imagePaths:
#         # ファイル名からユーザーIDを抽出
#         id = int(os.path.basename(imagePath).split('.')[0])
#         PIL_img = Image.open(imagePath).convert("L")
#         img_numpy = np.array(PIL_img, 'uint8')
#         faces = face_detector.detectMultiScale(img_numpy)

#         for x, y, w, h in faces:
#             ids.append(id)
#             facesSamples.append(img_numpy[y:y+h, x:x+w])

#     print('id:', id)
#     print('fs:', facesSamples)
#     return facesSamples, ids

if __name__ == '__main__':
    path = './face_data/'
    faces, ids = getImageAndLabels(path)

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, np.array(ids))

    recognizer.write('trainer/trainer.yml')
