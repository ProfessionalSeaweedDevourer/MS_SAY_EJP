import { createSlice } from '@reduxjs/toolkit'

const initialState = {
    txt: "테스트"
}

const textSlice = createSlice({
  name: "ts",
  initialState,
  reducers: {
    changeTxt: (cs, a) => {
      cs.txt = a.payload // a.payload: dispatcher 측에서 보내 준 값
    }
  }
});

export const {changeTxt} = textSlice.actions

export default textSlice.reducer