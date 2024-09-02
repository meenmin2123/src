from bs4 import BeautifulSoup
import requests
import pandas as pd 

code = '005930'
url = f'https://finance.naver.com/item/main.naver?code={code}'
req = requests.get(url, headers={'User-agent':'Mozilla/5.0'})
headers = {'User-agent':'Mozilla/5.0'}
html = BeautifulSoup(req.text, "lxml")
df = pd.DataFrame()

parr = html.find('td', class_='pgRR')
print(parr.a['href'])

# parr가 None이 아닌지 확인
if parr and parr.a:
    href = parr.a['href']
    print(href)

    s = href.split('=')
    print(s)

    last_page = s[-1]
    print(last_page)

    # 모든 페이지에서 데이터를 가져옴
    for page in range(1, int(last_page) + 1):
        page_url = f"{url}&page={page}"
        try:
            req = requests.get(page_url, headers=headers)
            # 필요한 표가 첫 번째 표라고 가정
            df = pd.concat([df, pd.read_html(req.text, encoding="euc-kr")[0]], ignore_index=True)
        except Exception as e:
            print(f"페이지 {page}의 데이터를 가져오지 못했습니다. 오류: {e}")
else:
    print("페이지 내비게이션 요소를 찾을 수 없습니다.")   
    
# 데이터가 없는 행 일괄 삭제
df.dropna(inplace = True)

# 인덱스 재배열
df.reset_index(drop=True, inplace=True)

# xlsx 형식으로 저장
df.to_excel("samsung_price.xlsx", index=False)