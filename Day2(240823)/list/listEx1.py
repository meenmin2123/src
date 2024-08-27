# 클래스 : 다른 타입으로 타입만들고 여러 개 저장
# 배열 : 하나의 타입으로 여러개를 저장

# 리스트 생성 시 []
# 여러 개 저장
# 인덱스 사용 가능(0~)
# 순차적인 자료구조

list1 = [1,2,3,4]
list2 = [1.1, 1.2, 1.3]
list3 = ["a", "b", "c"]
list4 = [1, "python", 10.1234]

print(list1)
print(list2)
print(list3)
print(list4)

# 데이터 접근
print(list4[0])
print(list4[1])
print(list4[2])

# 파이썬만의 리스트 접근 방법
# 오른쪽에서 부터 인덱스를 이용해서 접근 가능 - 음수값 이용
print(list4[-1])
print(list4[-2])
print(list4[-3])

# 빈 리스트
list5 = []
print(list5)
                                                                                      
# 비어 있는 리스트느 저장할 공간이 없음.
# append() 로 공간 생성
# list5[0] = 10
# print(list5)

list5.append(10)
list5.append(20)
list5.append(30)
print(list5)

# 여러개 추가
list5.append([40,50,60])
print(list5)

print(list5[3])
print(list5[3][0])

# 리스트 안에 리스트 저장
list6 = [
    [1,2,3],
    [1.1, 2.2 ,3.3],
    ["python", "java", "spring"]
]

print(list6)

# 2차원 배열과 비슷함
print(list6[0][1])
print(list6[1][2])
print(list6[2][0])

numberList = [1,2,3,4,5]

# insert(인덱스 값)
numberList.insert(2, 6)
numberList.insert(0, "hello")
print(numberList)

# []괄호 하는 이유는 여러 개의 데이터를 어떤 타입으로 저장
nameList = ["이익준"]
nameList.extend(["강만두,프린세스"])
nameList.extend(["만두"])
print(nameList)

# 문제 1
# 수상자 명단
winner = ['박미아', '정민호', '김철수', '이영희', '손소정']

# 검색할 명단
checkName = ['정수지','김철수','박민아','전은진']

# in , not in
# 결과 값이 True, False
# 리스트 안에 검색하는 값이 있니? in 연산자
print('정수지' in winner)

# 리스트 안에 검색하는 값이 없니? not in 연산자
print('정수지' not in winner)

# 반복문하고 index번호를 이용해서 체크하는
# 명단을 수상자 명단에서 확인하기 
# len(리스트명)
# 리스트의 길이를 반환한다. 

index = 0
while index < len(checkName):
    name = checkName[index]

    if name in winner:
        print(f"{name}가 수상했는지 확인해라.")
    else:
        print(f"{name}가 수상하지 못했는지 확인해라.")

    index += 1


# 문제 2
productList = [
    ['비누', 3, 3], 
    ['칫솔', 5, 4],
    ['샴푸', 2, 1],
    ['치약', 4, 4],
    ['로션', 5, 3]]

print("2차원 리스트 길이 : ", len(productList))
size = len(productList)
index = 0

while index < size :
    # 판매 실적, 고객평가 점수 >= 4
    if productList[index][1] >= 4 and productList[index][2] >= 4:
        print(productList[index][0] + "우수 상품")
    else:
        print(productList[index][0] + "판매 중지")

    index += 1






