import axios from "axios";
import { useState } from "react";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import { isEmpty } from "../../../../kwon/kwonValidCheckerReact";
import { hide } from "../../../../slice/loginSystemSummonSlice";
import { setSignUpPage } from "../../../../slice/memberSlice";
import { loginCheck } from "../../../msAISAMain";

const LoginForm = () => {
   const d = useDispatch();
   const [member, setMember] = useState({ id: "", pw: "" });
   const memberFD = new FormData();
   memberFD.append("id", member.id);
   memberFD.append("pw", member.pw);
   const navi = useNavigate();

   const changeMember = (e) => {
      setMember({ ...member, [e.target.name]: e.target.value });
   };
   const goSignUp = () => {
      d(hide());
      d(setSignUpPage(true));
      navi("/sign.up.go");
   };
   const signIn = () => {
      if (isValid()) {
         axios
            .post("http://localhost:9999/sign.in", memberFD, {
               withCredentials: "true",
            })
            .then((res) => {
               if (res.data.result === "로그인 성공") {
                  sessionStorage.setItem("loginMember", res.data.member);
                  loginCheck();
               } else {
                  alert(res.data.result);
               }
            });
      }
      setMember({ id: "", pw: "" });
   };
   const signInEnterKey = (e) => {
      if (e.key === "Enter") {
         signIn();
      }
   };
   const isValid = () => {
      if (isEmpty(member.id) || isEmpty(member.pw)) {
         alert("?");
         return false;
      }
      return true;
   };
   return (
      <table id="loginForm">
         <tr>
            <td align="center">
               <input
                  onKeyUp={signInEnterKey}
                  onChange={changeMember}
                  name="id"
                  value={member.id}
                  maxLength="10"
                  placeholder="id"
                  autoComplete="off"
                  />
            </td>
         </tr>
         <tr>
            <td align="center">
               <input
                  onKeyUp={signInEnterKey}
                  onChange={changeMember}
                  name="pw"
                  value={member.pw}
                  type="password"
                  maxLength="10"
                  placeholder="pw"
                  autoComplete="off"
               />
            </td>
         </tr>
         <tr>
            <td align="center">
               <button onClick={signIn}>로그인</button>
               <button onClick={goSignUp}>회원가입</button>
            </td>
         </tr>
      </table>
   );
};

export default LoginForm;
