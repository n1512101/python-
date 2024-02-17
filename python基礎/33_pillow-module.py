from PIL import Image

im = Image.open('C:/Users/n1512/Desktop/Python/openCV_practice/4. 顔認識/face_data/9.sumi/1.jpg')
# print(type(im), im)

r,g,b=im.split()
# print(r)
# print(g)
# print(b)

om = Image.merge(mode='RGB', bands=(r,b,g))
om.save('sumi.jpg')
