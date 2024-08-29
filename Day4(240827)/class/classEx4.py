class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age
        print(f"부모:{self.name}")


# 상속 받음
class Student(Person):

    # 매개변수 생성자
    # 오버로딩 지원X
    def __init__(self, name=None, age=None, id1=0):
        super().__init__(name, age)
        self.id1 = id1
        print("자식 클래스")

    def info(self):
        print("이름 :", self.name)
        print("나이 :", self.age)
        print("학번 :", self.id1)


# 객체 생성 시
# - 자식 클래스에서 객체 생성 시 부모클래스 객체 생성하는데 매개변수 받는 생성자
stu = Student()
stu2 = Student("강만두", 10, 1004)
print(stu.name)
print(stu2.name, stu2.age, stu2.id1)


# 파이썬은 다중상속이 가능하다.
class A:
    def action(self):
        print("A action()")


class B:
    def action(self):
        print("B action()")


# 똑같은 메서드가 있을 경우 먼저 상속한 A클래스의 action이 우선적으로 호출됨
class C(A, B):
    def action(self):
        print("C action()")


# 객체 생성
c1 = C()
c1.action()

# 클래스 상속 구조
# - Object 클래스는 모든 클래스가 자동으로 상속
# - 다형성의 개수
print(C.__mro__)
print(C.mro())


class A:

    def __init__(self):
        print("A클래스")


class B(A):
    def __init__(self):
        super().__init__()
        print("B클래스")


class C(A):
    def __init__(self):
        super().__init__()
        print("C클래스")


# 부모 클래스를 호출할 때 클래스 이름
# 다중 상속 때문에 상속할 때 구조를 잘 생각해야함.
class D(B, C):
    def __init__(self):
        super().__init__()
        print("D클래스")


# 똑같은 메서드가 있을 경우 먼저 상속한
# A클래스의 action이 우선적으로 호출된다.
# B, C 각각 클래스 인데 부모는 A
# B의 부모가 C 클래스 x

d1 = D()
