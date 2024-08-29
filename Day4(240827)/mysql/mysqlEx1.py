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

# cur.execute('''
# create table if not exists userTable(
#     id        varchar(4),
#     userName  varchar(15),
#     email     varchar(50),
#     brithYear int
# )
# ''')

cur.execute(
    """
select * from userTable
"""
)

# fetchall() : sql에서 조회된 모든 내용을 가져오는 메서드

print("아이디 |  이름 |  이메일 |  생년월일")
print("-" * 40)
for row in cur.fetchall():
    # print(row)  # 튜플 자료형으로 출력됨.
    print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

# cur.execute("INSERT INTO userTable VALUES('iu', '아이유', 'iu@kpop.com', 1993)")
# cur.execute("INSERT INTO userTable VALUES('bts', '방탄소년단', 'bts@bighit.com', 2013)")
# cur.execute("INSERT INTO userTable VALUES('psy', '싸이', 'psy@yg.com', 1977)")
# cur.execute("INSERT INTO userTable VALUES('boa', '보아', 'boa@sm.com', 1986)")

# 5. 위에 실행문을 실행하고 나서
#   commit() 저장
conn.commit()


# 6. 닫기 close()
conn.close()
