import React from "react";
import PropTypes from "prop-types";

const Props2 = (props2data) => {
    return(
        <>
            <h1> 제품명: {props2data.name}</h1>
            <h2> 가격: {props2data.price}</h2>
        </>
    );
};

Props2.propTypes = {
    name: PropTypes.string.isRequired,
    price: PropTypes.number.isRequired
}; // 입력값 자료형을 미리 지정, 추후 검증에 사용.

export default Props2;
