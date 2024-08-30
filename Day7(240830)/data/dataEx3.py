import pandas as pd
import os

# 현재 파일이 있는 디렉토리 경로 가져오기
current_dir = os.path.dirname(os.path.abspath(__file__))

# 엑셀 파일의 상대 경로 설정
file_path = os.path.join(current_dir, "기상청41_단기예보 조회서비스.xlsx")

df = pd.read_excel(file_path)

# 특정 nx, ny 좌표로 지역 검색
nx, ny = 60, 127
placeCode = 1129052500
region_info = df[(df['행정구역코드'] == placeCode) & (df['격자 X'] == nx) & (df['격자 Y'] == ny)]

# 지역명 출력
if not region_info.empty:
    print(region_info['행정구역코드'].values[0])
    print(region_info['1단계'].values[0])
    print(region_info['2단계'].values[0])
    print(region_info['3단계'].values[0])
else:
    print("해당 좌표에 대한 지역 정보를 찾을 수 없습니다.")