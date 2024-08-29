import pandas as pd

col_names = ['과목번호', '과목명' ,'강의실', '시간 수']
list1 = list([['C1','인공지능개론','R1',3],
              ['C2','웃음치료','R2',2],
              ['C3','경영학','R3',3],
              ['C4','3D디자인','R4',4],
              ['C5','스포츠경영','R2',2],
              ['C6','예술의 세계','R3',1]])

df = pd.DataFrame(list1, columns=col_names)
df

# 과목별 시간 수의 합계 구하기
df.groupby('과목명')['시간 수'].sum()

# 각 강의실에서 강의가 몇 번 열리는지 계산하기
df.groupby('강의실')['과목명'].count()

# 과목명 기준으로 오름차순 정렬하여 출력하기
df.sort_values(by='과목명', ascending=True)

# 특정 시간 수 이상인 과목만 필터링하기
# df[df['시간 수'] > 3] 

# 시간 수의 평균을 계산하고 4시간 이상인 과목 찾기
df['시간 수'].mean()
df[df['시간 수'] >= 4]