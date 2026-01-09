import React, { createContext, useState } from 'react';

// 유저 데이터 컨텍스트 생성
export const UserContext = createContext();

export const UserProvider = ({ children }) => {
  const [userInfo, setUserInfo] = useState({
    id: '',
    name: '',
    role: '',
    description: '',
    // optional: data URL or image URL for profile picture
    profileImage: '',
    post_count: 0,
    comment_count: 0,
  });

  return (
    <UserContext.Provider value={{ userInfo, setUserInfo }}>
      {children}
    </UserContext.Provider>
  );
};