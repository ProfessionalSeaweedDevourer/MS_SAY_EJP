import React from "react";

const CustomCSS2 = (customcss2data) => {
    const css2datadict = {
        color: customcss2data.c,
        backgroundColor: customcss2data.bgc,
        width: customcss2data.w,
        height: customcss2data.h,
        fontSize: customcss2data.fs,
    };

    return <div style={css2datadict}>CustomCSS2</div>;
};

export default CustomCSS2;
