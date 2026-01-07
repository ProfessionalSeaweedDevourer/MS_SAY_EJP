import React from 'react'
import { useDispatch } from "react-redux"
import { sizeUp, sizeDown } from '../textSizeSlice'

const redux2Btn = () => {
    const d = useDispatch();

  return (
        <>
            <button
                onClick={() => d(sizeUp())}
            >
                20% 키우기
            </button>
            <button
                onClick={() => d(sizeDown())}
            >
                20% 줄이기
            </button>

            <h1 style={{ fontSize: `${textSize}px` }}>크기 조절용 텍스트</h1>
        </>
  )
}

export default redux2Btn