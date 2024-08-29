import chardet
import csv

def det(filepath):
  result = ' '
  # 'rb' : csv처럼 이진파일들을 읽어올 때 사용하는 모드
  with open(filepath,'rb') as f:
    # detect() : 인코딩 감지하는 역할
    result = chardet.detect(f.read())
    print(result)
  return result['encoding']

def read_csv_file_open(filepath):
    # 인코딩
    encoding = det(filepath)
    print(f"인코딩 타입 : {encoding}")

    reader = ''
    with open(filepath,'r',encoding=encoding) as f:
        reader = csv.reader(f)
        print(type(reader))

        for line in reader:
            print(line)
    return list(reader)


filepath = "C:/fullstack/part5/src/Day6(240829)/colab/myCsvEx1.csv"  # 절대 경로

read_csv_file_open(filepath)