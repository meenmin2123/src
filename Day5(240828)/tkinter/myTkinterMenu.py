from tkinter import *
from tkinter import messagebox,filedialog

def open_file(event=None):
    file = filedialog.askopenfilename()

    # askopenfilename(속성)
    # parent = 윈도우창 or 프레임
    # filetypes = (("모든 파일","*.*"),("텍스트파일),"*.txt")) 튜플 형태

    if file:
        messagebox.showinfo("파일열기",f"선택된 파일:{file}" )

def quit_app(event=None):
    root.quit()     # root.mainloop() 중지시킴

root = Tk()
root.geometry("400x400")     

# 메뉴바 생성
mainMenu = Menu(root)
root.config(menu=mainMenu)

# 상위메뉴
fileMenu = Menu(mainMenu,tearoff=False)
mainMenu.add_cascade(label="파일", menu=fileMenu)

# 하위메뉴
fileMenu.add_command(label="열기",accelerator="Ctrl+o")
fileMenu.add_separator()            # 가로 선
fileMenu.add_command(label="종료")

# 이벤트 
# 모든 컴포넌트 실행중에도 단축키를 사용할 수 있도록 ! 
# 단축키 이벤트!
root.bind_all("<Control-o>",open_file)
root.bind_all("<Control-q>",quit_app)

root.mainloop()