# Dictionary
# {Key1: Value1, Key2: Value2, Key3: Value3, ...}

book = {"name": "1234", "number": "111-111"}
print(book)

dict2 = {"name": "강만두", "age": 10, "job": "댕댕이"}

# 추가
dict2["pro"] = {"python": "상", "c#": "하", "c++": "중"}

# 추가 (딕셔너리는 따로 함수가 필요없음)
# 변수명[key] = value

# value
# 모든 타입을 다 저장할 수있다. 리스트,튜플
# 딕셔너리 자체도 다 ~ 저장가능

print(dict2)
print("-" * 35)
print(dict2["pro"]["python"])

# 딕셔너리는 따로 추가하거나 수정하는것이
# 똑같다.
# key를 작성해서 실행을 하면 만약 key
# 딕셔너리 변수에 있다면 값을 수정!
# key없으면 새로운 객체를 생성한다.
dict3 = {}

dict3[1] = [1, 2, 3]
print(dict3)
print(dict3[1][1])

dict3[10] = (1, 2, 34)
print(dict3[10])

# key 중복적이면 안된다.(고유한 키)
#  문자,숫자,튜플 나머지는 안됨!

# value 중복적인 값 저장 가능!

# 딕셔너리 key만 꺼내고 싶을 경우
seohee = {"name": "seohee", "age": 20, "gender": "f"}

# 사용하고 싶을 경우에는 형변환 list()
print(seohee.keys())
print(seohee.values())

# 딕셔너리는 반복을 돌리면 key가 반환
for x in seohee.values():
    # print(seohee[x])
    print(x)

# del dict3
# print(dict3)

# 딕셔너리는 반복을 돌리면 key가 반환
# items(): 모든 키와 값을 쌍으로 가져오기
for key, value in seohee.items():
    # print(seohee[x])
    print(f"{key}: {value}")

    # seohee 길이 구하기
print("seohee 길이:", len(seohee))

# name key가 seohee 변수안에 있니?
# 딕셔너리는 in 연산자를 사용할 때
# key 기준으로 검색한다
print("name" in seohee)

# value 기준으로 검색 한다.
print("이서희" in seohee.values())

# 내가 삭제할 값을 반환해서 출력
# 딕셔너리 pop('key')
age = seohee.pop("age")
print("삭제한 나이:", age)

# 안에 있는 데이터를 모두 삭제!
seohee.clear()

# =======================================
print("-" * 40)

list1 = [i for i in range(1, 6)]
print(list1)

dict5 = {i: i**2 for i in range(1, 6)}
print(dict5)
