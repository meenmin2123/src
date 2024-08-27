# 함수 리턴 

# 튜플(tuple)
# - 리스트랑 똑같은 자료형
# - 한번 값을 저장하면 변경을 못함.
# - 삭제, 수정, 추가 못함
# - ex) 위치 정보, 여러 개의 리턴 값을 하나의 타입

# 상수
# - 
def a():
    return 1

def b():
    return 1,2

print(a())
print(b())

tuple1 = ()
print(type(tuple1))
print(len(tuple1))

list1 = []
list1.append(10)

# 1
num = (1)
print(type(num))

tuple2 = (1,)
print(type(tuple2))

tuple3 = ('1',1.1,1,'가')
tuple4 = 1,2,3,4,5,6,7
print(tuple3)
print(tuple4)
print(type(tuple4))

print(tuple3[0])
print(tuple4[1:3])

# 튜플 데이터 변경
# tuple4[1] = 100   #에러발생
list1 = []
list1.append(10)
print(list1)

# 튜플 -> 리스트 변경
temp = list(tuple4)
print(temp)

temp[1] = 100

tuple4 = tuple(temp)
print(tuple4)

print("*" * 30)

def greet(name="Guest"):
    print(f"Hello,{name}")

greet()
greet("만두")

# 여러 숫자의 합을 계산
# 가변인자(*) - 튜플 형태
def addNumbers(*num):
    print(num)

print(addNumbers(1,2,3))
print(addNumbers(1,2,3,4,5,6,74,8,9))
print(addNumbers(1))

def print_msg(*msg):
    for i,n in enumerate(msg,1):
        print(f"{i}. {n}")

print_msg("!","2","$","5","3","hello")

# 가변인자 두 개 같이 사용가능? => 사용 x
# def info(*a, *b):
#     print(a,b)

# 가변 인자는 맨 마지막에 한번만 사용 가능함.
def info2(c=0, *d):
    print(c)
    print(d)

info2(1,2,3,4,5,6,6,7,8,8,9)