# /*
#    * # 숫자이동[1단계]
#    * 1. 숫자2는 캐릭터이다.
#    * 2. 숫자1을 입력하면, 캐릭터가 왼쪽으로
#    *      숫자2를 입력하면, 캐릭터가 오른쪽으로 이동한다.
#    * 3. 단, 좌우 끝에 도달했을 때, 예외처리를 해야한다.
#    * 4. {0, 0, 2, 0, 0, 0, 0};  ==> 왼쪽 ==> {0, 2, 0, 0, 0, 0, 0};
#    * 
#    */
'''
roadList = [0, 8, 0, 0, 0, 0, 0]
print(roadList)

while True:
    value = int(input(">"))

    if value == 2:
        index = roadList.index(8)
        # print(index)
        if index < len(roadList) - 1:
            roadList[index] = 0
            roadList[index+1] = 8
            print(roadList)
        else : 
            print("더 이상 이동할 수 없습니다.")
            print(roadList)
            continue

    elif value == 1:
        index = roadList.index(8)
        # print(index)
        if index > 0 :
            roadList[index] = 0
            roadList[index-1] = 8
            print(roadList)
        else : 
            print("더 이상 이동할 수 없습니다.")
            print(roadList)
            continue
    elif value == 0:
        print("종료!")
        break
    else :
        print("다시 입력해주세요")
        continue
'''
game = [0, 0, 0, 2, 0, 0, 0]

# 게임판 출력
start = 0
size = len(game)

# 변수 
values = ""   # 게임판 출력 변수
newIndex = 0  # 새로운 인덱스를 지정하는 변수

while start < size :
    if game[start] == 0:
        values += "__ "
    else:        
        values += "옷 "
    start += 1
print(values)

player = game.index(2) # 2번의 위치를 찾아라!
move = int(input('좌 1: 우:3'))

# 1번을 눌렀을 때 이동할 수있는 index 범위
if move == 1 and player > -1:
    # 왼쪽을 눌렀을 때 
    newIndex = player -1

elif move == 3 and player < size -1:
    # 오른쪽을 눌렀을 때 
    newIndex = player +1

else: # 더이상 이동할 수 없다! 
    print(" 더 이상 이동 못한다!")

# 이동하는 명령문 
# 위치변경 
game[player],game[newIndex] = \
game[newIndex],game[player] 



# 관리비

apt = [
    [101, 102, 103],
    [201, 202, 203],
    [301, 302, 303]
]

pay = [
    [1000, 2100, 1300],
    [4100, 2000, 1000],
    [3000, 1600, 800]
]

# 문제 1) 각층별 관리비 합 출력
# 정답 1) 4400, 7100, 5400

floor = 1

while floor <= len(apt) : 
     print(f"{floor}층 관리비", sum(pay[floor-1]),"원")
     floor += 1

# 문제 2) 호를 입력하면 관리비 출력
# 예    2) 입력 : 202  관리비 출력 : 2000

found = False
'''
while True:
    num = int(input("어디 호수의 관리비가 궁금하신가요? : "))

    for i in range(len(apt)):
        if num in apt[i]:
            numPay = pay[i][apt[i].index(num)]
            print(f"{num}호의 관리비는 {numPay}원 입니다.")
            found = True
            break
    if num == 0:
        print("종료!")
        break

    if not found :
        print("해당 호수가 존재하지 않습니다.")  
    continue
'''

# 문제 3) 관리비가 가장 많이 나온 집, 적게 나온 집 출력
# 정답 3) 가장 많이 나온 집(201), 가장 적게 나온 집(303)

# 문제 4) 호 2개를 입력하면 관리비 교체