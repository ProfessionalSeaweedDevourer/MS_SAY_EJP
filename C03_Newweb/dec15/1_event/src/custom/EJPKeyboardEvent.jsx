import React, { useState } from "react";

const EJPKeyboardEvent = () => {
    const [eventInfo, setEventInfo] = useState("");
    const [keyInfo, setKeyInfo] = useState("");

    return (
        <>
            <input
                onKeyDown={(e) => {
                    setEventInfo("키보드 눌림");
                    setKeyInfo(e.key);
                }}
                onKeyUp={(e) => {
                    setEventInfo("키보드 뗌");
                    setKeyInfo(e.key);
                }}
            />
            <h2> {eventInfo} </h2>
            <h2> {keyInfo} </h2>
        </>
    );
};

export default EJPKeyboardEvent;
