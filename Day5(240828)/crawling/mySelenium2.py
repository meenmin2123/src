from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 웹 사이트 고정 창
options = webdriver.ChromeOptions()
options.add_argument("window-size=1600,1000")  # 너비와 높이를 고정으로 설정

driver = webdriver.Chrome(options=options)
driver.get("https://ncov.kdca.go.kr/pot/index.do")

time.sleep(5)

# data = driver.find_element(By.XPATH, '//*[@id="swiper-wrapper-6d11b1d4cfee10a82"]/div[1]')
# data = driver.find_element(By.CSS_SELECTOR, 'div.con')
# print(f"데이터: {data.text}")

# list1 = driver.find_elements(By.CSS_SELECTOR, 'a.notice_box')

# for div in list1:
#     print(f"* 텍스트:  {div.text}")
#     print(f"* 링크 : {div.get_attribute('href')}")

img1 = driver.find_elements(By.CSS_SELECTOR, "div.item img")

for img in img1:
    img_src = img.get_attribute("src")
    print(f"* 이미지 url : {img_src}")

time.sleep(20)

# 반응형 때문에 경로 이슈 발생.
# css를 이용해서 데이터 가져오기
# 해결 : 창 크기를 고정
