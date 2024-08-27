# input() : 문자형만 작성
str1 = input('정수 : ')

# input 
print(type(str1))

# 실수 -> 정수 ,  정수 -> 문자형
print("* 형변환 *")
str1 = int(str1)

print(type(str1))
print(str1)

# 정수
age = int(input("나이 : "))

# 실수
hei = float(input("키 : "))

# 문자
string = input("내용 : ")

# 사칙연산
# 곱하기
print("hello" * 5) 

print(age)
print(type(str1))
print(hei)
print(type(hei))
print(string)
print(type(string))

# map(변환할 타입, input().split())
# 여러 개를 한꺼번에 입력받고 싶을 때
list1 = input('여러 개의 문자를 입력 : ').split(' ')

print(list1)
print(list1)

# 파이썬에서 여러 개의 변수를 저장
a = 10; b = 20
c = 100; d = 20

#
a1, b1, c1 = 1000, 2000, 3000
print(a1)
print(b1)
print(c1)