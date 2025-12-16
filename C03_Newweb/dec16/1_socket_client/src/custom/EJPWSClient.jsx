import React, { useEffect } from "react";
import { useState } from "react";
import io from "socket.io-client";

const EJPWSClient = () => {
    const [socket, setSocket] = useState();
    useEffect(() => {
        setSocket(io("http://195.168.9.135:9999"))
    }, []);
    return (
        <>
            <button onClick={() => {
                socket.emit("test", "abcd")
            }}> 전송 </button>
        </>
    )
};

export default EJPWSClient;
