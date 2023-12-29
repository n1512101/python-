from inspect import FrameInfo
from pickle import FRAME
# from msilib.schema import SelfReg
import tkinter as tk
from tkinter import Entry, Frame, filedialog
from typing import Self
from PIL import Image, ImageTk, ImageOps  # 画像データ用
import cv2
import os

# csvファイル用
import csv
import pprint





class Frame0(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()

        # ウィンドウタイトル
        self.master.title("顔登録システム")

        # ウィンドウサイズ(幅x高さ)
        self.master.geometry("600x300")
        
        # Canvasの作成
        self.canvas = tk.Canvas(self, width=300, height=300)

        # Canvasを配置
        self.canvas.pack()

        # カメラをオープンする
        url = 'rtsp://admin:admin2@192.168.0.102:554/stream1'
        self.capture = cv2.VideoCapture(url)
        # self.capture = cv2.VideoCapture(0)

        # 動画を表示
        self.disp_image()

        # ユーザ画面(画面1)を表示
        # self.disp_user(1)

    # 画像をCanvasに表示する
    def disp_image(self):
        

        # フレーム画像の取得
        ret, frame = self.capture.read()

        # フレームの大きさ調整
        frame = cv2.resize(frame, dsize=(600, 330))

        # BGR→RGB変換
        global cv_image
        cv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # NumPyのndarrayからPillowのImageへ変換
        pil_image = Image.fromarray(cv_image)

        # PIL.ImageからPhotoImageへ変換する
        self.photo_image = ImageTk.PhotoImage(image=pil_image)

        # 画像の描画
        self.canvas.delete("all")

        # 画像を表示
        self.canvas.create_image(30,100,image=self.photo_image)

        # disp_image()を10msec後に実行する
        
        self.disp_id = self.after(10, self.disp_image)




class Frame1(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        # ラベル1('IDi:')
        # global lbl1
        lbl1 = tk.Label(self, text='IDi:')
        lbl1.grid(row=0, column=0,padx=30)
        

        # # IDiテキストボックス
        global txt1
        txt1 = tk.Entry(self, width=20)
        txt1.grid(row=0, column=1, pady=5)


        # ラジオボタン
        global group
        group = tk.IntVar()   #グループ用変数
        # global radio1, radio2
        radio1 = tk.Radiobutton(self, value=0, variable=group, text='新規ユーザー')
        radio1.grid(row=1, column=1, pady=10)
        radio2 = tk.Radiobutton(self, value=1, variable=group,text='更新')
        radio2.grid(row=2, column=1)

        # # '撮影'ボタン('撮影'ボタンを押すと画面2に移る)
        # # global button1
        # button1 = tk.Button(self, text='撮影', command=lambda:self.disp_user(2))
        button1 = tk.Button(self, text='撮影',width=5,command=change_frame2)
        button1.grid(row=3,column=1,pady=15)


class Frame2(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)


        # 映像を停止させる
        # self.after_cancel(self.disp_id)
        # self.after_cancel(Frame0.disp_id)

        # # 画面1のIDiテキストに入力された文字列をuser_IDi変数に読み取り
        # global user_IDi
        # user_IDi = txt1.get()

        # # 画面1の選択されたラジオボタンを取得
        # global new_or_update
        # new_or_update = group.get()

        # ラベル('この画像を登録しますか？')
        # global lbl2
        lbl2 = tk.Label(self, text='この画像を登録しますか？')
        lbl2.grid(row=0,column=0)





# フレームframe1に切り替わる関数
def change_frame1():
    frame1.tkraise()

# フレームframe2に切り替わる関数
def change_frame2():
    frame2.tkraise()

''' 
    # ユーザ画面を表示
    def disp_user(self, num):

        

        # 画面2
        elif num == 2:

            # 映像を停止させる
            self.after_cancel(self.disp_id)

            # 画面1のIDiテキストに入力された文字列をuser_IDi変数に読み取り
            global user_IDi
            user_IDi = txt1.get()

            # 画面1の選択されたラジオボタンを取得
            global new_or_update
            new_or_update = group.get()

            # 画面1のテキスト部分を消去
            lbl1.destroy()
            txt1.destroy()
            radio1.destroy()
            radio2.destroy()
            button1.destroy()

            # ラベル('この画像を登録しますか？')
            global lbl2
            lbl2 = tk.Label(text='この画像を登録しますか？')
            lbl2.place(x=400, y=50)

            # 'はい'、'いいえ'ボタン
            global button2, button3

            # 'はい'ボタン(ボタン押すとphoto_record()を実行する)
            button2 = tk.Button(self.master, text='はい', command=self.photo_record)
            button2.place(x=400, y=150)
            
            # 'いいえ'ボタン(ボタンを押すと画面3に移る)
            button3 = tk.Button(self.master, text='いいえ', command=lambda:self.disp_user(3))
            button3.place(x=490, y=150)

        # 画面3
        elif num == 3:

            # disp_image()を10msec後に実行する
            self.disp_id = self.after(10, self.disp_image)
            
            # 画面2のテキストを消去
            lbl2.destroy()
            button2.destroy()
            button3.destroy()


            # ラベル1(IDi)
            lbl1 = tk.Label(text='IDi:')
            lbl1.place(x=400, y=50)

            # IDiテキストボックス
            txt1 = tk.Entry(width=20)
            txt1.place(x=430, y=50)

            # ラジオボタン
            group = tk.IntVar()   #グループ用変数
            radio1 = tk.Radiobutton(self.master, value=0, variable=group, text='新規ユーザー')
            radio1.place(x=400, y=90)
            radio2 = tk.Radiobutton(self.master, value=1, variable=group,text='更新')
            radio2.place(x=400, y=120)

            # 撮影ボタン
            button1 = tk.Button(self.master, text='撮影', command=lambda:self.disp_user(2))
            button1.place(x=470, y=150)

        
        # # 画面4
        # elif num == 4:

        #     # 画面2のテキストを消去
        #     lbl2.destroy()
        #     button2.destroy()
        #     button3.destroy()

        #     # ラベル('IDi番号が登録済みです。')
        #     lbl2 = tk.Label(text='IDi番号が登録済みです。')
        #     lbl2.place(x=400, y=20)
        







    # ユーザの画像を登録する関数
    def photo_record(self):

        # '新規ユーザー'の場合
        if new_or_update == 0:

            # user_information.csvがすでに存在している場合(ファイル内にすでにuserデータが入っている場合)
            if os.path.isfile('user_information.csv') == True:




                
                # # 新規ユーザーなのにcsvファイル内に既に同じIDiが登録されている場合
                # # user_information.csvファイル内の行数を調べる
                # with open('user_information.csv', 'r') as file:
                #     csv_reader = csv.reader(file)
                #     # row_countはcsvファイルの行数
                #     row_count = sum(1 for row in csv_reader)   
                # file.close()

                # # 入力されたIDiと同じファイル内のIDiを検索
                # with open('user_information.csv', 'r') as file:
                #     lines = file.readlines()

                #     for i in range(1,row_count):
                #         target_line = lines[i]
                #         # info_in_fileはcsvファイル内の各行のデータ
                #         info_in_file = target_line.split(',')
                        
                #         # csvファイル内のIDiが画面入力されたIDiと一致した場合
                #         if info_in_file[0] == user_IDi:





                            



                #             self.disp_user(4)
                            
                            


                #             # 画面3に戻る
                #             # self.disp_user(3)
                #             file.close()
                #             return
                # file.close()
                







            # 新規ユーザーでcsvファイル内に同じIDiが登録されていない場合のみ下記実行
                # user_information.csvファイルの最後の行を変数last_lineに読み込む
                with open("user_information.csv", "r") as fr:
                    last_line = fr.readlines()[-1]
                fr.close()

                # last_line内が「IDi, User_ID」形式の文字列になっている為、','で区切る  last_User_IDが最後のUser_IDとなる
                user_info_list = last_line.split(',')
                last_User_ID = (int)(user_info_list[-1])

                # csvファイルにIDiとUser IDを書き込む
                with open('user_information.csv', 'a', newline='') as fw:
                    writer = csv.writer(fw)
                    writer.writerow([user_IDi, last_User_ID + 1])
                fw.close()
                
                # 写真をフォルダ内に保存
                # facesフォルダ内にuser IDに対応したフォルダを作成
                os.mkdir(f'faces/{str(last_User_ID + 1)}')
                # 静止画をuser IDフォルダに保存
                cv2.imwrite(f'faces/{str(last_User_ID + 1)}/1.jpg', cv_image)

            # user_information.csvがまだ存在しない場合(ファイルに初めてuser情報を書き込む場合)
            else:

                # ファイルを作成
                f = open('user_information.csv', 'w')

                # ファイルの先頭を記入
                f.write('IDi,User_ID\n')

                # 画面に入力されたIDiを書き込み、User_IDを1とする
                f.write(user_IDi + ',1\n')
                f.close()

                # 写真をフォルダ内に保存
                # facesフォルダ内にuser IDに対応したフォルダを作成
                os.mkdir('faces/1')
                # 静止画をuser IDフォルダに保存
                cv2.imwrite('faces/1/1.jpg', cv_image)


        # '更新'の場合
        else:

            # user_information.csvファイル内の行数を調べる
            with open('user_information.csv', 'r') as file:
                csv_reader = csv.reader(file)
                # row_countはcsvファイルの行数
                row_count = sum(1 for row in csv_reader)   
            file.close()

            # 入力されたIDiと同じファイル内のIDiを検索
            with open('user_information.csv', 'r') as file:
                lines = file.readlines()

                for i in range(1,row_count):
                    target_line = lines[i]
                    # info_in_fileはcsvファイル内の各行のデータ
                    info_in_file = target_line.split(',')
                    
                    # csvファイル内のIDiが画面入力されたIDiと一致した場合
                    if info_in_file[0] == user_IDi:
                        global User_ID_in_file
                        # User_ID_in_fileにIDiが一致したuser_idを代入
                        User_ID_in_file = info_in_file[-1]
                        break
            file.close()
                
            # フォルダ内の最後の写真の名前を調べる
            dir = f'faces/{User_ID_in_file.strip()}'
            # 所定ユーザーフォルダ内の最後の写真のint値に1を足す
            photo_name = int(max(os.listdir(dir)).strip(".jpg")) + 1
            
            # 静止画をIDiに対応したuser IDフォルダに保存
            cv2.imwrite(f'faces/{User_ID_in_file.strip()}/{photo_name}.jpg', cv_image)            

        # 画面3に移る
        self.disp_user(3)
'''


# # main関数
if __name__ == "__main__":
    app = tk.Tk()
    frame0 = Frame0(app)
    frame1 = Frame1(app)

    # frame2 = Frame2(app)

    frame0.grid(column=0,row=0)
    frame1.grid(column=1,row=0)

    

    frame2 = Frame2(app)

    frame2.grid(column=1,row=0)

    frame1.tkraise()
    app.mainloop()
