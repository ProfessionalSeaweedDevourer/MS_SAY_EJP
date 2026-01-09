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
          // normalize backend field to frontend context shape
          const normalized = {
            ...data,
            // backend already returns an absolute profile_image_url
            profileImage: data.profile_image_url || userInfo.profileImage || '',
            post_count: data.post_count || 0,
            comment_count: data.comment_count || 0,
          };
          setProfile(normalized);
          // sync context: map profile_image_url -> profileImage, and counts
          setUserInfo((prev) => ({ ...prev, ...normalized }));
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
      <div className="flex items-center gap-4">
        <div className="w-20 h-20">
          {current?.profileImage ? (
            <img src={current.profileImage} alt={current?.name} className="w-20 h-20 rounded-full object-cover" />
          ) : (
            <div className="w-20 h-20 rounded-full bg-slate-200 flex items-center justify-center text-2xl">{(current?.name||'?').charAt(0).toUpperCase()}</div>
          )}
        </div>
        <div>
          <h2 className="text-2xl font-bold text-slate-900">{current?.name || '사용자'}</h2>
          <p className="text-blue-600 font-medium">{current?.role || '직무를 입력해주세요'}</p>
        </div>
      </div>
      <hr className="my-4 border-slate-300" />
      <p className="text-slate-700">{current?.description || '소개글이 없습니다.'}</p>
      <div className="mt-4 text-sm text-slate-600">
        <div className="flex gap-4">
          <div>생년월일: {current?.birth_date || '-'}</div>
          <div>주소: {current?.address || '-'}</div>
        </div>
        <div className="mt-3 flex gap-4 text-sm">
          <div>작성글: {current?.post_count ?? current?.post_count === 0 ? current.post_count : '-'}</div>
          <div>댓글: {current?.comment_count ?? current?.comment_count === 0 ? current.comment_count : '-'}</div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;