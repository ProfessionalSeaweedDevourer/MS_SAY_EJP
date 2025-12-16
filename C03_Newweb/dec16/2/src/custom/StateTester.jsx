import React from "react";
import { useEffect } from "react";
import { useState } from "react";

const StateTester = () => {
    const [no, setNo] = useState(0);

    useEffect(() => { setSocket(io("http://195.168.9.135:9999")) })

    return (
        <>
            <button
                onClick={() => {
                    setNo(no+1);
                    alert(no);
                }}
            >
                {" "}
                버튼{" "}
            </button>
        </>
    );
};

export default StateTester;
