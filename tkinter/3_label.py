from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480")

label1 = Label(root, text = "안녕하세요")
label1.pack()

photo = PhotoImage(file = "image.png")
label2 = Label(root, image = photo)
label2.pack()


def change() :
    label1.config(text = "또 만나요")

    global photo2  # 함수가 끝나면 photo2 변수가 사라져서 적용이 안됨
    photo2 = PhotoImage(file = "image2.png")
    label2.config(image = photo2)

btn = Button(root, text = "클릭", command = change)
btn.pack()

root.mainloop()