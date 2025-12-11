import React, { useState } from "react"; // rafce 잊지 말 것. useState 쓸 때 {}로 임포트

const Input_ = () => {
    // React 표준에 따라 함수의 형태를 띄긴 하지만 이는 Class로 봐야 함
    // 클래스명은 대문자 스타트가 국룰

    const [txt, setTxt] = useState("Input setTxt Text"); // useStateSnippet으로 빠른 템플릿 생성

    return (
        <>
            <h1> {txt} </h1>
            <input
                value={txt}
                onChange={(ee) => {
                    // input 값이 바뀌는 이벤트 'ee'에 따라,
                    setTxt(ee.target.value); // setTxt에 의해 ee의 target value대로 txt 값을 변경.
                }}
            />

            <button
                onClick={() => {
                    alert(txt);
                }}
            >
                {" "}
                출력하기{" "}
            </button>
        </>
    );
};

export default Input_;
