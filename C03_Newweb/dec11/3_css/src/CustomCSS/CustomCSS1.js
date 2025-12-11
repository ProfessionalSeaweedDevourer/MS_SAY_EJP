import React from "react";

// css
const CustomCSS1 = () => {
    return (
        // React에서는 CSS도 JS 객체처럼 다룬다.
        // 속성명도 다 바뀌어 있다. (background-color => backgroundColor)
        <div style={{ color: "red", backgroundColor: "yellow", width: 300, height: "500px"}}>
            CustomCSS1
        </div>
        // {}가 등장했다는 것은, 단순 값이 아니라 JS 동작을 넣겠다는 것.
        // '정식 숫자', 즉 따옴표 없이 들어간 값 (300) 에는 px를 붙이지 않아도 픽셀 단위로 간주된다.
        // ""에 넣은 값일 경우에는 스스로 단위를 지정해 줘야 한다. (500px)
    );
};

export default CustomCSS1;
