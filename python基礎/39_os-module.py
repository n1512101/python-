import os

print(os.getcwd())
print(os.listdir())
print('-'*30)
print(os.listdir('./file'))
# os.mkdir('aa')
# os.makedirs('./a/b/c')
# os.rmdir('aa')
# os.removedirs('./a/b/c')
os.chdir('C:/Users/n1512/Desktop')
print(os.getcwd())

# for dirs,dirlst,filelst in os.walk('C:/Users/n1512/Desktop/Python'):
#     print(dirs)
#     print(dirlst)
#     print(filelst)
#     print('----------------------------')
    
# os.remove('./a.txt')
# os.rename('./aa.txt', 'newaa.txt')

import time
def date_format(longtime):
    s = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(longtime))
    return s

info = os.stat('C:/Users/n1512/Desktop/Python/python基礎/17_lambda.py')
print(type(info))
print(info)
print(date_format(info.st_atime))
print(date_format(info.st_ctime))

os.startfile('calc.exe')