from tkinter import *
from tkinter.messagebox import showinfo
# import tkinter.messagebox   # 팝업창


# 함수를 정의할 때 클래스 안에 선언. 매개변수가 없어도 됨.
def myFunc():
    showinfo('버튼 클릭','클릭 완료')

def myFunc2():
    if check.get() == 0:
        showinfo("","체크버튼 off")
    else :
        showinfo("","체크버튼 on")
def myFunc3():
    value = myVar.get()

    if value == '사과':
        result.configure(text="사과")
    elif value == '복숭아':
        result.configure(text='복숭아')
    elif value == '딸기':
        result.configure(text="딸기")
    elif value == '파인애플':
        result.configure(text='파인애플')

win = Tk()

# 메인
win.geometry('500x200')

# 버튼
btn1 = Button(win, text="클릭!", command=myFunc)

# 체크박스
# StringVar()
# BooleanVar()
check = IntVar()    # 클릭하면 숫자를 반환받음
cb1 = Checkbutton(win, text="클릭!", variable=check, command=myFunc2)

# 라디오 버튼
# - 예외적인 상황 발생
# - 1. 처음 시작했을 때 전체 시작. StringVar() 괄호 안에 어떤 설정
# - 2. deselect()

myVar = IntVar()
rb1 = Radiobutton(win, text="사과", variable=myVar, value="사과", command=myFunc3)
rb2 = Radiobutton(win, text="복숭아", variable=myVar, value="복숭아", command=myFunc3)
rb3 = Radiobutton(win, text="딸기", variable=myVar, value="딸기", command=myFunc3)
rb4 = Radiobutton(win, text="파인애플", variable=myVar, value="파인애플", command=myFunc3)

result = Label(win, text="선택한 과일")

# 추가
# side=LEFT, RIGHT, TOP, BOTTOM
btn1.pack()
cb1.pack()
rb1.pack(side=LEFT)
rb2.pack(side=LEFT)
rb3.pack(side=LEFT)
rb4.pack(side=LEFT)
result.pack()

win.mainloop()