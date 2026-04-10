import { useDispatch } from "react-redux";
import a from "./img/article.png";
import f from "./img/folder.png";
import i from "./img/image.png";
import w from "./img/windows.png";
import LoginSystem from "./loginSystem/loginSystem";
import { hide, summon } from "../../../slice/loginSystemSummonSlice";
import { useNavigate } from "react-router-dom";

const Menu = () => {
   const d = useDispatch();
   const navi = useNavigate();

   const summonLoginSystem = () => {
      d(summon());
   };
   const goSNS = () => {
      d(hide());
      navi("/sns.go");
   };
   return (
      <>
         <table id="siteMenuArea">
            <tr>
               <td>
                  <img src={w} onClick={summonLoginSystem} />
                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  <img src={a} onClick={goSNS} />
                  <img src={f} />
                  <img src={i} />
               </td>
            </tr>
         </table>
         <LoginSystem />
      </>
   );
};

export default Menu;
