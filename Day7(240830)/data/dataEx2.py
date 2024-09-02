import os
from datetime import datetime, timedelta
import requests
import os
import json
import pandas as pd
from urllib.request import urlopen

def placeCode_select(nx, ny):

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
        code = region_info['행정구역코드'].values[0]
        place1 = region_info['1단계'].values[0]
        place2 = region_info['2단계'].values[0]
        place3 = region_info['3단계'].values[0]
        list = [code, place1, place2, place3]
        
        # print(region_info['행정구역코드'].values[0])
        # print(region_info['1단계'].values[0])
        # print(region_info['2단계'].values[0])
        # print(region_info['3단계'].values[0])
        # print(f"list : {list}")
        
        return list
    else:
        print("해당 좌표에 대한 지역 정보를 찾을 수 없습니다.")
    
    
# 부여받은 서비스 키
serviceKey = "07gvxDaxlMsHsnqKIEKfBZvrvGeMZeW1aPh4H7f%2F5nFEufhp%2Beal5njV1knK67uvRlHrwdrbDge%2BG1ni00WMvQ%3D%3D"
# base_date = '20240830'
# base_time = '1500'
nx = '60'      # 예보 지점(x좌표)
ny = '127'     # 예보 지점(y좌표)
# input_d = datetime.strptime(base_date + base_time, "%Y%m%d%H%M") - timedelta(hours=1)
# print(f"실제 입력 시간 : {input_d}")

print("*" * 30)

now = str(datetime.now())
base_date = str(now.split(' ')[0].replace('-', ''))
base_time = int(str(int(now.split(' ')[1][:2])-1) + '00')

# print(now)
# print(base_date)
# print(base_time)

url = f"http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst?serviceKey={serviceKey}&numOfRows=60&pageNo=1&dataType=json&base_date={base_date}&base_time={base_time}&nx={nx}&ny={ny}"
print("url : " , url)

response = requests.get(url, verify=False)
res = json.loads(response.text)
print("text : " , res)
    
informations = dict()
for items in res['response']['body']['items']['item'] :
    cate = items['category']
    fcstTime = items['fcstTime']
    fcstValue = items['fcstValue']
    temp = dict()
    temp[cate] = fcstValue
    
    if fcstTime not in informations.keys() :
        informations[fcstTime] = dict()
    informations[fcstTime][cate] = fcstValue
# print(f"informations : {informations}")

# 시간별 정보 포함하여 출력
deg_code = {0 : 'N', 360 : 'N', 180 : 'S', 270 : 'W', 90 : 'E', 22.5 :'NNE',
           45 : 'NE', 67.5 : 'ENE', 112.5 : 'ESE', 135 : 'SE', 157.5 : 'SSE',
           202.5 : 'SSW', 225 : 'SW', 247.5 : 'WSW', 292.5 : 'WNW', 315 : 'NW',
           337.5 : 'NNW'}

def deg_to_dir(deg) :
    close_dir = ''
    min_abs = 360
    if deg not in deg_code.keys() :
        for key in deg_code.keys() :
            if abs(key - deg) < min_abs :
                min_abs = abs(key - deg)
                close_dir = deg_code[key]
    else :
        close_dir = deg_code[deg]
    return close_dir

# 함수 실행
deg_to_dir(0)

# 방위 정보 포함하여 출력
pyt_code = {0 : '강수 없음', 1 : '비', 2 : '비/눈', 3 : '눈', 5 : '빗방울', 6 : '진눈깨비', 7 : '눈날림'}
sky_code = {1 : '맑음', 3 : '구름많음', 4 : '흐림'}

for key, val in zip(informations.keys(), informations.values()) :
#     print(key, val)
    # val['LGT'] -- 낙뢰 
    template = f"""{base_date[:4]}년 {base_date[4:6]}월 {base_date[-2:]}일 {key[:2]}시 {key[2:]}분 {(placeCode_select(nx, ny)[1], placeCode_select(nx, ny)[2], placeCode_select(nx, ny)[3])} 지역의 날씨 :  """ 
    
    
    # 맑음(1), 구름많음(3), 흐림(4)
    if val['SKY'] :
        sky_temp = sky_code[int(val['SKY'])]
#         print("하늘 :", sky_temp)
        template += sky_temp + " | "
    
    # (초단기) 없음(0), 비(1), 비/눈(2), 눈(3), 빗방울(5), 빗방울눈날림(6), 눈날림(7)
    if val['PTY'] :
        pty_temp = pyt_code[int(val['PTY'])]
#         print("강수 여부 :",pty_temp)
        template += pty_temp + " | "
        # 강수 있는 경우
        if val['RN1'] != '강수없음' :
            # RN1 1시간 강수량 
            rn1_temp = val['RN1']
#             print("강수량(1시간당) :",rn1_temp)
            template += f"시간당 {rn1_temp}mm " + " | "
    
    # 기온
    if val['T1H'] :
        t1h_temp = float(val['T1H'])
#         print(f"기온 : {t1h_temp}℃")
        template += f" 기온 {t1h_temp}℃ " + " | "
    # 습도
    if val['REH'] :
        reh_temp = float(val['REH'])
#         print(f"습도 : {reh_temp}%")
        template += f"습도 {reh_temp}% " + " | "
    # val['UUU'] -- 바람
    
    # val['VVV'] -- 바람
    
    # 풍향/ 풍속
    if val['VEC'] and val['WSD']:
        vec_temp = deg_to_dir(float(val['VEC']))
        wsd_temp = val['WSD']
#         print(f"풍속 :{vec_temp} 방향 {wsd_temp}m/s")
        
    template += f"풍속 {vec_temp} 방향 {wsd_temp}m/s"
    print(template)