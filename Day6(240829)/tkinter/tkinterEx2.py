from tkinter import *

# ListBox

root = Tk()

root.title("?ListBox?")
root.geometry("800x500")

list1 = Listbox(root, bg="#98afe4", width=50, height=20)

# listbox 추가할 때는 insert()
for i in range(10): # 0 ~ 9
    list1.insert(END,i)
    
# 문자열 추가하기
strList = ['python','Tkinter','listbox']
for str in strList:
    list1.insert(END,str)

# 리스트나 튜플과 같은 반복 가능한 객체의 모든 값들을 

list1.pack()

root.mainloop()

# 1. listbox 이용해서 데이터 저장
# 2. treeview 컴포넌트 사용 - tkinter 모듈 안에 ttk 라이브러리로 포함
