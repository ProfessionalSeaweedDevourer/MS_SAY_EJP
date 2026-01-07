import axios from "axios";
import { useState } from "react";
import { isEmpty, lessThan } from "../../../../kwon/kwonValidCheckerReact";
import w from "./img/edit.png";
import s from "./img/search.png";
import SNSPost from "./snsPost";

const SNS = () => {
   const [borderCSS, setBorderCSS] = useState({ border: "black solid 3px" });
   const [borderCSS2, setBorderCSS2] = useState({ backgroundColor: "black" });
   const [fontColorCSS, setFontColorCSS] = useState({
      color: "black",
      fontSize: "12pt",
   });
   const [post, setPost] = useState({ color: "000000", txt: "" });

   const changePost = (e) => {
      setPost({ ...post, [e.target.name]: e.target.value });
      if (e.target.name === "color") {
         setFontColorCSS({ ...fontColorCSS, color: "#" + e.target.value });
         setBorderCSS({ border: "#" + e.target.value + " solid 3px" });
         setBorderCSS2({ backgroundColor: "#" + e.target.value });
      }
   };
   const writePost = () => {
      if (isValid()) {
         axios
            .get(
               `http://localhost:9999/sns.post.write?color=${
                  post.color
               }&txt=${JSON.stringify(
                  post.txt
               )}&member=${sessionStorage.getItem("loginMember")}`
            )
            .then((res) => {
               alert(res.data.result);
               setPost({ color: "000000", txt: "" });
               setFontColorCSS({ ...fontColorCSS, color: "#000000" });
               setBorderCSS({ border: "#000000 solid 3px" });
               setBorderCSS2({ backgroundColor: "#000000" });
            });
      }
   };
   const isValid = () => {
      if (isEmpty(post.color) || lessThan(post.color, 6) || isEmpty(post.txt)) {
         alert("?");
         setPost({ color: "000000", txt: "" });
         return false;
      }
      return true;
   };
   return (
      <>
         <SNSPost />
         <SNSPost />
         <SNSPost />
         <SNSPost />
         <SNSPost />
         <SNSPost />
         <div id="snsPageL"></div>
         <div id="snsPageR"></div>
         <div id="snsBlankArea"></div>
         <table id="snsWriteArea">
            <tr>
               <td align="center">
                  <table id="snsWriteArea2" style={borderCSS}>
                     <tr>
                        <td align="center">
                           <input placeholder="검색" />
                        </td>
                        <td align="center">
                           <img src={s} />
                        </td>
                     </tr>
                     <tr>
                        <td colSpan={2} style={borderCSS2}></td>
                     </tr>
                     <tr>
                        <td align="center" style={fontColorCSS}>
                           &nbsp;&nbsp;#
                           <input
                              name="color"
                              style={fontColorCSS}
                              maxLength={6}
                              placeholder="RRGGBB"
                              value={post.color}
                              onChange={changePost}
                              autoComplete="off"
                           />
                        </td>
                        <td align="center" rowSpan={2}>
                           <img src={w} onClick={writePost} />
                        </td>
                     </tr>
                     <tr>
                        <td align="center">
                           <textarea
                              name="txt"
                              maxLength={200}
                              onChange={changePost}
                              value={post.txt}
                              placeholder="내용"
                              autoComplete="off"
                           />
                        </td>
                     </tr>
                  </table>
               </td>
            </tr>
         </table>
      </>
   );
};

export default SNS;
