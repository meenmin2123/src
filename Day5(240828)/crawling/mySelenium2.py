from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 


driver = webdriver.Chrome()
driver.get('https://ncov.kdca.go.kr/pot/index.do')

time.sleep(5)

data = driver.find_element(By.XPATH,\
                          '//*[@id="swiper-wrapper-6d11b1d4cfee10a82"]/div[1]')
print(f"데이터: {data}")
time.sleep(20)