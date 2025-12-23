import React from "react";
import { useState } from "react";

const productBBS = () => {
    const [product, setProduct] = useState({ name: "", price: "" });

    const changeProduct = (e) => {
        setProduct({ ...product, [e.target.name]: e.target.value });
    };

    const showProduct = () => {
        alert(product.name);
        alert(product.price);
        setProduct({ name: "", price: "" });
    };

    return (
        <div id="productRegArea">
            제품명:{" "}
            <input
                className="txtType"
                value={product.name}
                name="name"
                onChange={changeProduct}
            />
            <br />
            가격:{" "}
            <input
                className="txtType"
                value={product.price}
                name="price"
                onChange={changeProduct}
            />
            <br />
            <button onClick={showProduct}> 등록 </button>
        </div>
    );
};

export default productBBS;
