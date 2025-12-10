import React from "react";

const MyBtns = () => {
    return (
        <>
            <button
                onClick={() => {
                    alert("누르기 1 성공");
                }} // 이런 식으로 함수를 넣는 것이 리액트 표준.
            >
                {" "}
                누르기 1{" "} 
            </button> 
        </>
    );
};

export default MyBtns;
// 길쭉해요
