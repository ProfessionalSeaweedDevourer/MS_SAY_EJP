import axios from "axios";
import { useSelector } from "react-redux";
import { getPost } from "./sns";

const SNSPostReply = (props) => {
   const loginMember = useSelector((s) => s.ms.loginMember);
   let btnArea = <td />;

   const deletePostReply = () => {
      axios
         .get(`http://localhost:9999/sns.post.reply.delete?no=${props.no}`)
         .then((res) => {
            alert(res.data.result);
            getPost();
         });
   };
   if (loginMember.id === props.writer) {
      btnArea = (
         <td>
            <button onClick={deletePostReply}>X</button>
         </td>
      );
   }
   return (
      <table className="aSNSPostReply">
         <tr>
            <td className="writer" style={{ color: "#" + props.color }}>
               {props.writer}
            </td>
            <td className="txt">{props.children}</td>
            <td className="date">{props.date}</td>
            {btnArea}
         </tr>
      </table>
   );
};

export default SNSPostReply;
