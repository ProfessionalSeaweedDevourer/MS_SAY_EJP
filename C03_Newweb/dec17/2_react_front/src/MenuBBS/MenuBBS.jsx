import React, { useState, useEffect } from "react";
import mmc from "./menu.module.css";
import axios from "axios";

const MenuBBS = () => {
    const [menuInput, setMenuInput] = useState({
        m_name: "",
        m_price: "",
        m_desc: "",
    });
    const [menuList, setMenuList] = useState([]);

    // 백엔드 서버 주소를 상수로 관리
    const API_URL = "http://195.168.9.135:8000/api/menus";

    // 1. 데이터를 가져오는 함수 정의
    const fetchMenus = async () => {
        try {
            const response = await axios.get(API_URL);
            setMenuList(response.data); // 서버에서 받은 배열을 상태에 저장
        } catch (error) {
            console.error("데이터 로딩 실패:", error);
        }
    };

    // 2. 컴포넌트 마운트 시 최초 1회 실행
    useEffect(() => {
        fetchMenus();
    }, []);

    const changeMenu = (e) => {
        const { name, value } = e.target;
        // 가격(m_price)은 숫자 타입으로 변환하여 저장
        const finalValue = name === "m_price" ? Number(value) : value;
        setMenuInput({ ...menuInput, [name]: finalValue });
    };

    const regMenu = async () => {
        // 간단한 유효성 검사
        if (!menuInput.m_name || !menuInput.m_price) {
            alert("이름과 가격을 입력하세요.");
            return;
        }

        try {
            const response = await axios.post(API_URL, menuInput);
            if (response.status === 200 || response.status === 201) {
                alert("등록 성공!");
                fetchMenus(); // 등록 성공 후 목록 새로고침
                setMenuInput({ m_name: "", m_price: "", m_desc: "" }); // 입력창 초기화
            }
        } catch (error) {
            console.error("등록 중 오류 발생:", error);
            alert("등록에 실패했습니다.");
        }
    };

    // 삭제 요청 함수
    const deleteMenu = async (m_name) => {
        // 1. 사용자에게 확인 (삭제 방지 절차)
        if (!window.confirm(`'${m_name}' 메뉴를 삭제하시겠습니까?`)) return;

        try {
            // 2. 백엔드 DELETE 엔드포인트 호출
            const response = await axios.delete(
                `http://195.168.9.135:8000/api/menus/${m_name}`
            );

            if (response.status === 200) {
                alert("삭제 성공");
                fetchMenus(); // 3. 목록 새로고침
            }
        } catch (error) {
            console.error("삭제 오류:", error);
        }
    };

    return (
        <div className={mmc.container}>
            <h3>등록</h3>
            메뉴명:{" "}
            <input
                name="m_name"
                value={menuInput.m_name}
                onChange={changeMenu}
            />
            <br />
            가격:{" "}
            <input
                name="m_price"
                type="number"
                value={menuInput.m_price}
                onChange={changeMenu}
            />
            <br />
            정보:{" "}
            <input
                name="m_desc"
                value={menuInput.m_desc}
                onChange={changeMenu}
            />
            <br />
            <button onClick={regMenu}> 등록 </button>
            <hr />
            <h3>메뉴</h3>
            <table border="1" style={{ width: "100%", textAlign: "center" }}>
                <thead>
                    <tr>
                        <th>메뉴명</th>
                        <th>가격</th>
                        <th>설명</th>
                    </tr>
                </thead>
                <tbody>
                    {menuList.map((item, index) => (
                        <tr key={index}>
                            <td>{item.m_name}</td>
                            <td>{Number(item.m_price).toLocaleString()}원</td>
                            <td>{item.m_desc}</td>
                            <td>
                                {/* 각 행마다 버튼을 생성하고 클릭 시 m_name 전달 */}
                                <button onClick={() => deleteMenu(item.m_name)}>
                                    삭제
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default MenuBBS;
