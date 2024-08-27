# 여러 개의 리스트 값을 꺼낼 때
# 슬라이싱 : 원하는 값을 일부분만 추출함.
list1 = [1,2,3,4,5,6]

# 2, 3, 4
# 리스트명[시작 인덱스(값 포함) : 끝 인덱스(값 포함x)]  
print(list1[1:4])

print(list1[:4])

# 4번부터 마지막 슬라이싱
print(list1[1:]) 
print(list1[-3:]) 

# 리스트 +
a = [1,2,3]
b = [6,4,5]

# 결과창 지우기 cls
# a리스트에 b를 연결한다.
print("a+b : ", a + b)
# b리스트에 a를 연결한다.
print("b+a : ",b + a)

print(a * 3)

num = 10
print(num)
del num
print("삭제!")

del list1[0]    # 인덱스만 삭제
print("인덱스만 삭제!")

del list1       # 리스트 전체 삭제.
print("리스트 삭제!")

#-----------------------------------------------

c = [10, 3, 90, 34, 52]
print(max(c))
print(min(c))

# c 리스트 합계
print("합계 : ",sum(c))

c.sort()
# 오름차순 정렬
print("오름차순 : ", c)

c.reverse() # c.sort(reverse=True)
# 내림차순 정렬
print("내림차순 : ", c)

strList = ['d','e','y','r','b','o']

strList.sort()
print("오름차순 : ", strList)

strList.reverse()
print("내림차순 : ", strList)

sorted(strList)
print("내림차순 : ", strList)

# 비어있는 리스트 생성
# 학생들의 점수를 저장 - 6개 입출력
'''
scoreList = []
num = 1
while num < 7:
    score = int(input(f"{num}번 학생의 점수 : "))
    scoreList.insert(num-1,score)
    num += 1
print("입력받은 리스트 : ",scoreList)
'''

# 입력 받은 점수 중 85점 있는지 확인
# 몇번째 인덱스에 있는지 출력
# 만약 점수 없으면 '점수 없음!' 반환
scoreList1 = []
num = 1
while num < 7:
    score = int(input("점수 입력 : "))
    scoreList1.append(score)
    num += 1

find = int(input("찾을 점수 : "))

if find in scoreList1:
    print(f"{find}점 : ", scoreList1.index(find),"번쨰 인덱스에 있다!")
else:
    print("점수 없음.")
print("입력받은 리스트 : ",scoreList1)

# 찾으려고 하는 점수가 중복일 경우
scoreList2 = [85,100,90,75,85]

# index(value,start,end)
# value 값 (필수)
# start 검색을 시작할 인덱스 (선택 사항)
# end 검색을 종료할 인덱스 (선택 사항) \

#-----------------------------------------------

# 대소문자 구별함.
proList = ["python", "java", "sql", "html", "css", "javascript", \
           "spring", "springboot"]
print(proList.index("java"))

# 리스트 삭제 - remove()
proList.remove("java")
print("삭제 후", proList)

# pop(index) 함수
#  특정 인덱스에 해당하는 값을 제거하고
#  그 값을 반환하는 기능을 가진다. 
# 삭제를 하게 되면 뒤에 있는 데이터가 자동으로
# 앞쪽으로 온다.

# 인덱스 없으면 에러! 
# pop() 맨 마지막 데이터를 삭제한다

#TypeError: 'str' object cannot be
#         interpreted as an integer
# print(proList.pop())

# 스택구조에서 값을  삭제할 때 pop()