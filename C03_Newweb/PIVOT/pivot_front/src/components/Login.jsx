import React, { useState, useContext } from 'react';
import { UserContext } from '../context/UserContext';

const Login = ({ setActiveTab }) => {
  const { setUserInfo } = useContext(UserContext);

  const [formData, setFormData] = useState({
    id: '',
    password: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('http://localhost:8000/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (response.ok) {
        // 백엔드가 사용자 정보를 반환하면 그것을 사용, 아니면 최소한 id를 저장
        setUserInfo(data || { name: formData.id, role: '', description: '' });
        alert(`로그인 성공: ${data?.name || formData.id}님 환영합니다.`);
        if (setActiveTab) setActiveTab('Dashboard');
      } else {
        alert(`로그인 실패: ${data.detail || '아이디/비밀번호를 확인하세요.'}`);
      }
    } catch (error) {
      console.error('통신 에러:', error);
      alert('서버와 통신할 수 없습니다.');
    }
  };

  return (
    <div className="max-w-md mx-auto p-6 bg-white rounded shadow-lg border border-slate-200">
      <h2 className="text-xl font-bold mb-6 text-slate-800">로그인</h2>
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

        <button
          type="submit"
          className="w-full bg-blue-600 text-white p-3 rounded font-bold hover:bg-blue-700 transition-colors mt-4"
        >
          로그인
        </button>
      </form>
    </div>
  );
};

export default Login;
