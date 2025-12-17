// React 대응 입력값 유효성 검사 JS 라이브러리

// 함수 만들기 기본 단축어: nfn
// '외부에서 쓸 함수' 만들기: enf =
// => export 붙어서 외부에서 쓸 수 있게 됨

// ========================================================================
// [1] 입력값이 비어 있을 경우
export const isEmpty = (value) => {
    return value === "";
};

// ========================================================================
// [2] 입력값이 요구되는 글자 수보다 짧을 경우
export const lessThan = (value, len) => value.legnth < len;

// ========================================================================
// [3] 한글 포함 감지

export const detectHangul = (value) => {
    const allowedset =
        "qwertyiopsdafghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890.-_";
    for (let i = 0; i < value.length; i++) {
        if (allowedset.indexOf(value[i]) == -1) {
            return true;
        }
    }
    return false;
};

// ========================================================================
// [4] 두 입력값이 서로 다를 경우

export const notEqual = (value1, value2) => value1 !== value2;

// ========================================================================
// [5] 특정 값이 들어 있지 않을 경우

export const nonExsistant = (value, set) => {
    for (let i = 0; i < set.length; i++) {
        if (value.indexOf(set[i]) != -1) {
            return false;
        }
    }
    return true;
};

// ========================================================================
// [6] 숫자가 아닐 경우

export const isNotNum = (value) => isNaN(value) || value.indexOf(" ") != -1;

// ========================================================================
// [7] 지정한 유형의 파일이 아닐 경우

export const wrongFileType = (file, type) => {
    type = "." + type;
    return file.name.toLowerCase().indexOf(type) == -1;
};
