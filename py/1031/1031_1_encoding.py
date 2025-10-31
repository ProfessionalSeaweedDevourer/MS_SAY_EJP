import os

script_dir = os.path.dirname(os.path.abspath(__file__))

# 인코딩과 디코딩
# 국제표준 utf-8 VS. 국내 (준)표준 euc-kr
# utf-8은 리눅스 주력, 윈도우는 euc-kr 주력에서 utf-8로 선회.

# python은 타 언어 대비 파일 입출력이 매우 간편하다.

file_path = os.path.join(script_dir, "sample.txt")
f = open(file_path, "r", encoding="utf-8")

# 1) 읽어 온 파일 전체의 문자열화

data = f.read()
print(data, type(data))

# 2) 파일을 한 줄 씩 문자열로

data = f.readline()
print(data, type(data))

data = f.readline()
print(data, type(data))

data = f.readline()
print(data, type(data))

# 3) 한꺼번에 읽고 줄바꿈 기준으로 여러 리스트로 나누기

data = f.readlines()
print(data, type(data))

f.close()