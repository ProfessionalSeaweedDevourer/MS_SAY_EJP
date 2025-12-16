import React from "react";
import { useState } from "react";
import { useEffect } from "react";

const EJPWSClient2 = () => {
    const [msg, setMsg] = useState("");
    const [socket, setSocket] = useState(io("http://196.168.9.135:9999"))

    useEffect(() => { setSocket(io("http://195.168.9.135:9999")) })

    socket.on("test 2", (msg2) => { alert(msg2);}, [])

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

export default EJPWSClient2;
