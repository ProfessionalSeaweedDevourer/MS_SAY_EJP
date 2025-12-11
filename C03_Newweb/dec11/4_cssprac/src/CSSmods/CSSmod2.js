import React, {useState} from 'react'

const CSSmod2 = () => {
    const [tblCSS, setTblCSS] = useState({
        width: 200,
        height: 200,
    })

    const changeWidth = (e) => {
        setTblCSS({ ...tblCSS, width: e.target.value * 1}); // ES6 문법: 대상의 내부 데이터 특정 속성에 접근
    } // ...객체: 그 객체의 속성값을 그대로 가져오기.
    // 일단 그대로 가져오고, 그 중 바꿀값: 바꾼값 * 1(숫자로 자료형변환)

    const changeHeight = (e) => {
        setTblCSS({ ...tblCSS, height: e.target.value * 1});
    }

    return (
        <table border={1} style={tblCSS}>
            <tr>
                <td>
                    <input value={tblCSS.width} onChange={changeWidth} />
                </td>
            </tr>
            <tr>
                <td>
                    <input value={tblCSS.height} onChange={changeHeight}/>
                </td>
            </tr>
        </table>
    )
}

export default CSSmod2