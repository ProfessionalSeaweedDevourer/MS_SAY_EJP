import React, { useState, useContext } from 'react';
import { UserContext } from '../context/UserContext';

const Register = () => {
  const { setUserInfo } = useContext(UserContext);
  
  // 로컬 입력 상태 관리
  const [formData, setFormData] = useState({
    id: '',
    password: '',
    birth_date: '',
    address: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // FastAPI 백엔드로 POST 요청 전송
      const response = await fetch('http://localhost:8000/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (response.ok) {
        // 성공 시 Context 업데이트 및 알림
        setUserInfo(formData);
        alert(`회원가입 성공: ${data.id}님 환영합니다.`);
      } else {
        // 백엔드에서 던진 HTTP 익셉션 처리 (중복 ID 등)
        alert(`가입 실패: ${data.detail || '알 수 없는 오류'}`);
      }
    } catch (error) {
      console.error('통신 에러:', error);
      alert('서버와 통신할 수 없습니다.');
    }
  };

  return (
    <div className="max-w-md mx-auto p-6 bg-white rounded shadow-lg border border-slate-200">
      <h2 className="text-xl font-bold mb-6 text-slate-800">회원가입 (Oracle DB 연동)</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-sm font-medium text-slate-700">아이디</label>
          <input 
            name="id" 
            placeholder="ID" 
            className="w-full p-2 border border-slate-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500" 
            value={formData.id} 
            onChange={handleChange} 
            required
          />
        </div>
        
        <div>
          <label className="block text-sm font-medium text-slate-700">비밀번호</label>
          <input 
            type="password"
            name="password" 
            placeholder="Password" 
            className="w-full p-2 border border-slate-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500" 
            value={formData.password} 
            onChange={handleChange} 
            required
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-slate-700">생년월일</label>
          <input 
            type="date"
            name="birth_date" 
            className="w-full p-2 border border-slate-300 rounded" 
            value={formData.birth_date} 
            onChange={handleChange} 
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-slate-700">주소</label>
          <input 
            name="address" 
            placeholder="주소 입력" 
            className="w-full p-2 border border-slate-300 rounded" 
            value={formData.address} 
            onChange={handleChange} 
          />
        </div>

        <button 
          type="submit"
          className="w-full bg-blue-600 text-white p-3 rounded font-bold hover:bg-blue-700 transition-colors mt-4"
        >
          DB에 저장하기
        </button>
      </form>
    </div>
  );
};

export default Register;