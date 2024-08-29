# 파일 내용 읽어오기
try:
    with open("test2.txt", "r") as file:
        content = file.read()
        # content = file.read(2)  read() - 전체 내용 / read(2) - 정해진 글자 수 만큼 읽어오기
        print(content)

except Exception as e:
    print(e)


#  csv 타입 가져와서 읽기
import chardet
import pandas
import csv

try:
    with open("singer1.csv", "rb") as file:
        content = file.read()
        print(content)

except Exception as e:
    print(e)
