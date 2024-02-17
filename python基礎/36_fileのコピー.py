def copy(src, new_path):
    file1 = open(src, 'rb')
    file2 = open(new_path, 'wb')
    s = file1.read()
    file2.write(s)
    file2.close()
    file1.close()
    
if __name__ == '__main__':
    src="C:/Users/n1512/Desktop/Python/openCV_practice/4. 顔認識/face_data/9.sumi/1.jpg"
    new_path="./sumi.jpg"
    copy(src, new_path)
    print('file is copyed')