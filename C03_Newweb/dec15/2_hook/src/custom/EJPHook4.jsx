import React from "react";

const EJPHook4 = () => {
    return (
        <canvas
            style={{ border: "2px solid black" }}
            width={300}
            height={300}
            onClick={(e) => {
                alert("!!!");
            }}
        />
    );
};

export default EJPHook4;
