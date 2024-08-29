# 클래스 변수
class Student:
    # 클래스 변수 : 모든 학생들의 학번 관리
    next_id = 1

    def __init__(self, name):
        self.name = name
        self.student_id = Student.next_id
        Student.next_id += 1  # 다음 학생 학번

    def __str__(self):
        return f"({self.student_id}번 이름:{self.name})"


stu1 = Student("만두")
stu2 = Student("만듀")
stu3 = Student("공쥬")

print(stu1)
print(stu2)
print(stu3)


class StudentManager:
    def __init__(self):
        # 학생들을 관리하는 리스트
        self.stuList = []

    # 추가
    def add_student(self, name):
        # 생성된 객체 자체로 가져옴
        # def add_student(self,stu):
        #     self.stuList.appenf(stu)
        stu = Student(name)
        self.stuList.append(stu)
        print(f"학생 추가됨 : {stu}")

    # 삭제
    def remove_student(self, student_id):
        for student in self.stuList:
            if student.student_id == student_id:
                self.stuList.remove(student)
                print(f"학생 삭제됨:{student}")
                return  # 삭제 후 메서드 종료
        print(f"{student_id}의 학생을 찾지 못하였습니다.")

    # 찾기
    def find_student(self, student_id):
        for student in self.stuList:
            if student.student_id == student_id:
                print(student)
                return
        print(f"{student_id}의 학생을 찾지 못하였습니다.")

    # 조회
    def list_students(self):
        print("Student List:")
        for student in self.stuList:
            print(student)


manager = StudentManager()
manager.add_student(Student("Alice"))
manager.add_student(Student("Bob"))
manager.find_student(0)
manager.find_student(1)
manager.find_student(2)
manager.find_student(3)
manager.list_students()
