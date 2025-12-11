import React, { useState } from "react";

const CSSmod3 = () => {
    const [tblCSS, setTblCSS] = useState({
        width: 200,
        height: 200
    });

    const changeCSS = (e) => {
        // alert(e); // 발생한 이벤트 정보
        // alert(e.target); // 이벤트가 발생한 객체
        // alert(e.target.name); // 이벤트가 발생한 객체의 이름 => 이것을 추적해서 해당 부분만 바꾸게 해 보자
        setTblCSS({ ...tblCSS, [e.target.name]: e.target.value*1});
    };

    return (
        <table border={1} style={tblCSS}>
            <tr>
                <td>
                    <input
                        name="width"
                        value={tblCSS.width}
                        onChange={changeCSS}
                    />
                </td>
            </tr>
            <tr>
                <td>
                    <input
                        name="height"
                        value={tblCSS.height}
                        onChange={changeCSS}
                    />
                </td>
            </tr>
        </table>
    );
};

export default CSSmod3;
