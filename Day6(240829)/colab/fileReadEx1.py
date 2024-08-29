# 파일 가져오기
try:
    file = open(
        "test1.txt", "w"
    )  # 파일이 없으면 생성 / 파일이 있으면 생성x 그냥 불러오기
    file.close()

except Exception as e:
    print(e)

try:
    with open("test2.txt", "w") as file:
        file.write("문자타입으로 저장이 된대요~")
        # file.write(1)

except Exception as e:
    print(e)
