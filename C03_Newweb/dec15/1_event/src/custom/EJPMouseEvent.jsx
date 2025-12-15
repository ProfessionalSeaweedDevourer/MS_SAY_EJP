import React, { useState } from "react";

const EJPMouseEvent = () => {
    const divCss = { width: 200, height: 200, border: "5px solid #C44CC4" };
    const [cursorInfo, setcursorInfo] = useState("");
    const [brwsrcoordInfo, setbrwsrcoordInfo] = useState("");
    const [nativecoordInfo, setnativecoordInfo] = useState("");
    const [clickInfo, setclickInfo] = useState("");

    const changeclickInfo = (msg) => {
        setclickInfo(msg);
    };

    return (
        <>
            <div
                style={divCss}
                onMouseDown={(e) => {
                    changeclickInfo(e.button + "눌림");
                }}
                onMouseUp={(e) => {
                    changeclickInfo(e.button + "뗌");
                }}
                onMouseEnter={() => {
                    setcursorInfo("커서 입장 감지");
                }}
                onMouseMove={(e) => {
                    setbrwsrcoordInfo(e.clientX + "," + e.clientY);
                    setnativecoordInfo(
                        e.nativeEvent.offsetX + "," + e.nativeEvent.offsetY
                    );
                }} // '브라우저 기준'의 좌표
                onMouseLeave={() => {
                    setcursorInfo("커서 퇴장 감지");
                }}
            ></div>

            <h2> {cursorInfo} </h2>
            <h2> {clickInfo} </h2>
            <h2> 브라우저 기준 좌표: {brwsrcoordInfo} </h2>
            <h2> 객체 기준 좌표: {nativecoordInfo} </h2>
        </>
    );
};

export default EJPMouseEvent;
