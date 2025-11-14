# main.py

# 1. Controller 모듈 임포트
from controller.homeController import HomeController

# 2. 메인 함수 정의
def main():
    # 애플리케이션 초기화 및 구동 시작
    
    # 3. 컨트롤러 객체 생성
    app_controller = HomeController()
    
    # 4. 컨트롤러의 메인 메서드 실행 (프로그램의 주 실행 루프 시작)
    app_controller.run()

# 5. 프로그램의 시작점 지정
if __name__ == "__main__":
    main()