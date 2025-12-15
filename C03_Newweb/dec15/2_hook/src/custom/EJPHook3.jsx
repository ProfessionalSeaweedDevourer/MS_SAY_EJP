import { useReducer } from "react";
import { useEffect } from "react";
import React, { useState } from "react";

const input2Reducer = (state, action) => {
    return {
        ...state,
        c: action.payload,
    };
};

const initialInput2State = {
    bgc: "lime", // 1번 input과 구별하기 위해 배경색 변경
    c: "red",
};

const EJPHook3 = () => {
    const [input1CSS, setInput1CSS] = useState({
        bgc: "yellow",
        c: "blue",
    });

    const [input2CSS, setInput2] = useReducer(
        input2Reducer, // Reducer 함수
        initialInput2State // 초기 상태 값
    );

    // useEffect(() => { alert("!!!") }, [])
    // // 두 번 알림 뜨는 것을 빼려면 main.jsx의 StrictMode 삭제
    // // yarn build 하고 서버에 올리면 StrictMode 있어도 두 번 나오지 않음:
    // // 이는 '렌더링 될 때마다' 발동하기 때문 => 초기 렌더링 시

    // useEffect(() => { alert("!!!") }, [input1CSS])
    // // 이렇게 하면 초기 렌더링 + input1CSS 값 변화시마다 발동

    useEffect(() => {
        alert("!!!");

        return () => {
            alert("???");
        }; // 여기에서의 return은 대상, 즉 EJPHook3가 '사라질 때' 발동. 일종의 소멸자.
    }, []);

    return (
        <>
            <input
                style={{ backgroundColor: input1CSS.bgc, color: input1CSS.c }}
                value={input1CSS.c}
                onChange={(e) => {
                    setInput1CSS({ ...input1CSS, c: e.target.value });
                }}
            />
            <br />
            <input
                style={{ backgroundColor: input2CSS.bgc, color: input2CSS.c }}
                value={input2CSS.c}
                onChange={(e) => {
                    // setInput2를 호출하여 Reducer 함수(input2Reducer)에 액션을 전달
                    setInput2({ payload: e.target.value });
                }}
            />
        </>
    );
};

export default EJPHook3;
