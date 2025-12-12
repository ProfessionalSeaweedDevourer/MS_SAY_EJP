import React, { useState } from "react";
import "./product.css";

const Listbuilder = () => {
    // 1. 상태(State) 정의
    // products: 테이블에 표시될 제품 목록 (배열)
    // newName: 새로운 제품명 입력 필드의 상태
    // newPrice: 새로운 가격 입력 필드의 상태

    const [products, setProducts] = useState([]);
    const [newName, setNewName] = useState("");
    const [newPrice, setNewPrice] = useState("");

    // 2. 입력 필드 값 변경 핸들러
    // React에서는 input 필드를 상태와 연결하여 '제어된 컴포넌트(Controlled Component)'로 만듭니다.
    const handleNameChange = (e) => {
        setNewName(e.target.value);
    };

    const handlePriceChange = (e) => {
        setNewPrice(e.target.value);
    };

    // 3. 등록 버튼 클릭 핸들러 (jQuery의 click 함수 역할)
    const handleRegistration = () => {
        // 입력 값 검증 (간단하게 비어있는지 확인)
        if (!newName || !newPrice) {
            alert("제품명과 가격을 모두 입력해 주십시오.");
            return;
        }

        // 4. 새 제품 객체 생성 및 상태 업데이트
        const newProduct = {
            id: Date.now(), // 고유한 key를 위해 현재 시간을 사용 (실제 앱에서는 서버 ID를 사용)
            name: newName,
            price: newPrice,
        };

        // products 배열에 새 제품을 추가하여 상태를 업데이트합니다.
        // setProducts 함수는 기존 상태를 기반으로 새 상태를 생성해야 합니다.
        setProducts([...products, newProduct]); // ...객체: 기존 내용 로드.

        // 5. 입력 필드 초기화 (jQuery의 val("") 역할)
        setNewName("");
        setNewPrice("");
    };

    return (
        <div id="prodArea">
            {/* 1. 입력 필드와 상태 연결 (value, onChange) */}
            제품명:
            <input className="txtType" value={newName} onChange={handleNameChange} />
            <br />
            가격:
            <input
                className="txtType"
                type="number" // 가격이므로 숫자 타입으로 설정
                value={newPrice}
                onChange={handlePriceChange}
            />
            <br />
            {/* 2. 등록 버튼에 이벤트 핸들러 연결 */}
            <button onClick={handleRegistration}> 등록 </button>
            <hr />
            <table id="prodBBSTbl">
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
