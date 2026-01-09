import React, { useContext } from 'react';
import { UserContext } from '../context/UserContext';

const Settings = () => {
  const { userInfo, setUserInfo } = useContext(UserContext);

  const [preview, setPreview] = React.useState(userInfo.profileImage || '');
  const fileRef = React.useRef();

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

        <div className="flex items-center gap-3">
          <div className="w-16 h-16">
            {preview ? (
              <img src={preview} alt="profile" className="rounded-full w-16 h-16 object-cover" />
            ) : (
              <div className="rounded-full bg-slate-200 w-16 h-16 flex items-center justify-center text-slate-600">{userInfo.name ? userInfo.name.charAt(0).toUpperCase() : '?'}</div>
            )}
          </div>
          <div>
            <input
              ref={fileRef}
              type="file"
              accept="image/*"
              onChange={(e) => {
                const f = e.target.files?.[0];
                if (!f) return;
                setPreview(URL.createObjectURL(f));
              }}
            />
          </div>
        </div>

        <div className="flex gap-2">
          <button
            onClick={async () => {
              if (!userInfo.id) {
                alert('로그인 후에 설정을 저장할 수 있습니다.');
                return;
              }

              try {
                // update textual fields first
                const res = await fetch(`http://localhost:8000/users/${userInfo.id}`, {
                  method: 'PUT',
                  headers: { 'Content-Type': 'application/json' },
                  credentials: 'include',
                  body: JSON.stringify({
                    name: userInfo.name,
                    role: userInfo.role,
                    description: userInfo.description,
                  }),
                });

                if (!res.ok) {
                  const err = await res.json();
                  alert(err.detail || '설정 저장에 실패했습니다.');
                  return;
                }

                const updated = await res.json();
                // if a file was selected, upload it
                const file = fileRef.current?.files?.[0];
                if (file) {
                  const fd = new FormData();
                  fd.append('file', file);
                  const up = await fetch(`http://localhost:8000/users/${userInfo.id}/profile-image`, {
                    method: 'POST',
                    credentials: 'include',
                    body: fd,
                  });

                  if (!up.ok) {
                    const err = await up.json();
                    alert(err.detail || '이미지 업로드에 실패했습니다.');
                    return;
                  }
                  // set profileImage to backend-served URL (cache-bust)
                  setUserInfo((prev) => ({ ...prev, ...updated, profileImage: `http://localhost:8000/users/${userInfo.id}/profile-image?ts=${Date.now()}` }));
                  alert('설정 및 이미지가 저장되었습니다.');
                } else {
                  setUserInfo((prev) => ({ ...prev, ...updated }));
                  alert('설정이 저장되었습니다.');
                }
              } catch (e) {
                console.error(e);
                alert('서버와 통신할 수 없습니다.');
              }
            }}
            className="bg-blue-600 text-white px-4 py-2 rounded"
          >
            저장
          </button>
        </div>
      </div>
    </div>
  );
};

export default Settings;