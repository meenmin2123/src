#for문 
# 횟수가 정해져있거나 반복해야되는 대상
'''
for 변수 in 객체:
    실행문
    실행문

 문자열,리스트
'''

for x in 'abc':
    print(x)

print("*" * 15)
'''
- 오류 발생 : 실수는 들어갈 수 없음.
- 숫자형 데이터는 들어올 수 없음. 여러 개의 데이터를 가지고 반복을 자동으로
수행할 때 사용하는 반복문
for y in 10:
    print(y)
'''

for v in ['1','2','3']:
    print(v)

print("*" * 15)

for v in [[1,2],[3,4],[5,6]]:
    print(v)

print("*" * 15)
# 1 ~ 5까지 출력 - for문 사용
# range : 숫자의 범위를 반환하는 range(시작,끝 -1) 
# - 끝나는 숫자는 데이터를 포함하지 않는다
for x in range(1,6):
    print(x)

print("*" * 15)
# range : 숫자의 범위를 반환하는 range(시작,끝 -1, 증감크기) 
for i in range(1,51,2):
    print(i)

print("*" * 15)
for j in range(10,0,-1):
    print(j)

print("*" * 15)

# 리스트의 값과 인덱스를 같이 출력
proList = ['java','python','html','css','javascript','spring']

# for 문으로 반복을 하면 값이 온다.
# 값과 같이 인데스(공간의 번호)
for p in enumerate(proList):
    print(p)

print("*" * 15)

for index,value in enumerate(proList):
    print("공간 : ", index)
    print("값 : ", value)

print("*" * 30)

# 두 개의 리스트를 동시에 반복
nameList = ['강만두','레이첼','엘리쟈베스','프린세스']
ageList = [10,11,12]
bloodList = ['A','O','AB','B']

for name,age,blood in zip(nameList,ageList,bloodList):
    print(f"{name}의 나이는 {age}이다, {blood}")

print("*" * 30)

# 1 2 4 5 -> 건너뛰기
for i in range(1,6):
    if i == 3:
        continue
    print(i)

print("*" * 30)
for a in range(1,6):
    if a == 3:
        print("stop")
        break
    print(a)

print("*" * 30)
# 무한반복은 while로 하는것이 편함
# import itertools

# for _ in itertools.cycle([None]):
#     print("python")

# while True:
#     res = input("?? >")
#     print(res)
