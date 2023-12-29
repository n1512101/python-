from inspect import FrameInfo
import tkinter as tk
from tkinter import Entry, filedialog
from PIL import Image, ImageTk, ImageOps  # 画像データ用
import cv2
import os

# csvファイル用
import csv
import pprint


class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()

        # ウィンドウタイトル
        self.master.title("顔登録システム")

        # ウィンドウサイズ(幅x高さ)
        self.master.geometry("800x300")
        
        # Canvasの作成
        self.canvas = tk.Canvas(self.master)

        # Canvasを配置
        self.canvas.pack(expand = True, fill = tk.BOTH)

        # カメラをオープンする
        url = 'rtsp://admin:admin2@192.168.0.102:554/stream1'
        self.capture = cv2.VideoCapture(url)
        # self.capture = cv2.VideoCapture(0)

        # 動画を表示
        self.disp_image()



    # 画像をCanvasに表示する
    def disp_image(self):
        
        frame1 = tk.Frame(root)
        # フレーム画像の取得
        ret, frame1 = self.capture.read()

        # フレームの大きさ調整
        frame1 = cv2.resize(frame1, dsize=(600, 330))
    
        # BGR→RGB変換
        global cv_image
        cv_image = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)

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



# main関数
if __name__ == "__main__":
    root = tk.Tk()


    # frame.grid(row=0,column=0)

    # frame2 = tk.Frame(root)
    # frame2.grid(row=0,column=1)


    app = Application(master = root)
    app.mainloop()