// OOP 구현
// 객체(Component) 만들기: Class 필요
// > React는 클래스보다 함수형 component를 권장: rafce
// React Arrow Function Export Component 


import React from 'react'

// const MyH1 = () => {
//   return (
//     <div> 테스트 1 </div>
//   )
// }

// export default MyH1


// JSX(JavaScript XML): HTML이 아니라 HTML처럼 생긴 XML
// > 무조건 반환값이 있어야 함: 모든 태그 <>는 반드시 </>로 닫아야 함
// 풀세트를 만들어야 하는데 정작 태그 내용물은 필요 없다면: <시작태그 /> 로 단순화 가능

// 낙타체 선호
// 속성값 자리는 "값"으로, {JS문법}으로

const MyH2 = () => {
  return (
    <>
        <h2> 테스트 2 </h2>
        <h2> 테스트 3 </h2>
        <hr />
    </>
  )
}

export default MyH2