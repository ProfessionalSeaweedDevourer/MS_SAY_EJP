import { useDispatch, useSelector } from "react-redux";
import { hideSPUF, setContent } from "../../../../slice/snsPostUpdateFormSlice";
import c from "./img/close.png";
import e from "./img/editWhite.png";
import axios from "axios";
import { getPost } from "./sns";
import { isEmpty } from "../../../../kwon/kwonValidCheckerReact";
const SNSPostUpdateForm = () => {
   const d = useDispatch();
   const spufCSS = useSelector((s) => s.spufs.css);
   const content = useSelector((s) => s.spufs.content);
   const hidePostUpdateForm = () => {
      d(hideSPUF());
   };
   const changeContent = (e) => {
      d(setContent({ ...content, txt: e.target.value }));
   };
   const updatePost = () => {
      if (isValid()) {
         axios
            .get(
               `http://localhost:9999/sns.post.update?no=${
                  content.no
               }&txt=${JSON.stringify(content.txt)}`
            )
            .then((res) => {
               alert(res.data.result);
               getPost();
               d(hideSPUF());
            });
      }
   };
   const isValid = () => {
      if (isEmpty(content.txt)) {
         alert("?");
         return false;
      }
      return true;
   };
   return (
      <table id="snsPostUpdateArea" style={spufCSS}>
         <tr>
            <td align="center">
               <table id="snsPostUpdateForm">
                  <tr>
                     <td className="id">{content.writer}</td>
                     <td align="right">
                        <img src={c} onClick={hidePostUpdateForm} />
                     </td>
                  </tr>
                  <tr>
                     <td>
                        <textarea
                           onChange={changeContent}
                           value={content.txt}
                        />
                     </td>
                     <td>
                        <img src={e} onClick={updatePost} />
                     </td>
                  </tr>
               </table>
            </td>
         </tr>
      </table>
   );
};

export default SNSPostUpdateForm;
