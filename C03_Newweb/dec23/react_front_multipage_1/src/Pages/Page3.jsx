import axios from "axios";
import React from "react";
import { Link } from "react-router-dom";

const Page3 = () => {
    const showProduct = () => {
        axios
            .get(
                `http://localhost:9999/product.get?token=${sessionStorage.getItem(
                    "productInfo"
                )}`
            )
            .then((res) => {
                alert(res.data.name + ":" + res.data.price);
            });
    };

    return (
        <>
            <h1> 페이지 3 </h1>

            <button onClick={showProduct}> 등록 데이터 확인 </button>

            <a href="/p4.go"> 페이지 4로 이동하기(a 태그 사용) </a>
            <br />
            <Link to="/p4.go"> 페이지 4로 이동하기(Link to 사용) </Link>
        </>
    );
};

export default Page3;
