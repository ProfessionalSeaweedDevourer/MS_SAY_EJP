# 외부 파일로부터 패키지 가져오기

# 1번 형식
import animal.pet # import 패키지.모듈

d = animal.pet.dog("후추")
d.bark()
d.printInfo()

# 2번 형식
import animal.pet as ap
d = ap.dog("후추")
d.bark()
d.printInfo()

# 3번 형식: vscode 기본은 이 스타일. 다만 상황에 따라 1, 2번 형식도 쓸 줄 알아야 함.
from animal.pet import dog

# Windows에서 경로 설정을 통해, 프로젝트 전체를 일종의 패키지로 인식하게 할 수도 있음.
