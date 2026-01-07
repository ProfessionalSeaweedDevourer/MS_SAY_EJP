import React, { useState } from "react";

const Redux1 = () => {
    const [textSize, setTextSize] = useState(24);

    return (
        <>
            <button
                onClick={() => setTextSize((prev) => Math.round(prev * 1.2))}
            >
                20% 키우기
            </button>
            <button
                onClick={() => setTextSize((prev) => Math.round(prev * 0.8))}
            >
                20% 줄이기
            </button>

            <h1 style={{ fontSize: `${textSize}px` }}>크기 조절용 텍스트</h1>
        </>
    );
};

export default Redux1;
