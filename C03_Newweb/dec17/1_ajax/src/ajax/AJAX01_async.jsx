import React from "react";
import axios from "axios";

// 01번의 동기 처리 예제

const AJAX01_async = () => {
    const getWeather = async () => {
        const url =
            "https://api.openweathermap.org/data/2.5/weather?q=seoul&appid=4051a3cb562e73934021bfeec41f6777&units=metric&lang=kr";
        // async 붙이고 요청 앞에 await 달아주기.
        await axios.get(url).then(() => {
            alert("Placeholder");
        });
        // alert("Test"); // 비동기식 처리가 기본이므로 이쪽이 get보다 먼저 수행된다.
    };

    return (
        <>
            <h1> 날씨: </h1>
            <h1> 기온: </h1>
            <h1> 습도: </h1>
            <button onClick={getWeather}> 정보 갱신 </button>
        </>
    );
};

export default AJAX01_async;
