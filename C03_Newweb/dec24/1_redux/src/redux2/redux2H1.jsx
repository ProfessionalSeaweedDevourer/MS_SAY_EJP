import React from 'react'
import { useSelector } from 'react-redux'


// subscriber: state를 사용할 대상
const redux2H1 = () => {
    const h1CSS = useSelector((st) => st.tss)

  return (
    <h1 style={h1CSS}> 크기 조절용 텍스트 </h1>
  )
}

export default redux2H1