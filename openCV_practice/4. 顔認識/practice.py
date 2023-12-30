import cv2 as cv

img = cv.imread("face_data/4.jpg")
cv.imshow("img", img)

print(img.shape)

cv.waitKey(0)

cv.destroyAllWindows()