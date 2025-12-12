import React, {useState} from 'react'

const Rpt2 = () => {

    const [snacks, setSnacks] = useState([
        { name: "빼빼로", price: 2000, color: "brown" },
        { name: "새콤달콤", price: 500, color: "pink" },
        { name: "쌀로별", price: 3000, color: "yellow" },
        { name: "썬칩", price: 3500, color: "red" },
        { name: "도리토스", price: 3300, color: "orange" },
        { name: "프링글스", price: 3800, color: "green" },
        { name: "하리보", price: 2800, color: "gold" },
        { name: "구운감자", price: 2500, color: "black" },
    ]);

    // const filteredSnacks = snacks.filter((n) => n.price >= 1000)

    const filteredSnacks2 = snacks.sort((n1, n2) => {
        if(n1.name > n2.name) {
            return 1;
        } else {
            return -1;
        }
    }) // 제품명에 따른 오름차순 정렬 구현

    const snackTrs = filteredSnacks2.map((s, i) => {
        return (
            <tr style={{ color: s.color }}>
                <td>{s.name}</td>
                <td>{s.price}</td>
            </tr>
        );
    });

    return (
        <table border={1}>
            <tr>
                <td>제품명</td>
                <td>가격</td>
            </tr>
            {snackTrs}
        </table>
    );
}

export default Rpt2