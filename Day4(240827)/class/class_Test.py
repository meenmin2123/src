class Human:

    def info(self):
        print("응애응애")

    def __init__(self,areum=None):
        self.areum = areum

    def __init__(self,name=None,age=None,gender=None):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self) -> str:
        return f"이름:{self.name}, 나이:{self.age}, 성별:{self.gender}"

    def who(self,name=None,age=None,gender=None):
        if name is not None:
            print(f"이름 : {name}")
        else:
            print(f"이름1:{self.name}")

        if age is not None:
            print(f"나이 : {age}")
        else:
            print(f"나이1:{self.age}")

        if gender is not None:
            print(f"성별 : {gender}")
        else:
            print(f"성별1:{self.gender}")

    def who(self):
        print("이름{} 나이:{} 성별:{}".format(self.name,self.age,self.gender))

    def setInfo(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        print(self.areum)
    

areum = Human()
areum.info()
human1 = Human("아름",25,"여자")
print(f"이름:{human1.name} 나이:{human1.age} 성별:{human1.gender}")

areum.who()

# ------------------------------------------------------------------------------------
# 252
class Human:
    pass

# 253 
areum = Human()
print(areum)

# 254
class Human2:
    def __init__(self):
        print("응애응애")

h1 = Human2()

# 255
class Human3:
    def __init__(self,name,age,g):
        self.name = name
        self.age = age
        self.g = g

    def __str__(self):
        return f"이름:{self.name},나이:{self.age} , 성별:{self.g}"
   
    # 260번 에러 원인!
    # 클래스 멤버 메서드는 무조건 매개변수
    # 첫번째는 자기 자신의 주소값 받아야된다.
    def who(self):
        print("이름{} 나이:{} 성별:{}"\
            .format(self.name,self.age,self.g))

    # 258번 코드 
    def setInfo(self,name,age,g):
        self.name = name
        self.age = age
        self.g = g
        print("수정됨")



ar = Human3("이름",25,"여자")
print(ar.name)

# 255 객체를 이용해서 값 출력


# 271
import random as r
class Account:

    # 클래스 변수
    acc_count = 0

    def info(self, bankName, bankNum):
        self.bankName = bankName
        self.bankNum = bankNum
    
    def __init__(self, bankName, bankNum=0):
        self.bankName = bankName
        self.bankNum = bankNum

        num1 = r.randint(0,999)
        num2 = r.randint(0,99)
        num3 = r.randint(0,999999)
    
        # zfill(width) : 문자열의 길이를 지정 후, 데이터 채움. 
        # - 만약 부족한 길이는 0으로 채움.

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)   
        num3 = str(num3).zfill(6)           

        self.bankNum = num1 + '-' + num2 + '-' + num3

        print("계좌번호:", self.bankNum)

        # 클래스 변수 증가
        Account.acc_count += 1

acc = Account("카카오뱅크")

# 261 ~ 264
class Stock:
    pass

class Stock2:
    def __init__(self,name,code):
        self.name = name
        self.code = code

    def __str__(self):
        # toString() 메서드랑 똑같음.
        # return 타입으로 str 타입으로 넘어가야하는데 print()실행하고
        # 문자열로 넘겨주는 리턴타입이 맞지 않아서 오류

        print(f"{self.name}")
        print(f"{self.code}")
    
    def set_name(self,name):
        self.name = name

stock = Stock2("삼성전자","005930")
print(stock)

stock.set_name("현대")
print(stock)

class MyClass:
    def __init__(self):
        # 비공개    
        self.__name = "private"

    def getNAme(self):
        return self.__name

muclass = MyClass()
print(muclass.getNAme)

# Protected : 자식 클래스와 상속한  만 접근이 가능하도록
# _변수명

