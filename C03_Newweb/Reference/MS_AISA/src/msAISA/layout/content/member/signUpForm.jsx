import axios from "axios";
import { useEffect, useRef, useState } from "react";
import {
   containsHangul,
   isEmpty,
   isNotNum,
   isNotType,
   lessThan,
   notContains,
   notEqual,
} from "../../../../kwon/kwonValidCheckerReact";
import { useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import { setSignUpPage } from "../../../../slice/memberSlice";

const SignUpForm = () => {
   const d = useDispatch();
   const [member, setMember] = useState({
      id: "",
      pw: "",
      pwChk: "",
      name: "",
      jumin1: "",
      jumin2: "",
      addr1: "",
      addr2: "",
      addr3: "",
      psa: "",
   });
   const memberFD = new FormData();
   memberFD.append("id", member.id);
   memberFD.append("pw", member.pw);
   memberFD.append("name", member.name);
   memberFD.append("jumin1", member.jumin1);
   memberFD.append("jumin2", member.jumin2);
   memberFD.append("addr1", member.addr1);
   memberFD.append("addr2", member.addr2);
   memberFD.append("addr3", member.addr3);
   memberFD.append("psa", member.psa);
   const [membetIdInputCSS, setMembetIdInputCSS] = useState({ color: "white" });
   const memberInput = useRef({});
   const navi = useNavigate();

   const changeMember = (e) => {
      if (e.target.name === "psa") {
         setMember({ ...member, psa: e.target.files[0] });
      } else {
         if (e.target.name === "id") {
            axios
               .get(
                  `http://localhost:9999/member.id.check?id=${e.target.value}`
               )
               .then((res) => {
                  if (res.data.result === "중복") {
                     setMembetIdInputCSS({ color: "red" });
                  } else {
                     setMembetIdInputCSS({ color: "white" });
                  }
               });
         }
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
   const signUp = () => {
      if (isValid()) {
         axios
            .post("http://localhost:9999/sign.up", memberFD, {
               headers: {
                  "Content-Type": "multipart/form-data",
               },
               withCredentials: "true",
            })
            .then((res) => {
               memberInput.current.psa.value = "";
               setMember({
                  id: "",
                  pw: "",
                  pwChk: "",
                  name: "",
                  jumin1: "",
                  jumin2: "",
                  addr1: "",
                  addr2: "",
                  addr3: "",
                  psa: "",
               });
               if (res.data.result === "가입 성공") {
                  navi("/");
               }
            });
      }
   };
   const isValid = () => {
      if (
         isEmpty(member.id) ||
         containsHangul(member.id) ||
         membetIdInputCSS.color === "red"
      ) {
         alert("id?");
         setMember({ ...member, id: "" });
         memberInput.current.id.focus();
         return false;
      }
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
      if (
         isEmpty(member.jumin1) ||
         isEmpty(member.jumin2) ||
         lessThan(member.jumin1, 6) ||
         isNotNum(member.jumin1) ||
         isNotNum(member.jumin2)
      ) {
         alert("주민번호?");
         setMember({ ...member, jumin1: "", jumin2: "" });
         memberInput.current.jumin1.focus();
         return false;
      }
      if (isEmpty(member.addr1) || isEmpty(member.addr3)) {
         alert("주소?");
         setMember({ ...member, addr1: "", addr2: "", addr3: "" });
         memberInput.current.addr3.focus();
         return false;
      }
      if (
         isEmpty(member.psa) ||
         (isNotType(member.psa, "png") &&
            isNotType(member.psa, "gif") &&
            isNotType(member.psa, "jpg") &&
            isNotType(member.psa, "bmp"))
      ) {
         alert("프사?");
         setMember({ ...member, psa: "" });
         memberInput.current.psa.value = "";
         return false;
      }
      return true;
   };

   useEffect(() => {
      return () => {
         d(setSignUpPage(false));
      };
   }, []);

   return (
      <table id="signUpFormTbl">
         <tr>
            <td align="center">
               <input
                  style={membetIdInputCSS}
                  maxLength="10"
                  value={member.id}
                  ref={(thisInput) => (memberInput.current.id = thisInput)}
                  name="id"
                  onChange={changeMember}
                  placeholder="id"
                  className="txtTypeInput"
                  autoComplete="off"
                  autoFocus
               />
            </td>
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
                        주민번호 : &nbsp;
                        <input
                           maxLength="6"
                           value={member.jumin1}
                           ref={(thisInput) =>
                              (memberInput.current.jumin1 = thisInput)
                           }
                           name="jumin1"
                           onChange={changeMember}
                           className="jumin1Input"
                           placeholder="XXXXXX"
                           autoComplete="off"
                        />
                        &nbsp;-&nbsp;
                        <input
                           maxLength="1"
                           value={member.jumin2}
                           ref={(thisInput) =>
                              (memberInput.current.jumin2 = thisInput)
                           }
                           name="jumin2"
                           onChange={changeMember}
                           className="jumin2Input"
                           placeholder="X"
                           autoComplete="off"
                        />
                        XXXXXX
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
                        프사 : &nbsp;
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
               <button onClick={signUp}>가입</button>
            </td>
         </tr>
      </table>
   );
};

export default SignUpForm;
