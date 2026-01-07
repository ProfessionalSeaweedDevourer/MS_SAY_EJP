import React, { useContext } from 'react';
import { UserContext } from '../context/UserContext';

const Dashboard = () => {
  const { userInfo } = useContext(UserContext);

  return (
    <div className="p-6 bg-slate-100 rounded-lg">
      <h2 className="text-2xl font-bold text-slate-900">{userInfo.name || '사용자'} 님의 프로필</h2>
      <p className="text-blue-600 font-medium">{userInfo.role || '직무를 입력해주세요'}</p>
      <hr className="my-4 border-slate-300" />
      <p className="text-slate-700">{userInfo.description || '소개글이 없습니다.'}</p>
    </div>
  );
};

// {} 내의 ||(OR) 역할: 앞에 지정한 입력값이 없을 경우 대체하여 들어가는 기본 데이터

export default Dashboard;