import React from "react";
import { useState } from "react";
import { useEffect } from "react";

const EJPWSClient3 = () => {
    const [msg, setMsg] = useState("");
    const [socket, setSocket] = useState(io("http://196.168.9.135:9999"))

    useEffect(() => { socket.on("test 2", (msg2) => { alert(msg2);}) return () => { socket.off("test2") } }, []);

    

    return (
        <>
            <input
                value={msg}
                onChange={(e) => {
                    setMsg(e.target.value);
                }}
                placeholder="메시지를 입력하세요"
            />
            <button onClick={() => { socket.emit("test", msg) }}> 전송 </button>
        </>
    );
};

export default EJPWSClient3;