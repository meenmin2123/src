# Function
# 함수 : 입력값을 받아 출력값을 반환하는 코드의 묶음

# def 함수명(매개변수) :
#     실행할 문장

#  def 함수명(매개변수):
#      실행할 문장
#      return 값

def info(name, age = 0):
    # 문자랑 문자 연결할 때 +
    print("이름 : ", name)
    print("나이 : ", age)

# 함수 실행
info("강만두",11)
info("강만두")

print("*" * 30)
# 함수의 매개변수한테 기본값을 설정 
# 기본값을 설정하면 값이 들어오면 들어온 
# 값으로 처리를 하고 값이 안 들어오면 
# 기본값으로 저장한다.
# 기본값 설정은 뒤에서 부터!
def info(name='무명',age=0):
    # 문자랑 문자를 연결 할 때는 + 
    print("이름:",name)
    print("나이:",age)

# 함수 실행
info("강만두",11)
info("강만두")
info()

print("*" * 30)

# 더하기
def add(a=0 , b=0):
    if a == 0 and b == 0:
        return '0을 입력해서 계산 못함.'
    return a + b

result = add()
print(result)

result2 = add(10,2)
print(result2)

print("*" * 30)

def longest(a,b,c):
    sizeA = len(a)
    sizeB = len(b)
    sizeC = len(c)

    if sizeA >= sizeB and sizeA >= sizeC:
        return a
    elif sizeB >= sizeA and sizeB >= sizeC:
        return b
    else :
        return c

print(longest('one','second','three'))

print()

def longe(a,b,c):
    # return max(a,b,c)
    return max(a,b,c,key=len)
print(longe('one','second','three'))
