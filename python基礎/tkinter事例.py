import tkinter as tk

root = tk.Tk()
root.title("face")
root.geometry("300x100")

frame1 = tk.Frame(root)
frame1.grid(row=0, column=0)

label1 = tk.Label(frame1, text="this is a pen")
entry1 = tk.Entry(frame1)
button1 = tk.Button(frame1, text="yes")

label1.pack()
entry1.pack()
button1.pack()


frame2 = tk.Frame(root)
frame2.grid(row=0, column=1)


label2 = tk.Label(frame2, text="hello world")
label2.pack()
button2 = tk.Button(frame2, text="frame3に移る",command=lambda:sub_window())
button2.pack()

def sub_window():
    sub_window = tk.Toplevel()
    sub_window.geometry("200x100")
    label_sub = tk.Label(sub_window, text="間違い")
    label_sub.pack()
    button_sub = tk.Button(sub_window, text="確認", command=sub_window.destroy)
    button_sub.pack()

root.mainloop()