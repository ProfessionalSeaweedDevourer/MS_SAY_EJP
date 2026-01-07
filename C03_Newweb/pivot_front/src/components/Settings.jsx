import React, { useContext } from 'react';
import { UserContext } from '../context/UserContext';

const Settings = () => {
  const { userInfo, setUserInfo } = useContext(UserContext);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setUserInfo({ ...userInfo, [name]: value });
  };

  return (
    <div className="max-w-md mx-auto p-6 bg-white rounded shadow">
      <h2 className="text-xl font-bold mb-4 text-slate-800">기본 정보 입력</h2>
      <div className="space-y-4">
        <input 
          name="name" 
          placeholder="이름" 
          className="w-full p-2 border rounded" 
          value={userInfo.name} 
          onChange={handleChange} 
        />
        <input 
          name="role" 
          placeholder="직무 (예: Frontend Developer)" 
          className="w-full p-2 border rounded" 
          value={userInfo.role} 
          onChange={handleChange} 
        />
        <textarea 
          name="description" 
          placeholder="자기소개" 
          className="w-full p-2 border rounded" 
          value={userInfo.description} 
          onChange={handleChange} 
        />
      </div>
    </div>
  );
};

export default Settings;