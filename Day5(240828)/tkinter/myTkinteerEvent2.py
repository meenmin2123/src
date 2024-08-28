from tkinter import *
from tkinter import messagebox,filedialog

def open_file(event=None):
    file = filedialog.askopenfilename()

    if file:
        messagebox.showinfo("파일열기",f"선택된 파일:{file}")