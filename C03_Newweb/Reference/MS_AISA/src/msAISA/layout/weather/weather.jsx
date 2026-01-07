import axios from "axios";
import { useEffect, useState } from "react";

const Weather = () => {
   const [weather, setWeather] = useState({ i: "", d: "", t: "", h: "" });
   const [weatherCSS, setWeatherCSS] = useState({ top: 0, left: 0 });
   const getWeather = () => {
      axios
         .get(
            "https://api.openweathermap.org/data/2.5/weather?q=seoul&appid=***REMOVED_OWM_KEY***&units=metric&lang=kr"
         )
         .then((ress) => {
            setWeather({
               i: ress.data.weather[0].icon,
               d: ress.data.weather[0].description,
               t: ress.data.main.temp,
               h: ress.data.main.humidity,
            });
            window._aqiFeed({
               display:
                  "<span style='%style;font-size:10pt;padding:3px;'>공기 :%aqiv(%impact)</span>",
               container: "city-aqi-container",
               city: "seoul",
               lang: "kr",
            });
         });
   };

   const moveWeather = (e) => {
      setWeatherCSS({ top: e.clientY + 5, left: e.clientX + 5 });
   };
   const preventPopup = (e) => {
      e.preventDefault();
   };

   useEffect(() => {
      getWeather();
      document.addEventListener("contextmenu", preventPopup);
      document.addEventListener("mousemove", moveWeather);
      document.addEventListener("mouseup", getWeather);
      return () => {
         document.removeEventListener("contextmenu", preventPopup);
         document.removeEventListener("mousemove", moveWeather);
         document.removeEventListener("mouseup", getWeather);
      };
   }, []);

   return (
      <table id="weatherArea" style={weatherCSS}>
         <tr>
            <td align="center" rowSpan="3" style={{ width: 35 }}>
               <img
                  src={`https://openweathermap.org/img/wn/${weather.i}.png`}
               />
            </td>
            <td>{weather.d}</td>
         </tr>
         <tr>
            <td>
               {weather.t}℃({weather.h}%)
            </td>
         </tr>
         <tr>
            <td>
               <span id="city-aqi-container"></span>{" "}
            </td>
         </tr>
      </table>
   );
};

export default Weather;
