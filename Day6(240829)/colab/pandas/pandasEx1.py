# * Pandas
#   1) Series : 1차원 리스트 Series 객체를 제공. 인덱스 데이터 선택 빠르게 할 수 있음
#   2) DataFrame : 2차원 데이터 구조를 이용해서 행과 열을 이용해서 데이터를 쉽게 조작 분석
#   - 결측치
#   - 이상치 : 데이터에서 다른 데이터들하고 크게 차이가 나는 값
# * 2차원 구조 'DataFrame'
#   - DataFrame(값,conlums= 열 이름 리스트)
#   - 리스트,딕셔너리,넘파이의 배열
#   - 리스트를 이용해서 한 행씩 지정 

import pandas as pd

a = pd.Series([1,3,5,7,9])
print(a)

list1 = list([
    ['한빛','남자','20','180'],
    ['한결','남자','21','177'],
    ['한라','여자','20','160']
])

col_names =['이름','성별','나이','키']

# 데이터프레임 객체를 생성
df = pd.DataFrame(list1,columns=col_names)
#print(df)
df

dict1 = {'이름':{0:'한빛', 1:'한결', 2:'한라'},
         '성별':{0:'남자', 1:'남자', 2:'여자'},
         '나이':{0:'20', 1:'21', 2:'20'},
         '키':{0:'180', 1:'177', 2:'160'}}

df2 = pd.DataFrame(dict1)
pd.DataFrame(dict1)
df2

# ------
import pandas as pd

list1 = list([['허준호','남자','30','183'],
 ['이가원','여자','24','162'],
 ['배규민','남자','23','179'],
 ['고고림','남자','21','182'],
 ['이새봄','여자','28','160'],
 ['이보람','여자','26','163'],
 ['이루리','여자','24','157'],
 ['오다현','여자','24','172']])

col_names = ['이름','성별','나이','키']

df = pd.DataFrame(list1, columns=col_names)
# df

# 만약 데이터프레임객체를 csv로 저장
# header : 열이름을 포함할지 여부 설정
# - True : 열 이름이 csv파일의 첫번쨰 줄에 작성
# - False :  열 이름이 csv파일의 첫번쨰 줄에 작성되지 않음.
# index : index를 포함 여부를 설정
# - True : 인덱스가 csv파일에 추가됨
# - False : 추가 안됨

df.to_csv('test.csv',header=True ,index=False, encoding='utf-8')

# csv 읽기
df2 = pd.read_csv('test.csv',encoding='utf-8')

# 모든 열을 조회
df2.columns
df2['이름']

# ---------

# 데이터 미리보기 기능
# - head(n) : 상위 n개 데이터 조회
# - tail(n) : 하위 n개 데이터 조회

df2.head()
df2.tail()

# -----------

# 행 정렬 
#  - 인덱스나 특정 열의 값을 기준으로 행을 정렬
#  - 기본 오름차순설정

# 인덱스 기준으로 정렬
# axis 축을 지정
#  0  행을 기준으로 정렬
#  1  열을 기준으로 정렬

# -----------
# 정렬
# ascending = Fasle 내림차순 / True 오름차순

df2.sort_values(by=['이름','키'],ascending=False).head()

# -----------
# 데이터 조회
df2 = pd.read_csv('test.csv',encoding='utf-8')

df2[['이름','나이']].head()
df2.iloc[0:3]


# -----
# 키 180 이상인 사람만 조회
# import pandas as pd

# 데이터 조회
# df2 = pd.read_csv('test.csv',encoding='utf-8')

df2[df2['키']>=180]
df2[df2['나이'].isin([21,23])]
df2[(df2['성별'] == '여자') & (df2['키']>160)]
df2[(df2['성별'] == '남자') | (df2['나이']>=28)]
df2[(df2['이름'].str.contains('봄'))]

# ------------
df2['나이'].min()
df2['나이'].max()
df2['나이'].mean()    # 평균
df2['나이'].median()  # 중앙값
df2['나이'].std       # 표준편차
df2['나이'].count()   # 데이터 개수 - 열에서 데이터가 존재하는지(결측치가 아닌것만)
df2['나이'].sum()     # 합

# 여러 개의 통계값을 보고 싶을 경우
df2.describe()

# -----------
# 인덱스 4번 행의 value을 5씩 증가
df2.loc[4,'키'] += 5
df2

# 변경된 데이터만 출력
df2.loc[[4]]
df2.loc[[4],['이름','키']]

# 다수의 행 선택
df2.loc[[2,4,6]]

# 모든 행에서 특정 열만 선택
df2.loc[:,'이름']

# -----------
df2.loc[1:3,'키'] = ['NULL'] * 3
df2 
