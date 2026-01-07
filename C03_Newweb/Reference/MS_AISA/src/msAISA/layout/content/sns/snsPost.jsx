import { useState } from "react";
import c from "./img/close.png";
import e from "./img/editWhite.png";
import f from "./img/folder.png";
import s from "./img/search.png";
const SNSPost = () => {
   const [bgColor, setBgColor] = useState({ backgroundColor: "#ff000099" });
   return (
      <table className="aSNSPost">
         <tr>
            <td className="titleTd" style={bgColor}>
               <table className="titleTdTbl">
                  <tr>
                     <td>
                        <table>
                           <tr>
                              <td>
                                 <img src={f} className="folderImg" />
                              </td>
                              <td className="writerTd">hong</td>
                           </tr>
                        </table>
                     </td>
                     <td align="right">
                        <img src={e} />
                        <img src={c} />
                     </td>
                  </tr>
               </table>
            </td>
         </tr>
         <tr>
            <td className="contentTd">
               <table className="contentTdTbl">
                  <tr>
                     <td rowSpan={3} align="center" className="imgTd">
                        <img src={s} />
                     </td>
                     <td align="right" className="dateTd">
                        2026-01-06 14:55:00
                     </td>
                  </tr>
                  <tr>
                     <td className="txtTd">
                        ㅋㅋㅋㅋㅋㅋ
                        <br />
                        ㅋㅋㅋ
                        <br />ㅋ
                     </td>
                  </tr>
                  <tr>
                     <td className="replyTd">댓글자리</td>
                  </tr>
               </table>
            </td>
         </tr>
      </table>
   );
};

export default SNSPost;
