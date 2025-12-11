import React, { useState } from 'react';

const CSSmod1 = () => {
    const [txt1, setTxt1] = useState('150'); 
    const [txt2, setTxt2] = useState('100'); 
    
    // 최종 CSS width 속성값을 계산하는 함수
    const cellWidthStyle1 = txt1 + 'px';
    const cellWidthStyle2 = txt2 + 'px';

    return (
        <>
            <table border={1}>
                <tr>
                    <td style={{ width: cellWidthStyle1 }}>
                        <input
                            type="number"
                            value={txt1} 
                            onChange={(e) => {
                                setTxt1(e.target.value); 
                            }}
                        />
                    </td>
                </tr>   
                <tr>
                    <td style={{ width: cellWidthStyle2 }}>
                        <input
                            type="number"
                            value={txt2} 
                            onChange={(e) => {
                                setTxt2(e.target.value); 
                            }}
                        />
                    </td>
                </tr>
            </table>
        </>
    );
};

export default CSSmod1;