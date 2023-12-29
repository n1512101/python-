import os

# listdir()  フォルダ内のすべてのファイルを表示する
print(os.listdir(r"C:\Users\n1512\Desktop\Python"))

# curdir  現在のカレントディクトリー  相対パス
print(os.curdir)

# getcwd()  現在のカレントディクトリー　　絶対パス
print(os.getcwd())

# mkdir()   フォルダを作る
# makedirs()   フォルダの中にフォルダを作れる
# rmdir()   空のフォルダを削除する
# rename()   ファイルの名前変更
# remove()   ファイルの削除

# os.path.join()   パスを接続
print(os.path.join(r"C:\Users\n1512\Desktop\Python", "note.md"))

# os.path.split()   パスを分割
print(os.path.split(r"C:\Users\n1512\Desktop\Python\note.md"))

# os.path.getsize()   ファイルのサイズ
print(os.path.getsize(r"C:\Users\n1512\Desktop\Python\passの使い方.py"))

# os.path.exists()    ファイルが存在するか
print(os.path.exists(r"C:\Users\n1512\Desktop\Python\passの使い方.py"))

# os.path.isfile()   ファイルなのかどうか
print(os.path.isfile(r"C:\Users\n1512\Desktop\Python\passの使い方.py"))

# os.path.isdir()   フォルダなのかどうか
print(os.path.isdir(r"C:\Users\n1512\Desktop\Python\passの使い方.py"))