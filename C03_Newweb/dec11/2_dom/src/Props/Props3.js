import React from "react";
import PropTypes from "prop-types";

const Props3 = (props3data) => {
    // 태그 속성 border 값에 {} 치는 것에 주의. HTML이 아니라 JSX이기 때문
    return (
        <>
            <table border={1}>
                <tr>
                    <td>
                        CPU: {props3data.cpu}
                    </td>
                </tr>
                <tr>
                    <td>
                        RAM: {props3data.ram} GB
                    </td>
                </tr>
                <tr>
                    <td>
                    Storage: {props3data.storagetype} {props3data.storagesize} TB
                    </td>
                </tr>
            </table>
        </>
    );
};

Props3.propTypes = {
    cpu: PropTypes.string.isRequired,
    ram: PropTypes.number.isRequired,
    storagetype: PropTypes.string.isRequired,
    storagesize: PropTypes.number.isRequired
}; // 자료형 지정: pt, ptr(필수 required) 시리즈 자동완성 지원
// 입력값 자료형을 미리 지정, 추후 검증에 사용.
// 그런데 씹어도 오류가 뜨거나 구동을 막지는 않고...
// 소스 가독성에 약간 기여하는 정도인데 그냥 안 쓰는 듯

export default Props3;
