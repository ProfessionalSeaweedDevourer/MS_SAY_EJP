/* eslint-disable react-refresh/only-export-components */
/* eslint-disable react-hooks/globals */
import axios from "axios";
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { setLoginMember } from "../slice/memberSlice";
import Content from "./layout/content/content";
import "./layout/content/member/member.css";
import "./layout/layout.css";
import "./layout/menu/loginSystem/login.css";
import "./layout/content/sns/sns.css";
import Menu from "./layout/menu/menu";
import Title from "./layout/title/title";
import Weather from "./layout/weather/weather";
import { useNavigate } from "react-router-dom";

let d = null;
let navi = null;
let signUpPage = null;

export const loginCheck = () => {
   axios
      .get(
         `http://localhost:9999/member.info.get?member=${sessionStorage.getItem(
            "loginMember"
         )}`
      )
      .then((res) => {
         d(setLoginMember(res.data.member));
         if (!signUpPage && res.data.member === undefined) {
            // 로그인 풀렸으면
            navi("/");
         } else {
            axios
               .get(
                  `http://localhost:9999/sign.in.exp.refresh?member=${sessionStorage.getItem(
                     "loginMember"
                  )}`
               )
               .then((res2) => {
                  sessionStorage.setItem("loginMember", res2.data.member);
               });
         }
      });
};

const MSAISAMain = () => {
   d = useDispatch();
   navi = useNavigate();
   signUpPage = useSelector((s) => s.ms.signUpPage);

   useEffect(() => {
      document.addEventListener("click", loginCheck);

      return () => {
         document.removeEventListener("click", loginCheck);
      };
   }, []);

   return (
      <>
         <Title />
         <Content />
         <Menu />
         <Weather />
      </>
   );
};

export default MSAISAMain;
