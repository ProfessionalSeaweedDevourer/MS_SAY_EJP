import { useSelector } from "react-redux";
import LoginForm from "./loginForm";
import Logined from "./logined";

const LoginSystem = () => {
   const loginSystemCSS = useSelector((s) => s.lsss);
   const loginMember = useSelector((s) => s.ms.loginMember);

   let loginFormPage = null;
   if (loginMember === undefined) {
      loginFormPage = <LoginForm />;
   } else {
      loginFormPage = <Logined />;
   }

   return (
      <table id="loginSystem" style={loginSystemCSS}>
         <tr>
            <td valign="top" align="center">
               {loginFormPage}
            </td>
         </tr>
         <tr>
            <td valign="bottom" align="right" id="techArea">
               React
            </td>
         </tr>
      </table>
   );
};

export default LoginSystem;
