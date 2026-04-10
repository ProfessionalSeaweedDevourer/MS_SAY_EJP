/* eslint-disable react-hooks/set-state-in-effect */
import axios from "axios";
import { useEffect, useRef, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import {
   isEmpty,
   isNotType,
   lessThan,
   notContains,
   notEqual,
} from "../../../../kwon/kwonValidCheckerReact";
import { loginCheck } from "../../../msAISAMain";
import { useNavigate } from "react-router-dom";
import { setSignUpPage } from "../../../../slice/memberSlice";

const MemberInfo = () => {
   const d = useDispatch();
   const loginMember = useSelector((s) => s.ms.loginMember);
   const [member, setMember] = useState({
      id: "",
      pw: "",
      pwChk: "",
      name: "",
      addr1: "",
      addr2: "",
      addr3: "",
      psa: "",
   });
   const memberFD = new FormData();
   memberFD.append("member", sessionStorage.getItem("loginMember"));
   memberFD.append("pw", member.pw);
   memberFD.append("name", member.name);
   memberFD.append("addr1", member.addr1);
   memberFD.append("addr2", member.addr2);
   memberFD.append("addr3", member.addr3);
   memberFD.append("psa", member.psa);
   const memberInput = useRef({});
   const navi = useNavigate();
   const [psaURL, setPsaURL] = useState();

   const bye = () => {
      if (prompt("진짜 탈퇴하려면 탈퇴 입력") === "탈퇴") {
         axios
            .get(
               `http://localhost:9999/member.bye?member=${sessionStorage.getItem(
                  "loginMember"
               )}`
            )
            .then((res) => {
               alert(res.data.result);
               sessionStorage.removeItem("loginMember");
               loginCheck();
            });
      }
   };
   const changeMember = (e) => {
      if (e.target.name === "psa") {
         setMember({ ...member, psa: e.target.files[0] });
         if (e.target.files[0] !== undefined) {
            const reader = new FileReader();
            reader.readAsDataURL(e.target.files[0]);
            reader.onloadend = () => {
               setPsaURL(reader.result);
            };
         } else {
            setMember({ ...member, psa: "" });
         }
      } else {
         setMember({ ...member, [e.target.name]: e.target.value });
      }
   };
   const showAddressSearchPopup = () => {
      new window.daum.Postcode({
         oncomplete: function (data) {
            setMember({
               ...member,
               addr1: data.zonecode,
               addr2: data.roadAddress,
            });
         },
      }).open();
   };
   const updateMember = () => {
      if (isValid()) {
         if (member.psa === "") {
            axios
               .post(
                  "http://localhost:9999/member.info.update.no.psa",
                  memberFD,
                  {
                     headers: {
                        "Content-Type": "multipart/form-data",
                     },
                     withCredentials: "true",
                  }
               )
               .then((res) => {
                  alert(res.data.result);
                  if (res.data.result === "수정 성공") {
                     sessionStorage.setItem("loginMember", res.data.member);
                  }
                  loginCheck();
               });
         } else {
            axios
               .post("http://localhost:9999/member.info.update", memberFD, {
                  headers: {
                     "Content-Type": "multipart/form-data",
                  },
                  withCredentials: "true",
               })
               .then((res) => {
                  alert(res.data.result);
                  if (res.data.result === "수정 성공") {
                     sessionStorage.setItem("loginMember", res.data.member);
                  }
                  loginCheck();
               });
         }
      }
   };
   const isValid = () => {
      if (
         isEmpty(member.pw) ||
         notEqual(member.pw, member.pwChk) ||
         lessThan(member.pw, 4) ||
         notContains(member.pw, "1234567890")
      ) {
         alert("pw?");
         setMember({ ...member, pw: "", pwChk: "" });
         memberInput.current.pw.focus();
         return false;
      }
      if (isEmpty(member.name)) {
         alert("이름?");
         setMember({ ...member, name: "" });
         memberInput.current.name.focus();
         return false;
      }
      if (isEmpty(member.addr1) || isEmpty(member.addr3)) {
         alert("주소?");
         setMember({ ...member, addr1: "", addr2: "", addr3: "" });
         memberInput.current.addr3.focus();
         return false;
      }
      if (isEmpty(member.psa)) {
         return true;
      }
      if (
         isNotType(member.psa, "png") &&
         isNotType(member.psa, "gif") &&
         isNotType(member.psa, "jpg") &&
         isNotType(member.psa, "bmp")
      ) {
         alert("프사?");
         setMember({ ...member, psa: "" });
         memberInput.current.psa.value = "";
         return false;
      }
      return true;
   };
   useEffect(() => {
      if (loginMember.id === undefined) {
         navi("/");
      } else {
         setMember({
            ...loginMember,
            addr1: loginMember.address.split("!")[2],
            addr2: loginMember.address.split("!")[0],
            addr3: loginMember.address.split("!")[1],
            psa: "",
         });
         setPsaURL(
            `http://localhost:9999/member.info.psa.get?file=${loginMember.psa}`
         );
      }

      return () => {};
   }, []);

   return (
      <table id="signUpFormTbl">
         <tr>
            <td align="center">{member.id}</td>
         </tr>
         <tr>
            <td align="center">
               <input
                  maxLength="10"
                  value={member.pw}
                  ref={(thisInput) => (memberInput.current.pw = thisInput)}
                  name="pw"
                  onChange={changeMember}
                  type="password"
                  placeholder="pw"
                  className="txtTypeInput"
                  autoComplete="off"
               />
            </td>
         </tr>
         <tr>
            <td align="center">
               <input
                  maxLength="10"
                  value={member.pwChk}
                  ref={(thisInput) => (memberInput.current.pwChk = thisInput)}
                  name="pwChk"
                  onChange={changeMember}
                  type="password"
                  placeholder="pw확인"
                  className="txtTypeInput"
                  autoComplete="off"
               />
            </td>
         </tr>
         <tr>
            <td align="center">
               <input
                  maxLength="10"
                  value={member.name}
                  ref={(thisInput) => (memberInput.current.name = thisInput)}
                  name="name"
                  onChange={changeMember}
                  placeholder="이름"
                  className="txtTypeInput"
                  autoComplete="off"
               />
            </td>
         </tr>
         <tr>
            <td align="center" style={{ paddingLeft: 3, paddingRight: 3 }}>
               <table>
                  <tr>
                     <td className="txtTypeInput">
                        생년월일 : {member.birthday}
                     </td>
                  </tr>
               </table>
            </td>
         </tr>
         <tr>
            <td align="center">
               <input
                  value={member.addr1}
                  ref={(thisInput) => (memberInput.current.addr1 = thisInput)}
                  onClick={showAddressSearchPopup}
                  placeholder="우편번호"
                  className="txtTypeInput"
                  autoComplete="off"
                  readOnly
               />
               <br />
               <input
                  value={member.addr2}
                  ref={(thisInput) => (memberInput.current.addr2 = thisInput)}
                  onClick={showAddressSearchPopup}
                  placeholder="주소"
                  className="txtTypeInput"
                  autoComplete="off"
                  readOnly
               />
               <br />
               <input
                  maxLength="50"
                  value={member.addr3}
                  ref={(thisInput) => (memberInput.current.addr3 = thisInput)}
                  name="addr3"
                  onChange={changeMember}
                  placeholder="상세주소"
                  className="txtTypeInput"
                  autoComplete="off"
               />
            </td>
         </tr>
         <tr>
            <td align="center" style={{ paddingLeft: 3, paddingRight: 3 }}>
               <table>
                  <tr>
                     <td className="txtTypeInput">
                        <img src={psaURL} />
                        <br />
                        <input
                           ref={(thisInput) =>
                              (memberInput.current.psa = thisInput)
                           }
                           name="psa"
                           onChange={changeMember}
                           type="file"
                        />
                     </td>
                  </tr>
               </table>
            </td>
         </tr>
         <tr>
            <td align="center">
               <button onClick={updateMember}>수정</button>
               <button onClick={bye}>탈퇴</button>
            </td>
         </tr>
      </table>
   );
};

export default MemberInfo;
