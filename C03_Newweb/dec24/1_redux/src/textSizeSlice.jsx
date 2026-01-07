// State: '상태'.
// Reducer: State를 '변화'시키는 함수.
// Action: 활동.
// Slice: Reducer + Action

// rxslice 입력하여 기본 구조 빠르게 생성
import { createSlice } from '@reduxjs/toolkit'

const initialState = {
    fontSize: 30,
}

const textSizeSlice = createSlice({
  name: "txtSl",
  initialState,
  reducers: {
    sizeUp: (currentState) => {
        currentState.fontSize *= 1.2;
    },
    sizeDown: (cs) => {
      cs.fontSize *= 0.8;
    }
  }
});

export const { sizeUp, sizeDown } = textSizeSlice.actions

export default textSizeSlice.reducer