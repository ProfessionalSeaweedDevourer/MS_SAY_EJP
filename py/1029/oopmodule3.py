# 모듈 직접 실행 시 발동하는, 실질적인 main 루프 영역 만들기

if __name__ == "__main__":
    print("Test")

# Error VS. Warning: 문법이 안 맞아서 아예 안 됨(내 과실) / 지저분해서 실행은 되지만 피할 것
# Exception: 기본적으로는 잘 되다가도 예외적인 상황이 발생 -> 내 잘못은 아니더라도 내가 고쳐야 함
# Exception Handling: (발생할 수도 있고 아닐 수도 있는) 예외사항의 대응책 세워 두기.