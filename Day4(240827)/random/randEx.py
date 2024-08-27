import random

# 정수값 출력
rand = random.randint(1,3)
print(rand)

# 리스트에서 랜덤으로 값을 선택
items = ['python','java','spring','html','javascript']

# choice(리스트) 리스트 안에 데이터 중에서 하나를 뽑음.
rend_item = random.choice(items)
print(rend_item)

# 여러 개 뽑기(중복적으로)
# choices(리스트, 추출할 데이터 개수)
rend_item2 = random.choices(items,k=2)
print(rend_item2)

# 리스트 섞기
print("셔플 전 :", items)
random.shuffle(items)
print("셔플 후 :",items)
