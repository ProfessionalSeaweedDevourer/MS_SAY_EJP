import React, { useState } from "react";

// JS/jQuery: 파싱 > 반복문으로 테이블 형성 > 테이블에 데이터 넣기
// React: 파싱 > 반복문으로 테이블 형성해서 바로 넣기

const Rptstmt2 = () => {
    const [ar, setAr] = useState([1231, 84, 123, 93, 84]);

    const h4s = ar.map((a, i) => <h4>{a}</h4>);

    return <div>{h4s}</div>;
};

export default Rptstmt2;
