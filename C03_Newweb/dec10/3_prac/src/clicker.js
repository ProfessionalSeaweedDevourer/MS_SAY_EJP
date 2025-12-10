import React, { useState } from 'react'

const Clicker = () => {
    const [cnt, setCnt] = useState(0);

    const changeCnt = () => {
        setCnt(cnt+1); // 호출될 때마다 cnt를 cnt+1로 바꾸는 메소드 setCnt 사용
    }

    return <button onClick={changeCnt}> {cnt} </button>; // 클릭 시마다 changeCnt 호출
}

export default Clicker