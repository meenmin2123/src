# 자동이용해서 데이터를 크롤링하거나
# 로그인

# 1. 크롬드라이버를 설치하기 - 회의록에 사이트
# 2. 본인 크롬 버전 - 크롬 확인 (도울말)
# 3. 크롬드라이버 exe 실행 파일을 현재 - 파일과 같은 위치에 저장하기

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 1. py파일로 드라이버 가져오기
# Chrome('경로/파일명.exe')
# - 같은 경로에 크롬 드라이버가 있으면 () 안에 작성 안해도 됨.
driver = webdriver.Chrome()
# driver.get('https://www.google.co.kr/?hl=ko')
driver.get("https://www.instagram.com/")  # 인스타 주소

# 위에 html 문서를 다 가져올 수 있도록 조금 기다림
time.sleep(5)

eleName = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
eleName.send_keys("minmeen2123")

elePw = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
elePw.send_keys("1234567890")
elePw.send_keys(Keys.ENTER)

print(eleName)
print(elePw)

time.sleep(10)  # 10초 동안은 꺼지지 않게 시간 설정
