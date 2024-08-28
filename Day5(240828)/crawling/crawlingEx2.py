import requests
from bs4 import BeautifulSoup
import time

class Naver:
    def __init__(self,title='', link1='',content=''):
        self.title = title
        self.link1 = link1
        self.content = content

class NaverBlogMa:
    def __init__(self):
        self.blogList = []

    # 추가
    def add_blog(self, link):
        self.blogList.append(link)
        for li in link:
            res = li.get_text()
            self.blogList.append(res)
        print(f"블로그 링크 추가: {link}")
    
    # 삭제

    # 조회
    def select(self):
        if not self.blogList:
            print("저장된 블로그 링크가 없습니다.")
        else :
            print("전체 링크 출력")
            for blog in self.blogList:
                print(blog)
    # 수정


# get 요청
# 입력하는 검색창 get 요청을 하는 창
naver = NaverBlogMa()

resp = requests.get("https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=%EC%95%A0%ED%94%8C")

soup = BeautifulSoup(resp.text, 'html.parser')
findLink = soup.find_all('a',class_='title_link')[0].text


# print(naver.add_blog(findLink))
# naver.select()
# findLink = soup.select("li.bx")
print(findLink)

# if len(findLink) != 0:
#     for li in findLink:
#         print(li.get_text(string=True))
#         time.sleep(2)

title = soup.select('a.title_link')[0].text
print(f"select() : {title}")

img = soup.select('img')[2]['src']
print(f"select() img : {img}")

# naver.add_blog(findLink)
# print(naver.blogList)
for li in naver.blogList:
        print(li)

# 첫번째 이미지불러오기
imageUrl = soup.find_all('img')[1]
print(imageUrl)


#--------------------------------------
# 찾기 
# bxList = soup.find_all('li',class_='bx')
#print(bxList)

# 첫번째 링크 텍스트 가져오기 
# title = soup.find_all('a',\
#         class_='title_link')[0].text 
# print(title)

# # 첫번째 이미지 URL 가져오기 
# imageUrl = soup.find_all('img')[2]['src']
# print(imageUrl)


# select()
#  css 선택자를 이용해서 다양하게 데이터를
#  찾아올 수있다.  클래스 ., id #,  a ,
#  태그명[속성]

# bxList = soup.select("li.bx")

# #print(bxList)
# for li in bxList:
#     # 양쪽 공백을 제거할 수있도록 속성값
#     # strip=True
#     print(li)
#     print(li.get_text(strip=True))

#     #time.sleep(2)

# title = soup.select('a.title_link')[0].text
# print(f"select() : {title}")

# img = soup.select('img')[2]['src']
# print(f"select() img : {img}")

naverList = []

title = soup.select('a.title_link')[0].text
link1 = soup.select('a.title_link')[0]['href']
img = soup.select('img')[2]['src']

# naver객체 생성
obj = Naver(title=title,\
            link1=link1,\
            content=img)

# 리스트에 저장 
naverList.append(obj)

print(naverList[0])
