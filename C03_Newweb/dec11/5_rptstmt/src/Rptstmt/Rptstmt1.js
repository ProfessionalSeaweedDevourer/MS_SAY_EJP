import React from "react";

const Rptstmt1 = () => {
    const testarr = [123, 1123, 543, 129381, 312, 1];

    const rptTest1 = () => {
        for (let index = 0; index < testarr.length; index++) {
            const testarrcontent = testarr[index];
            // testarrcontent는 매 루프마다 '새로' 생성되고 '완전히' 지워진다.
            // 때문에 불변값의 const로 선언해도 실행에 문제가 되지 않는다.
            // * python에서는 그냥 동적으로 변수 값을 갈아끼운다.
            // 영 불편하면 반복문 시작 전에 let a; 선언하고 a=으로 불러오기.
            alert(testarrcontent);
        }
    };

    const rptTest2 = () => {
        testarr.map(() => {
            alert("!!!");
        });
    };

    return (
    <>
    <button onClick={rptTest1}> 테스트1 </button>
    
    </>
    );
};

export default Rptstmt1;
