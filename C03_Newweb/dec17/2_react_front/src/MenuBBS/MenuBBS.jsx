import React, { useState } from "react";
import mmc from "./menu.module.css";
import "../common/Validcheck_react"

const MenuBBS = () => {
    const [menu, setMenu] = useState({ name: "", price: "", desc: "" });

    const changeMenu = (e) => {
        setMenu({ ...menu, [e.target.name]: e.target.value });
    };

    const regMenu = () => {
        alert(menu.name);
        alert(menu.price);
        alert(menu.desc);
    };

    const validCheck = () => {
        if (isEmpty(menu.name)) {
            alert("메뉴명 이상 감지");
            return false;
        }
        if (isEmpty(menu.price)) {
            alert("가격 이상 감지");
            return false;
        }
        return true;
    };

    return (
        <>
            메뉴명: <input value={menu.name} onChange={changeMenu}></input>{" "}
            <br />
            가격: <input /> <br />
            정보: <input /> <br />
            <button onClick={alert("")}> 등록 </button>
            <hr />
            <table border={1}></table>
        </>
    );
};

export default MenuBBS;
