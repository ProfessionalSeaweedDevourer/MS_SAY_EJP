// enf

// input의 required가 있는데, 다양한 type의 input이 있는데
//      1) form을 안써서 무의미
//      2) IE를 진짜 무시해도 될까
// -> 그냥 vanillaJS때 느낌으로 작업하자

export const isEmpty = (value) => value === "";

export const lessThan = (value, len) => value.length < len;

export const containsHangul = (value) => {
   const okSet =
      "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890@.-_";
   for (let i = 0; i < value.length; i++) {
      if (okSet.indexOf(value[i]) === -1) {
         return true;
      }
   }
   return false;
};

export const notEqual = (value1, value2) => value1 !== value2;

export const notContains = (value, set) => {
   for (let i = 0; i < set.length; i++) {
      if (value.indexOf(set[i]) !== -1) {
         return false;
      }
   }
   return true;
};

export const isNotNum = (value) => isNaN(value) || value.indexOf(" ") !== -1;

// 파일객체, 확장자
export const isNotType = (file, type) => {
   type = "." + type;
   return file.name.toLowerCase().indexOf(type) === -1;
};
