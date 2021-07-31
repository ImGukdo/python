from tkinter import *

root = Tk()
root.title("GUI")

btn1 = Button(root, text = "버튼1")
btn1.pack()

# 글자에서 x축 방향과 y축 방향으로 간견을 넓힌다. 자간을 넓힌다
btn2 = Button(root, padx = 5, pady = 10, text = "버튼2")
btn2.pack()

btn3 = Button(root, padx = 10, pady = 5, text = "버튼3")
btn3.pack()

#  버튼 박스의 크기를 지정함
btn4 = Button(root, width = 10, height = 3, text = "버튼4")
btn4.pack()

#  글자 색상과 배경 색상을 지정
btn5 = Button(root, fg = "red", bg = "yellow", text = "버튼5")
btn5.pack()

#  이미지로 버튼 만들기
photo = PhotoImage(file = "gui_basic/image.png")
btn6 = Button(root, image = photo)
btn6.pack()

# 버튼을 눌렀을때 동작 만들기
def btncmd() :
    print("버튼이 클릭되었어요")

btn7 = Button(root, text = "동작하는 버튼", command = btncmd)
btn7.pack()

# 버튼의 위치를 지정
btn8 = Button(root, text='위치지정버튼', width=10)
btn8.place(x=100, y=250)

root.mainloop()