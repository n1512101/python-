import os.path

print(os.path.abspath('./file'))
print(os.path.exists('file'))
print(os.path.exists('file12345'))
print(os.path.join('D:/python','b.txt'))
print(os.path.splitext('b.txt'))
print(os.path.basename(r'C:\Users\n1512\Desktop\Python\python基礎\file\aa.txt'))
print(os.path.dirname(r'C:\Users\n1512\Desktop\Python\python基礎\file\aa.txt'))
print(os.path.isdir(r'C:\Users\n1512\Desktop\Python\python基礎\file'))
print(os.path.isfile(r'C:\Users\n1512\Desktop\Python\python基礎\file\aabbbb.txt'))