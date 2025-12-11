import React from 'react'
import "./actualcss3.css"
// 이번에는 css를 이쪽으로 불러와서 써보자.
// 이 스크립트에서만 불러왔지만, 불러온 css는 app 전체에 적용됨에 주의.

const CustomCSS3 = () => {
    // id와 classname의 구분
  return (
    <>
        <div id="a">CustomCSS3</div>
        <div className="b"> TestText </div>
    </>
  )
}

export default CustomCSS3