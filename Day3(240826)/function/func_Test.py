# 문제1

score = [50, 60, 70, 80, 90]

def passFail(lis):
    sumVal = sum(lis)
    avg = sumVal / len(lis)

    if avg >= 60:
        return print("pass!")
    else :
        return print("fail!")
    
print(passFail(score))

# 문제2
# 하루: 86,400

def convert_seconds_to_hms(seconds):
    if seconds > 0 and seconds <= 24 * 60 * 60:  # 하루 미만인지 확인
        hour = int(seconds / (60 * 60))  # 시간 계산
        minute = int((seconds % (60 * 60)) / 60)  # 남은 초로부터 분 계산
        second = int(seconds % 60)  # 남은 초 계산
        return hour, minute, second
    else:
        raise ValueError("입력 시간이 하루를 초과합니다.")

# 사용자로부터 초 입력받기
try:
    res = float(input("변환할 초 > "))
    hour, minute, second = convert_seconds_to_hms(res)
    print(f"시간: {hour}, 분: {minute}, 초: {second}")
except ValueError as e:
    print(e)

