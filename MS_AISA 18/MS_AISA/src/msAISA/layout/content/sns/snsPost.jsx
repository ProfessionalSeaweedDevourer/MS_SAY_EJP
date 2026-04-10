/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable react-hooks/set-state-in-effect */
import axios from "axios";
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { isEmpty } from "../../../../kwon/kwonValidCheckerReact";
import {
   setContent,
   summonSPUF,
} from "../../../../slice/snsPostUpdateFormSlice";
import c from "./img/close.png";
import e from "./img/editWhite.png";
import f from "./img/folder.png";
import { getPost } from "./sns";
import SNSPostReply from "./snsPostReply";

const SNSPost = (props) => {
   let btnTd = null;
   const d = useDispatch();
   const loginMember = useSelector((s) => s.ms.loginMember);
   const [postCSS, setPostCSS] = useState({ opacity: 1 });
   const [postReplys, setPostReplys] = useState([]);
   const postReplysDOM = postReplys.map((pr, i) => {
      return (
         <SNSPostReply
            no={pr.no}
            writer={pr.writer}
            date={pr.date}
            color={props.color}
         >
            {pr.txt}
         </SNSPostReply>
      );
   });
   const [replyTxt, setReplyTxt] = useState("");
   const [txtCSS, setTxtCSS] = useState({ opacity: 1 });
   const changeReply = (e) => {
      setReplyTxt(e.target.value);
   };
   const deletePost = () => {
      if (window.confirm("삭제?")) {
         axios
            .get(`http://localhost:9999/sns.post.delete?no=${props.no}`)
            .then((res) => {
               alert(res.data.result);
               getPost();
            });
      }
   };
   const hidePost = () => {
      setPostCSS({ opacity: 0 });
   };
   const hideTxt = () => {
      setTxtCSS({ opacity: 0 });
   };
   const isValid = () => {
      if (isEmpty(replyTxt)) {
         alert("?");
         return false;
      }
      return true;
   };
   const showPost = () => {
      setPostCSS({ opacity: 1 });
   };
   const showTxt = () => {
      setTxtCSS({ opacity: 1 });
   };
   const summonPostUpdateForm = () => {
      d(
         setContent({ no: props.no, writer: props.writer, txt: props.children })
      );
      d(summonSPUF());
   };
   const writePostReply = () => {
      if (isValid()) {
         axios
            .get(
               `http://localhost:9999/sns.post.reply.write?postno=${
                  props.no
               }&member=${sessionStorage.getItem(
                  "loginMember"
               )}&txt=${replyTxt}`
            )
            .then((res) => {
               alert(res.data.result);
               setReplyTxt("");
               getPost();
            });
      }
   };
   useEffect(() => {
      setPostReplys(props.replys);
   });

   if (loginMember === undefined) {
      btnTd = null;
   } else if (loginMember.id === props.writer) {
      btnTd = (
         <td align="right">
            <img
               src={e}
               onClick={summonPostUpdateForm}
               onMouseEnter={hideTxt}
               onMouseLeave={showTxt}
            />
            <img
               src={c}
               onClick={deletePost}
               onMouseEnter={hidePost}
               onMouseLeave={showPost}
            />
         </td>
      );
   }
   return (
      <table className="aSNSPost" style={postCSS}>
         <tr>
            <td
               className="titleTd"
               style={{ backgroundColor: "#" + props.color + "88" }}
            >
               <table className="titleTdTbl">
                  <tr>
                     <td>
                        <table>
                           <tr>
                              <td>
                                 <img src={f} className="folderImg" />
                              </td>
                              <td className="writerTd">{props.writer}</td>
                           </tr>
                        </table>
                     </td>
                     {btnTd}
                  </tr>
               </table>
            </td>
         </tr>
         <tr>
            <td className="contentTd">
               <table className="contentTdTbl">
                  <tr>
                     <td
                        rowSpan={3}
                        align="center"
                        className="imgTd"
                        style={{
                           borderRight: "#" + props.color + "88 solid 3px",
                        }}
                     >
                        <img
                           src={`http://localhost:9999/member.info.psa.get?file=${props.psa}`}
                        />
                     </td>
                     <td align="right" className="dateTd">
                        {props.date}
                     </td>
                  </tr>
                  <tr>
                     <td className="txtTd" style={txtCSS}>
                        {props.children}
                     </td>
                  </tr>
                  <tr>
                     <td className="replyTd">
                        {postReplysDOM}
                        <table className="aSNSPostReply">
                           <tr>
                              <td
                                 className="writer"
                                 style={{ color: "#" + props.color }}
                              >
                                 {loginMember.id}
                              </td>
                              <td className="txt">
                                 <input
                                    value={replyTxt}
                                    onChange={changeReply}
                                    placeholder="댓글"
                                    autoComplete="off"
                                 />
                              </td>
                              <td>
                                 <button onClick={writePostReply}>쓰기</button>
                              </td>
                           </tr>
                        </table>
                     </td>
                  </tr>
               </table>
            </td>
         </tr>
      </table>
   );
};

export default SNSPost;
