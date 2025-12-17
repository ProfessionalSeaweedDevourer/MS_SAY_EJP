import React from "react";
import { useState } from "react";
import axios from "axios";

// React에는 AJAX 관련 자체 메소드가 없다. 라이브러리 axios를 yarn add한다.

// Openweathermap API 활용:
// https://api.openweathermap.org/data/2.5/weather?q=seoul&appid=4051a3cb562e73934021bfeec41f6777&units=metric&lang=kr

const AJAX01 = () => {

    const [weather, setWeather] = useState({
        d: "",
        h: "0",
        t: "0",
    })

    const getWeather = () => {



        const url =
            "https://api.openweathermap.org/data/2.5/weather?q=seoul&appid=***REMOVED_OWM_KEY***&units=metric&lang=kr";

        // axios.get(주소) 하여 AJAX GET 요청한다.
        // axios.get(url).then(콜백함수)
        axios.get(url).then((res) => {

            // 응답 내용이 res.data로 들어간다.
            // alert(JSON.stringify(res.data)); // 일단 정상 출력 확인

        // -----------------------------------------------------------
        // 이제 전체 내용물에서 각 부분을 쪼개서 변수 할당하고 출력할 수 있게.
        // -----------------------------------------------------------
            setWeather({
                d: res.data.weather[0].description,
                t: res.data.main.temp,
                h: res.data.main.humidity,
            })

        });
        // alert("Test"); // 비동기식 처리가 기본이므로 이쪽이 get보다 먼저 수행된다.
    };

    return (
        <>
            <h1> 날씨: {weather.d} </h1>
            <h1> 기온: {weather.t} </h1>
            <h1> 습도: {weather.h} </h1>
            <button onClick={getWeather}> 정보 갱신 </button>
        </>
    );
};

export default AJAX01;
