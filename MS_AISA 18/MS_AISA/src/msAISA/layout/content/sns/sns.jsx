/* eslint-disable react-hooks/globals */
/* eslint-disable react-refresh/only-export-components */
import axios from "axios";
import { useEffect, useState } from "react";
import { isEmpty, lessThan } from "../../../../kwon/kwonValidCheckerReact";
import w from "./img/edit.png";
import s from "./img/search.png";
import SNSPost from "./snsPost";
import SNSPostUpdateForm from "./snsPostUpdateForm";

export let getPost;

const SNS = () => {
   const [borderCSS, setBorderCSS] = useState({ border: "black solid 3px" });
   const [borderCSS2, setBorderCSS2] = useState({ backgroundColor: "black" });
   const [fontColorCSS, setFontColorCSS] = useState({
      color: "black",
      fontSize: "12pt",
   });
   const [page, setPage] = useState(1);
   const [pageCount, setPageCount] = useState(1);
   const [post, setPost] = useState({ color: "000000", txt: "" });
   const [posts, setPosts] = useState([]);
   const postsDOM = posts.map((p, i) => {
      return (
         <SNSPost
            no={p.no}
            writer={p.writer}
            psa={p.psa}
            date={p.date}
            color={p.color}
            replys={p.replys}
         >
            {p.txt}
         </SNSPost>
      );
   });
   const [searchTxt, setSearchTxt] = useState("");

   const changePost = (e) => {
      setPost({ ...post, [e.target.name]: e.target.value });
      if (e.target.name === "color") {
         setFontColorCSS({ ...fontColorCSS, color: "#" + e.target.value });
         setBorderCSS({ border: "#" + e.target.value + " solid 3px" });
         setBorderCSS2({ backgroundColor: "#" + e.target.value });
      }
   };
   const changeSearchTxt = (e) => {
      setSearchTxt(e.target.value);
   };

   getPost = () => {
      axios
         .get(
            `http://localhost:9999/sns.post.get?page=${page}&search=${searchTxt}`
         )
         .then((res) => {
            setPosts(res.data.posts);
            setPageCount(res.data.pageCount);
         });
   };
   const goNextPage = () => {
      if (page < pageCount) {
         setPage(page + 1);
      }
   };
   const goPrevPage = () => {
      if (page > 1) {
         setPage(page - 1);
      }
   };
   const searchPost = () => {
      getPost();
      setSearchTxt("");
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
               getPost();
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
   useEffect(() => {
      getPost();

      return () => {};
   }, [page]);

   return (
      <>
         {postsDOM}
         <div id="snsPageL" onClick={goPrevPage}></div>
         <div id="snsPageR" onClick={goNextPage}></div>
         <div id="snsBlankArea"></div>
         <table id="snsWriteArea">
            <tr>
               <td align="center">
                  <table id="snsWriteArea2" style={borderCSS}>
                     <tr>
                        <td align="center">
                           <input
                              value={searchTxt}
                              onChange={changeSearchTxt}
                              onKeyUp={(e) => {
                                 if (e.key === "Enter") {
                                    searchPost();
                                 }
                              }}
                              placeholder="검색"
                           />
                        </td>
                        <td align="center">
                           <img src={s} onClick={searchPost} />
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
         <SNSPostUpdateForm />
      </>
   );
};

export default SNS;
