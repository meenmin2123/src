# list()형 변환
# 리스트 형식으로 반환이 아니라 객체로 반환됨.
# range(개수) 0부터 끝-1
list1 = list(range(10))
print(list1)

print("*" * 30)
# 리스트를 생성할 때 반복문을 이용해서 리스트를 생성할 수 있음.
# 실행 순서
# 1. range(1,6) 1부터 5까지의 숫자를 생성
# 2. 생성된 숫자를 순서대로 꺼내와서 i에
#    저장한다.
# 3.  저장된 값을 이용해서 리스트를 생성한다.
list2 = [i for i in range(1, 6)]
print(list2)

"""
* list Comprehension
  - 파이썬에서 리스트를 간단하게 한줄로 선언
  - 리스트 생성시 코드의 가독성을 높여준다.
  [data for item in iterable]
  data : 값이 들어온다.
  item : 현재 반복되있는 값
  iterable : 리스트, 숫자범위(range),문자열..
"""

list3 = ["a", "b", "c"]
upperList = [str.upper() for str in list3]
print(upperList)

# 짝수만 리스트에 포함
# 1 ~ 10까지 숫자 중에서 짝수만
numbers = [i for i in range(1, 11) if i % 2 == 0]

numbers = [i for i in range(1, 11) if i % 2 == 0]

# 1. range() 범위값 반환
# 2. 범위값에서 하나씩 꺼내서 i에 저장
# 3. 조건검사 이때 True이면 리스트에 포함한다.

# -6부터 10까지 반복을 하는데 홀수만 리스트에
# 저장하기! 문자열로 저장

# 숫자 -> 문자로 변경해서 저장 str()
# 문자 -> 숫자 (정수)  int()

numbers3 = [str(i) for i in range(-6, 11) if i % 2 == 1]
print(numbers3)

# 구구단을 for문을 이용해서 range로 2~9단까지 출력
for i in range(2, 10):
    print(f"====={i}단*=====")
    for j in range(1, 10):
        print(f"{i} * {j} : ", i * j)

# 한줄로 작성할 때
gugudan = [[i * j for j in range(1, 10)] for i in range(2, 10)]
# print(gugudan)

for index, value in enumerate(gugudan):
    print(index + 2, "단:", value, sep="")

# start 속성을 이용해서 index값을 지정할
# 수 있다. 기본적으로 0으로 되어있음
# join()
# map(str,value)
#  여러개의 문자를 각각의 타입으로 변환X
for index, value in enumerate(gugudan, start=2):
    print(f"{index}단:", value)

# 여러개의 데이터를 입력받아서 각각의 데이터
# 로 리스트에 저장
user = input("여러개 데이터: (10 1.1 st)")
values = []
# 입력 문자를 공백으로 분리해서 각 값 처리
for i in user.split(" "):
    if i.isdigit():  # True
        # isdigit() 정수로 변환 가능하니?
        values.append(int(i))
    elif "." in i and i.replace(".", "", 1).isdigit():
        values.append(float(i))

    else:
        values.append(i)

print(values)
print()


# 예외처리를 이용해서 여러 데이터를 입력받는다.
def value(val):
    try:
        # 실행할 문장 정수형로 형변환이 되면
        # 정수형으로 리턴된다.
        return int(val)
    except ValueError:
        print("정수형?")
        pass

    # 실수형태로 형변환이 된다.
    # 예외 안 생김 return 을이용해서 실수로
    # 변경하고 함수끝!
    try:
        return float(val)
    except ValueError:
        print("실수형?")
        pass

    return val


values = list(map(value, user.split()))

print(values)


def value(val):
    try:
        return float(val)
    except ValueError:
        print("정수형")
        return

    return val


# input()        문자
# int(input())   정수
# float(input()) 실수
