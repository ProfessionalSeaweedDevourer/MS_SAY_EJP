import React, {useReducer} from 'react'
// rafce 하여 기본 구조 자동완성.

// useReducer: 멤버 변수 + 그 값을 변화시키는 메소드 (setter)
// => + setter에 추가 기능 제공: 소스를 더 잘 정리

const flagGame = (curState, action) => { 
  return curState + " -> " + action.flag + " " + action.action;
 }

const EJPHook2 = () => {
  // anfn 하면 화살표 함수 자동완성.

    // useReducer s..하면 snippet으로 자동완성.
    // const [멤버변수, setter메소드] = useReducer(setter함수, 기본값)
    const [history, setHistory] = useReducer(flagGame, "시작")
    // => setHistory 호출 시 자동으로 flagGame이 실행됨. 

  return (
    <>
    
    <h1> {history} </h1>
    <button onClick={() => { setHistory({flag: "청기", action: "올려"}) }}> 청기 올려 </button>
    <button onClick={() => { setHistory({flag: "청기", action: "내려"}) }}> 청기 내려 </button>
    <button onClick={() => { setHistory({flag: "백기", action: "올려"}) }}> 백기 올려 </button>
    <button onClick={() => { setHistory({flag: "백기", action: "내려"}) }}> 백기 내려 </button>
    
    </>
  )
}

export default EJPHook2