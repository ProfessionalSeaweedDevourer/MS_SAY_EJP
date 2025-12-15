import React, {useState} from 'react'

// React만의 새로운 개념: hook.
// class '역할'의 함수를 사용하는 것을 권장.
// 그런데 객체 - 클래스에서는 속성(멤버 변수), 행동(메소드), 생성자가 필요.
// => '함수'로 이를 구현하도록 돕는 요소가 hook.

// useState도 일종의 훅: 일종의 멤버 변수와 같은 것을 구현.
// 멤버 변수와 이를 제어하는 메소드를 생성하는 것.
// 가령 아래의 예시는 기능적으로 다음과 같음.
// class EJPHook1:
//      def __init__(self, cnt):
//          self.cnt = 0
//      def setCnt(cnt):
//          self.cnt = cnt

const EJPHook1 = () => {
    const [cnt, setCnt] = useState(0);
    // 그런데 그냥 cnt 값을 바꾸지 않고 꼭 setCnt를 거쳐야 하는 이유는?
    // '잘못된 값'이 삽입될 위험에 대비한 '캡슐화'.
    // setCnt를 거치지 않고는 cnt 값을 임의 변경할 수 없도록 설계.

    const changeCnt = () => {
        setCnt(cnt+1)
    }
  return (
    <>
        <h1> 버튼 클릭 횟수: {cnt} </h1>
        <button onClick={changeCnt}> 버튼 </button>
    </>
  )
}

export default EJPHook1