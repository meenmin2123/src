class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x},{self.y})"


# 객체 생성
p1 = Point(1, 2)
p2 = Point(3, 4)

# + 연산자 오버로딩 (__add__ 자동으로 호출)
p3 = p1 + p2  # p1.__add__(p2)
print(p3)

a = 2
b = 10
c = a.__add__(b)
d = a.__sub__(b)
e = a.__mul__(b)
f = a.__truediv__(b)
g = a.__floordiv__(b)

print(c)
print(d)
print("곱하기 : ", e)
print("몫 : ", f)
print("몫 정수 : ", g)

# __mod__(self, other): % 연산자
# __pow__(self, other): ** 연산자
# __eq__(self, other): == 연산자
# __ne__(self, other): != 연산자
# __lt__(self, other): < 연산자
# __le__(self, other): <= 연산자
# __gt__(self, other): > 연산자
# __ge__(self, other): >= 연산자


# id : 예약어(파이썬이 미리 사용하는 키워드) , 변수로 사용 x
class Person:
    def __init__(self, id1, pw):
        self.id1 = id1
        self.pw = pw

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.id1 == other.id1 and self.pw == other.pw
        return False

        # isinstance of (in Java)와 비슷함.
        # Person 클래스의 인스턴스이거나 상속관계를 갖는 Person 관계 있으면
        # 데이터를 비교하고 관계 없으면 비교 안함.

    def __str__(self):
        return f"Person({self.id1},{self.pw})"


person1 = Person("만두", "공주")
person2 = Person("만듀", "메롱")

print(person1 == person2)


# -----------------------------------------------------------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


# 객체 생성
p = Point(3, 4)

# __repr__ 호출
print(repr(p))  # 출력: Point(3, 4)
