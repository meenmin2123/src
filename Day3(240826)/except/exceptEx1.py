# 파이썬 예외처리
# try : 예외가 발생할 문장
# except : 예외 처리하는 문장

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(e)

# 여러 예외처리!
try:
    result = int("abc")

except (ValueError, TypeError):
    print("타입에러 및 값 에러!")


try:
    result = int(input("정수:"))

except Exception as e:
    print(e)


# 문자열의 길이를 값으로 딕셔너리
# 생성
try:
    words = ["apple", "banana", "cherry"]
    lengths = {w: len(w) for w in words}
except Exception as e:
    print(e)

print("-" * 30)
# 딕셔너리를 이용해서 짝수

# 딕셔너리 생성
numbers = range(10)
even = {n: n for n in numbers if n % 2 == 0}
print(even)

# 문자열에서 대문자로만 키를 사용
string = "Hello World"
try:
    dict1 = {char: char.lower for char in string if char.isupper()}
except Exception as e:
    print(e)

# 문제 1
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

# 결과
# {'name': 'Alice', 'age': 25, 'city': 'New York'}

try:
    dict2 = {keys[i]: values[i] for i in range(len(keys))}

    print("dict2 : ", dict2)
except Exception as e:
    print(e)
else:
    # 예외없이 성공했을 때
    print("통과!")
finally:
    # 예외발생 하든 안하든 무조건 실행함.
    print("예외발생 하든 안하든 무조건 실행함.")


# rasie 강제적으로 예외를 발생시키는 것
def test(a, b):
    if a == 0 or b == 0:
        raise ZeroDivisionError
    return a / b


# main에서 처리하기
try:
    test(10, 0)
except Exception as e:
    print(e)
else:
    print("성공했는데?")
finally:
    print("운 좋네~")
