import React, { useState } from "react";
import "./product.css";

const Listbuilder = () => {
    const [products, setProducts] = useState([]);
    const [newProduct, setNewProduct] = useState({
        name: "",
        price: "",
    });

    const handleChange = (e) => {
        setNewProduct({
            ...newProduct,
            [e.target.name]: e.target.value,
        });
    };
    // JS 배열 추가하기:
    // 배열[인덱스] : = 값;
    // 배열.push(값) : 값 추가
    // 배열.concat(값) : 값을 추가하고 전체 배열을 반환

    const handleRegistration = () => {
        if (!newProduct.name || !newProduct.price) {
            alert("제품명과 가격을 모두 입력해 주십시오.");
            return;
        }

        const productToAdd = {
            id: Date.now(),
            name: newProduct.name,
            price: newProduct.price,
        };

        setProducts([...products, productToAdd]);

        setNewProduct({
            name: "",
            price: "",
        });
    };

    return (
        <div id="prodArea">
            제품명:
            <input
                className="txtType"
                name="name"
                value={newProduct.name}
                onChange={handleChange}
            />
            <br />
            가격:
            <input
                className="txtType"
                type="number"
                name="price"
                value={newProduct.price}
                onChange={handleChange}
            />
            <br />
            <button onClick={handleRegistration}> 등록 </button>
            <hr />
            <table id="prodBBSTbl" border="1">
                <thead>
                    <tr>
                        <th> 제품명 </th>
                        <th> 가격 </th>
                    </tr>
                </thead>
                <tbody>
                    {products.map((product) => (
                        <tr className="dataTr" key={product.id}>
                            <td>{product.name}</td>
                            <td>{product.price}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Listbuilder;
