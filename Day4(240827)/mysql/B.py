# A.py 파일을 포함을 해서 그 안에 있는
# 내용들을 출력, 메서드 실행!

# 모듈
#  - 함수,클래스,변수 정의하는 파일 
#  - 다른 파이썬 파일에서 가져가서 사용할 
#    수 있도록 정리해놓은 파일!

#  - 여러개의 파이썬 파일에서 똑같은 (공통적인)
#    내용을 사용할 때 중복적으로 명령문을
#    작성하지 않고 미리 만들어놓은 파일을
#    이용하면 좋다! ( 재사용!)

# 파일명만 import에 작성하면 된다.

#import A
from A import *
print(var)
# print(A.var)
# print(A.string)

import test
print(test.string)

# 파일을 찾을 때 
# B.py 폴더 안에서 먼저 파일을 찾는다
# 파일이 없으면 
# 예외 
#ModuleNotFoundError: No module named 'requests'

import sys
#print(sys.path)

# 경로 추가
# 절대경로
sys.path.append('C:\\fullstack')

test.show()
# 상대경로
print(test.string)