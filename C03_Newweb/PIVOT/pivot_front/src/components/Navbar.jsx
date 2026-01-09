import React, { useContext } from 'react';
import { UserContext } from '../context/UserContext';

const Navbar = ({ activeTab, setActiveTab }) => {
  const { userInfo, setUserInfo } = useContext(UserContext);

  const handleLogout = () => {
    setUserInfo({ name: '', role: '', description: '' });
    setActiveTab('Dashboard');
  };

  // Build menus: always show Dashboard/Forum. Show Settings only when logged in,
  // and display the user's name as the menu label that navigates to the Settings tab.
  const menus = ['Dashboard', 'Forum'];
  const loggedIn = Boolean(userInfo?.name);
  if (loggedIn) menus.push(userInfo.name);

  return (
    <nav className="flex items-center justify-between p-6 bg-slate-900 text-white">
      <h1 className="text-2xl font-bold tracking-tighter">PIVOT</h1>
      <ul className="flex gap-8 items-center">
        {menus.map((label) => {
          const targetTab = loggedIn && label === userInfo.name ? 'Settings' : label;
          return (
            <li
              key={label}
              className={`cursor-pointer hover:text-blue-400 transition ${activeTab === targetTab ? 'text-blue-500 font-semibold' : ''}`}
              onClick={() => setActiveTab(targetTab)}
            >
              {label}
            </li>
          );
        })}

        {!loggedIn ? (
          // Not logged in: show Login/Register
          <>
            <li
              className={`cursor-pointer hover:text-blue-400 transition ${activeTab === 'Login' ? 'text-blue-500 font-semibold' : ''}`}
              onClick={() => setActiveTab('Login')}
            >
              Login
            </li>
            <li
              className={`cursor-pointer hover:text-blue-400 transition ${activeTab === 'Register' ? 'text-blue-500 font-semibold' : ''}`}
              onClick={() => setActiveTab('Register')}
            >
              Register
            </li>
          </>
        ) : (
          // Logged in: show Logout
          <>
            <li
              className="cursor-pointer hover:text-blue-400 transition"
              onClick={handleLogout}
            >
              Logout
            </li>
          </>
        )}
      </ul>
    </nav>
  );
};

export default Navbar;