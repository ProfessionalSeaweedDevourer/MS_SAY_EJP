import React, { useCallback, useState } from "react";

const Rpt1 = () => {
    const [numbers, setNumbers] = useState([123, 65, 38, 100, 10, 34, 50]);

    // 오늘 다룰 개념: 필터링.
    //  > 배열 요소를 차례대로 탐색하면서, 각 데이터마다 콜백 함수 호출.
    //  > 배열명.filter((값) => {})
    numbers.filter((n) => {
        if (n % 2 === 0) {
            return true;
        } else {
            return false;
        }
    });

    // 한 줄로 구현하기: 
    let numbers2 = numbers.filter((n) => n%2 === 0)
    // * === : 값과 자료형 모두 일치 판정

    // const numbers3 = numbers2.sort(); // '글자'를 오름차순 정렬

    const numbers3 = numbers2.sort((n1, n2) => { 
        if (n1>n2) {
            return -1; // 앞의 값이 더 크면 -1: 내림차순 정렬
        } else {
            return 1;
        }
     })

    // numbers의 각 요소에 대해 콜백 발생, 연결한 행위 발생.
    // 연결 행위에 조건문을 넣으면, '조건에 해당하는 요소에 대해서만' 행위가 발생하게 할 수 있음.

    const marqnums = numbers3.map((a, i) => (
        <marquee behavior="alternate"> {a} </marquee>
    ));

    return <div>{marqnums}</div>;
};

export default Rpt1;
