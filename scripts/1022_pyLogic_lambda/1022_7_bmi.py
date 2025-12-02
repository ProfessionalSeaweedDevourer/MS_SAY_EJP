from time import sleep

def geth():
    height = float(input("키(m 단위): "))
    if height > 2.72 or height < 0.54:
        print("단위를 확인하세요.")
        geth()
    else:
        return height

def getw():    
    weight = float(input("체중(kg 단위): "))
    if weight > 675 or weight < 20:
        print("단위를 확인하세요.")
        getw()
    else:
        return weight

height = float(geth())
weight = float(getw())

bmi = weight / (height * height)
print(f"BMI: {bmi:.2f}")
print("-----------")

if bmi < 23:
    print("정상")
elif 23 <= bmi < 25:
    print("과체중")
elif 25 <= bmi < 30:
    print("1단계 비만")
elif 30 <= bmi < 35:
    print("2단계 비만")
elif 35 <= bmi:
    print("고도비만")

sleep(5)

# .py에 대한 실행 파일 만들기 -> .bat을 이용한 커맨드 적용
