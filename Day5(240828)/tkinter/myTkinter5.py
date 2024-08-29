from tkinter import *


def msg():
    # 엔트리에서 값을 꺼내기
    idNow = entry.get()
    pwNow = entry2.get()

    if idNow == "love" and pwNow == "1107":
        print("로그인 성공")
    else:
        print("로그인 실패")


root = Tk()
root.geometry("500x200")  # 창 크기

label = Label(root, text="아이디")
label.pack()
entry = Entry(root, width=30)
entry.pack(pady=5)

label2 = Label(root, text="비밀번호")
label2.pack()
entry2 = Entry(root, width=30)
entry2.pack(pady=5)

btn = Button(root, text="확인", command=msg)
btn.pack()

root.mainloop()
