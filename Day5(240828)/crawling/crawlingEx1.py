# 다운 받은 뒤, import 써서 terminal에 오류 안 뜨는지 확인.
import requests

# import bs4
# BeautifulSoup : 크롤링을 하기 쉽게 도와주는 라이브러리.
# - 웹 페이지의 데이터를 추출하기 위해 html이나 xml문서를 파싱하여 구조화된 데이터를 만들 수 있음.
from bs4 import BeautifulSoup
import selenium
import time  # 시간과 관련된 라이브러리

# 내가 원하는 웹 사이트 접속
html = requests.get("https://www.google.co.kr/")

time.sleep(5)  # 5초 뒤에 다시 데이터 가져옴  ex)로그인, 검색
soup = BeautifulSoup(html.text, "html.parser")

# print(soup)
# 데이터를 검색할 수 있는 메서드
# find(), find_all(), select()

title = soup.title.string
print(f"타이틀: {title}")

# 첫번째 링크 가져오기
link1 = soup.find("a")
print(f"첫번째 링크: {link1.get('href')}")
print(type(link1))

print("*" * 30)

link2 = soup.find_all("a")
listA = []

print(type(link2))
for link in link2:
    res = [link.get("href")]
    listA.append(res)
print(f"전체 링크 출력: {listA}")

print("*" * 30)

all_link = soup.find_all("a")

# 예외처리
if len(all_link) != 0:
    for index, link2 in enumerate(all_link, start=1):
        print(f"{index}.{link2.get('href')}")


# 요청을 하면 html에 응답이 옴.
# 데이터의 원본(바이트)을 그대로 가져옴.
# 이진파일 데이터를 다룰 때 유용함.
# 텍스트 말고 이미지, 파일
# html.text.replace("_ or / or \" ",'')
# 모든 내용은 텍스트로 문자열 반환됨.
# print(html.content)

# html.text : html이나 json 등의 텍스트 데이터를 분석하거나 출력하기 위해서 사용함.
# 문자열, content도 슬라이싱을 할 수 있음.
# print(html.text[:100])
