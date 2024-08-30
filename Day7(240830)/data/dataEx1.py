from datetime import datetime, timedelta
import requests
import os
import json
import pandas as pd

# 현재 파일이 있는 디렉토리 경로 가져오기
current_dir = os.path.dirname(os.path.abspath(__file__))

# 엑셀 파일의 상대 경로 설정
file_path = os.path.join(current_dir, "기상청41_단기예보 조회서비스.xlsx")

# 엑셀 파일 읽기
data = pd.read_excel(file_path)

# 데이터 출력
# print(data.head())

# 부여받은 서비스 키
serviceKey = "07gvxDaxlMsHsnqKIEKfBZvrvGeMZeW1aPh4H7f%2F5nFEufhp%2Beal5njV1knK67uvRlHrwdrbDge%2BG1ni00WMvQ%3D%3D"

base_date = '20240830'
base_time = '0800'
nx = '61'      # 예보 지점(x좌표)
ny = '128'     # 예보 지점(y좌표)

# 구하고 싶은 시간
input_d = datetime.strptime(base_date + base_time, "%Y%m%d%H%M")
print(f"구하고 싶은 시간 : {input_d}")

# 실제 입력 시간
input_d = datetime.strptime(base_date + base_time, "%Y%m%d%H%M") - timedelta(hours=1)
print(f"실제 입력 시간 : {input_d}")

input_datetime = datetime.strftime(input_d, "%Y%m%d%H%M")
input_date = input_datetime[:-4]
input_time = input_datetime[-4:]

# url
url = f'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcstserviceKey={serviceKey}&numOfRows=10&pageNo=1&base_date={base_date}&base_time={base_time}&nx=60&ny=127'

response = requests.get(url, verify=False)
if response.status_code != 200:
    print(f"Request failed: {response.status_code}")
    print(response.text)
res = json.loads(response.text)