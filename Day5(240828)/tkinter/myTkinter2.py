import tkinter as tk

win = tk.Tk()  # Tk()를 tk 모듈을 통해 호출

# 이 부분에 컴포넌트들을 배치
label1 = tk.Label(win, text="python1")
label2 = tk.Label(win, text="python2", font="")
label3 = tk.Label(win, text="python3")

# 배치 - 윈도우 창에 추가
label1.pack()
label2.pack()
label3.pack()

win.mainloop()