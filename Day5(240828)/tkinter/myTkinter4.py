from tkinter import *

def msg():
    # 엔트리에서 값을 꺼내기
    print(entry.get())

root = Tk()
root.geometry("500x200")        # 창 크기 

# input > entry 
# 사용자로 부터 입력을 받는 컴포넌트
entry = Entry(root, width=30)
entry.pack(pady=5)

btn = Button(root, text="확인", command=msg)
btn.pack()

root.mainloop()