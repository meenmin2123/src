from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x400")  # 창 크기


# 마우스 클릭했을 때 이벤트 생성하기
def mouseClickEvent(event):
    # 마우스 클릭 시 작동할 내용
    # 윈도우 창에 이벤트 설정
    # bind("마우스 클릭 종류", 이벤트처리함수)
    pass


def clickLeft(event):
    messagebox.showinfo("마우스", "왼쪽 클릭!")


def clickCenter(event):
    messagebox.showinfo("마우스", "왼쪽 클릭!")


def clickRight(event):
    messagebox.showinfo("마우스", "왼쪽 클릭!")


def click(event):
    btnMap = {1: "왼쪽", 2: "가운데", 3: "오른쪽"}

    temp = btnMap.get(event.num)

    # 마우스 이벤트 객체에
    # 마우스 위치를 설정
    msg = f"{temp} 버튼클릭! 위치:({event.x},{event.y})"

    btnMap.get(event.num)
    messagebox.showinfo("마우스", msg)


# 이벤트 설정
root.bind("<Button-1>", clickLeft)
root.bind("<Button-2>", clickCenter)
root.bind("<Button-3>", clickRight)

root.mainloop()
