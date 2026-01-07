import React from 'react'
import { useSelector, useDispatch } from 'react-redux';
import { changeTxt } from '../textSlice';

function Redux3() {
  // 스토어에서 txt 상태 추출
  const currentTxt = useSelector((state) => state.text.txt);
  const dispatch = useDispatch();

  const handleChange = (e) => {
    // 입력값을 payload로 전달하여 상태 변경 요청
    dispatch(changeTxt(e.target.value));
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>화면 텍스트: {currentTxt}</h2>
      <input 
        type="text" 
        value={currentTxt} 
        onChange={handleChange} 
        placeholder="내용을 입력하세요"
      />
    </div>
  );
}

export default Redux3;