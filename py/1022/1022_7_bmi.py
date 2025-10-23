from time import sleep

bmi = float(input("BMI: "))
if bmi<23:
    print("정상")
elif 23<=bmi<25:
    print("과체중")
elif 25<=bmi<30:
    print("1단계 비만")
elif 30<=bmi<35:
    print("2단계 비만")
elif 35<=bmi:
    print("고도비만")

sleep(5)

# .py에 대한 실행 파일 만들기 -> .bat을 이용한 커맨드 적용
