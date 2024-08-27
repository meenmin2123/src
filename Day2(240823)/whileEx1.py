#문제 1
'''
num = 1
while num < 11 :
    print("나무를", num, "번 찍어서 안 넘어가는 나무 없다.")
    num += 1
'''
    
#문제 2
'''
num1 = 1
while num1 < 6:
    print("*" * num1) 
    num1 += 1
'''

#문제 3
'''
num2 = 2
i = 1
while num2 < 10:
    for i in range(1,9): 
        print(num2, "단 : " , num2 * i)
    
    num2 += 1
'''

#문제 4

num = input("이름 : ")
count = int(input('문제 개수:'))
# 문제를 푼 개수를 저장함
totalCount = 0
start = 1
 
while start <= count:
    save = input(f'{start}번 문제를 해결했니?')

# 문제 개수만큼 반복문을 작성하면 됨.
    save = save.lower()
    if save == 'y':
        totalCount += 1
    start += 1

print(num,"학생, 총", totalCount,"번 해결함")

# 문제 5




