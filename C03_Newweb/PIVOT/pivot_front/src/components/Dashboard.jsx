import React, { useContext, useEffect, useState } from 'react';
import { UserContext } from '../context/UserContext';

const Dashboard = () => {
  const { userInfo, setUserInfo } = useContext(UserContext);
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    const fetchProfile = async () => {
      if (!userInfo?.id) return;

      try {
        const res = await fetch(`http://localhost:8000/users/${userInfo.id}`);
        if (res.ok) {
          const data = await res.json();
          setProfile(data);
          // sync context
          setUserInfo((prev) => ({ ...prev, ...data }));
        }
      } catch (e) {
        console.error('profile fetch failed', e);
      }
    };

    fetchProfile();
  }, [userInfo?.id, setUserInfo]);

  const current = profile || userInfo;

  return (
    <div className="p-6 bg-slate-100 rounded-lg">
      <h2 className="text-2xl font-bold text-slate-900">{current?.name || '사용자'} 님의 프로필</h2>
      <p className="text-blue-600 font-medium">{current?.role || '직무를 입력해주세요'}</p>
      <hr className="my-4 border-slate-300" />
      <p className="text-slate-700">{current?.description || '소개글이 없습니다.'}</p>
      <div className="mt-4 text-sm text-slate-600">
        <div>생년월일: {current?.birth_date || '-'}</div>
        <div>주소: {current?.address || '-'}</div>
      </div>
    </div>
  );
};

export default Dashboard;