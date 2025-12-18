import React, { useState } from "react";
import axios from "axios";

const AJAX_01_GET = () => {
    const [xy, setXY] = useState({ x: "", y: "" });
    const [result, setResult] = useState({
        sum: "",
        sub: "",
        mult: "",
        div: "",
    });

    const changeXY = (e) => {
        setXY({ ...xy, [e.target.name]: e.target.value });
    };

    const calc = () => {
        axios
            .get(`http://192.168.9.135:8000/calc.do?x=${xy.x}&y=${xy.y}`)
            .then((res) => {
                setResult(res.data);
            });
    };

    return (
        <>
            x: <input value={xy.x} name="x" onChange={changeXY} />
            <br />
            y: <input value={xy.y} name="y" onChange={changeXY} />
            <br />
            <button onClick={calc}> 계산 </button>
            <hr />
            +: {result.sum} <br />
            -: {result.sub}
            <br />
            *: {result.mult} <br />
            /: {result.div} <br />
        </>
    );
};

export default AJAX_01_GET;
