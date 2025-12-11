import React from "react";

const Props1 = (props1data) => {
    return (
        <>
            <h1> 이름: {props1data.name} </h1>
            <h2> 연령: {props1data.age}세 </h2>
            <hr />
        </>
    );
};

export default Props1;
