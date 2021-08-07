from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480")  # 가로 * 세로

# 텍스트 위젯 만들기
txt = Text(root, width = 30, height = 5)
txt.pack()

txt.insert(END, "글자를 입력하세요")  # 텍스트 위젯에 글자 미리 넣어 두기

e = Entry(root, width = 30)
e.pack()
e.insert(0, "한 줄만 입력해요")  # 엔트리창의 값이 비어 있으므로 END 대신 0을 써도 된다

def btncmd() :
    #  내용 출력
    print(txt.get("1.0", END))  # 1은 첫번째 라인, 0은 0번째 column 위치
    print(e.get())

    #  내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)
btn = Button(root, text = "클릭", command = btncmd)
btn.pack()


root.mainloop()