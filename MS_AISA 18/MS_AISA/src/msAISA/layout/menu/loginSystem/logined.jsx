import { useSelector } from "react-redux";
import { loginCheck } from "../../../msAISAMain";
import { useNavigate } from "react-router-dom";

const Logined = () => {
   const loginMember = useSelector((s) => s.ms.loginMember);
   const navi = useNavigate();
   
   const goMemberInfo = () => {
      navi("/member.info.go");
   };
   const signOut = () => {
      sessionStorage.removeItem("loginMember");
      loginCheck();
   };
   return (
      <table id="loginForm">
         <tr>
            <td rowSpan="2" align="center" className="imgTd">
               <img
                  src={`http://localhost:9999/member.info.psa.get?file=${loginMember.psa}`}
               />
            </td>
            <td className="idTd">{loginMember.id}</td>
         </tr>
         <tr>
            <td align="right">
               <button onClick={goMemberInfo}>정보확인</button>
               <button onClick={signOut}>로그아웃</button>
            </td>
         </tr>
      </table>
   );
};

export default Logined;
