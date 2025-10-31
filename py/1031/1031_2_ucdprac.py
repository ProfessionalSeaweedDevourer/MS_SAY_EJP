import os

class Saveinfo:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def fileupdate(self):
        # 현재 스크립트 파일과 같은 디렉토리에 파일을 저장하기 위한 경로 설정
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "product_info.txt")

        # 저장할 데이터 문자열 (이름, 가격, 중량을 쉼표로 구분하고 줄바꿈 추가)
        data_line = f"{self.name}, {self.price}, {self.weight}\n"

        # 'a' (append) 모드로 파일을 열어 데이터 추가 저장
        # with 구문을 사용하여 파일이 자동으로 닫히도록 처리
        try:
            with open(file_path, "a", encoding="utf-8") as f:
                f.write(data_line)
            print(f"-> {self.name} 정보가 파일에 저장되었습니다.")
        except IOError as e:
            print(f"파일 저장 중 오류가 발생했습니다: {e}")

# =========================================================
# 메인 실행 블록
# =========================================================
if __name__ == "__main__":
    print("제품 정보를 입력하세요. 이름을 'STOP'으로 입력하면 종료됩니다.")
    
    # while 루프를 사용하여 사용자 입력을 반복적으로 받음
    while True:
        try:
            # 1. 이름 입력 및 종료 조건 확인
            name = input("이름: ").strip()
            if name.upper() == "STOP":
                print("입력 종료. 스크립트를 마칩니다.")
                break
            
            # 2. 가격 및 중량 입력
            price = input("가격: ").strip()
            weight = input("중량: ").strip()

            # 3. Saveinfo 객체 생성
            userinfo = Saveinfo(name, price, weight)
            
            # 4. 파일에 저장
            userinfo.fileupdate()

        except Exception as e:
            print(f"입력 처리 중 예상치 못한 오류가 발생했습니다: {e}")
            break