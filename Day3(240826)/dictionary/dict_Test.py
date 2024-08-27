# 1
"""
print("목적지를 선택해주세요.")
obj = int(input('목적지 선택( 1. 춘천 / 2. 부산 / 3. 대구 / 4. 수원)'))
if obj == 1:
    val_obj = 5000
elif obj == 2:
    val_obj = 30000
elif obj == 3:
    val_obj = 20000
elif obj == 4:
    val_obj = 10000

print(f"목적지 선택 금액 : {val_obj}")
    
print("열차 종류를 선택해주세요.")
train = int(input('열차 선택( 1. KTX / 2. 새마을호 / 3. 무궁화호 )'))

if train == 1:
    val_train = 10000
elif train == 2:
    val_train = 5000
elif train == 3:
    val_train = 3000
    
print(f"기차 선택 금액 : {val_train}")
    
print("좌석 종류를 선택해주세요.")
sit = int(input('열차 선택( 1. 좌석 / 2. 입석 )'))
    
if sit == 1:
    val_sit = 0
elif sit == 2:
    val_sit = 2000

print(f"좌석 선택 금액 : {val_sit}")

total = val_obj + val_train + val_sit

print(f"최종 금액 : {total}")
""" 
# -------------------------------------------------
'''
destination_prices = {
    "1. 춘천" : 5000,   # 춘천
    "2. 부산" : 30000,  # 부산
    "3. 대구" : 20000,  # 대구
    "4. 수원" : 10000   # 수원
}

train_prices = {
    "1. KTX" : 10000,  # KTX
    "2. 새마을호" : 5000,   # 새마을호
    "3. 무궁화호" : 3000    # 무궁화호
}


seat_prices = {
    "1. 좌석" : 0,      # 좌석
    "2. 입석" : 2000    # 입석
}

def selection_price(prices_dict, prompt):
    print("prompt : ", prompt)

    for key in prices_dict:
        print(key)

    choice = input("선택 > ")

    return prices_dict.get(choice, 0)

val_obj = selection_price(destination_prices, "목적지를 선택해주세요.")
val_train = selection_price(train_prices, "열차 종류를 선택해주세요.")
val_seat = selection_price(seat_prices, "좌석 종류를 선택해주세요.")

total = val_obj + val_train + val_seat

print(f"최종 금액 : {total}원")
'''
print('-'*30)

# 2
icecream = {
    '메로나' : 1000,
    '폴라포' : 1200,
    '빵빠레' : 1800
}

print(icecream)
print('-'*30)

# 3
icecream['죠스바'] = 1200
icecream['월드콘'] = 1500

print(icecream)
print('-'*30)

# 4
print("메로나 가격 : " , icecream['메로나'])
print('-'*30)

# 5
icecream['메로나'] = 1300
print(icecream)
print('-'*30)

# 6
del icecream['메로나']
print(icecream)
print('-'*30)

# 7
inventory = {
    '메로나' : [300, 20],
    '비비빅' : [400, 3],
    '죠스바' : [250, 100]
}

print(inventory)
print('-'*30)

# 8
print(inventory['메로나'][0], "원")

# 9
print("재고량 :",inventory['메로나'][1],"개")

# 10
inventory['월드콘'] = [500,7]
print(inventory)

print('-'*30)
# 11
icecreamDict = {
    '탱크보이' : 1200,
    '폴라포' : 1200,
    '빵빠레' : 1800,
    '월드콘' : 1500,
    '메로나' : 1000
}

print(icecreamDict.keys())

print('-'*30)
# 12
def print_reverse(str):
    return  ''.join(reversed(str))

print(print_reverse('python'))
print('-'*30)
# 13
def print_score(scoreList):
    sumVal = sum(scoreList)
    return float(sumVal / len(scoreList))

print(print_score(([1,2,3])))

# 14
print(icecreamDict.values())

# 15
print("총 합:",sum(icecreamDict.values()),"원")

# 16
new_product = {
    '팥빙수' : 2700,
    '아맛나' : 1000
}

icecreamDict.update(new_product)
print(icecreamDict)

