import tkinter as tk
import tkinter.ttk
import pymysql

# 1. mysql 연결하기 connect()
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="1107",
    database="pythonTest",
    charset="utf8",
    port=3306,
)
cur = conn.cursor()

root = tk.Tk()


def insert_user():
    user_id = idEntry.get()
    user_name = nameEntry.get()
    user_email = emailEntry.get()
    user_birth = birthEntry.get()

    query = "INSERT INTO `USERTABLE` (id, userName, email, brithYear) VALUES (%s, %s, %s, %s)"
    cur.execute(query, (user_id, user_name, user_email, user_birth))
    conn.commit()
    treeview.insert(
        "",
        "end",
        values=(idEntry.get(), nameEntry.get(), emailEntry.get(), birthEntry.get()),
    )
    print(f"{user_id}님의 정보가 추가되었습니다.")


def select_users():

    # 기존 데이터 삭제
    for item in treeview.get_children():
        treeview.delete(item)

    cur.execute("select * from userTable")
    rows = cur.fetchall()

    for row in rows:
        treeview.insert("", "end", values=row)


root.title("GUI 데이터 입력")
root.geometry("800x400")

idEntry = tk.Entry(root, justify=tk.CENTER)
idEntry.grid(row=0, column=0, padx=10, pady=5, sticky="ew")  # 첫 번째 행, 첫 번째 열

nameEntry = tk.Entry(root)
nameEntry.grid(row=0, column=1, padx=10, sticky="ew")  # 첫 번째 행, 두 번째 열

emailEntry = tk.Entry(root)
emailEntry.grid(row=0, column=2, padx=10, sticky="ew")  # 첫 번째 행, 세 번째 열

birthEntry = tk.Entry(root)
birthEntry.grid(row=0, column=3, padx=10, sticky="ew")  # 첫 번째 행, 네 번째 열

input_button = tk.Button(root, text="입력", command=insert_user)
select_button = tk.Button(root, text="조회", command=select_users)

input_button.grid(row=0, column=4, padx=5, pady=5)
select_button.grid(row=0, column=5, padx=5, pady=5)

# 표 생성하기. colums는 컬럼 이름
treeview = tk.ttk.Treeview(
    root, columns=["id", "userName", "email", "brithYear"], show="headings"
)

treeview.heading("id", text="ID")
treeview.column("id", width=100, anchor="center")

treeview.heading("userName", text="name", anchor="center")
treeview.column("userName", width=100, anchor="center")

treeview.heading("email", text="email", anchor="center")
treeview.column("email", width=100, anchor="center")

treeview.heading("brithYear", text="brithYear", anchor="center")
treeview.column("brithYear", width=100, anchor="center")

# Treeview 위젯을 화면에 배치
# 세 번째 행, 모든 열에 걸쳐 채우기
treeview.grid(row=2, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")

# 행의 크기 조정
root.grid_rowconfigure(2, weight=1)  # Treeview가 있는 행 확장 가능하도록 설정

for i in range(5):
    root.grid_rowconfigure(i, weight=1)  # 행 확장

select_users()

root.mainloop()
