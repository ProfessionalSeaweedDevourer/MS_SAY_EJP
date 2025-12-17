import React, { useState } from "react";
import axios from "axios";

const AJAX02 = () => {
    const [searchTxt, setsearchTxt] = useState("");
    const [bookInfo, setbookInfo] = useState({
        title: "검",
        authors: "색",
        publisher: "하",
        price: "세",
        sale_price: "요",
    });

    const getBookData = () => {
        // 검색어가 비어있을 경우 요청 방지
        if (!searchTxt) return;

        axios
            .get(`https://dapi.kakao.com/v3/search/book?query=${searchTxt}`, {
                headers: {
                    Authorization: "KakaoAK 6a62f1fc9b9cbafd087a228121563d10",
                },
            })
            .then((res) => {
                const documents = res.data.documents;

                if (documents && documents.length > 0) {
                    // 핵심: documents 배열의 첫 번째 요소([0])에 접근
                    const firstBook = documents[0];
                    
                    setbookInfo({
                        title: firstBook.title,
                        authors: firstBook.authors.join(', '), // 저자가 배열이므로 문자열로 합침
                        publisher: firstBook.publisher,
                        price: firstBook.price,
                        sale_price: firstBook.sale_price,
                    });
                } else {
                    // 검색 결과가 없을 경우 초기화
                    alert("검색 결과가 없습니다.");
                    setbookInfo({
                        title: "결과 없음",
                        authors: "결과 없음",
                        publisher: "결과 없음",
                        price: "결과 없음",
                        sale_price: "결과 없음",
                    });
                }
            });
            
        setsearchTxt("");
    };

    return (
        <>
            <input
                value={searchTxt}
                onChange={(e) => {
                    setsearchTxt(e.target.value);
                }}
            />{" "}
            <button onClick={getBookData}> 검색 </button>
            <table border={1}>
                <thead>
                    <tr>
                        <th>제목</th>
                        <th>저자</th>
                        <th>출판사</th>
                        <th>정가</th>
                        <th>할인가</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td> {bookInfo.title} </td>
                        <td> {bookInfo.authors} </td>
                        <td> {bookInfo.publisher} </td>
                        <td> {bookInfo.price} </td>
                        <td> {bookInfo.sale_price} </td>
                    </tr>
                </tbody>
            </table>
        </>
    );
};

export default AJAX02;