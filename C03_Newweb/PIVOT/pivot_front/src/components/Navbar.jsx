import React, { useContext } from 'react';
import { UserContext } from '../context/UserContext';

const Navbar = ({ activeTab, setActiveTab }) => {
  const { userInfo, setUserInfo } = useContext(UserContext);

  const handleLogout = () => {
    setUserInfo({ name: '', role: '', description: '' });
    setActiveTab('Dashboard');
  };

  const defaultMenus = ['Dashboard', 'Inventory', 'Analysis', 'Settings'];

  return (
    <nav className="flex items-center justify-between p-6 bg-slate-900 text-white">
      <h1 className="text-2xl font-bold tracking-tighter">PIVOT</h1>
      <ul className="flex gap-8 items-center">
        {defaultMenus.map((menu) => (
          <li
            key={menu}
            className={`cursor-pointer hover:text-blue-400 transition ${activeTab === menu ? 'text-blue-500 font-semibold' : ''}`}
            onClick={() => setActiveTab(menu)}
          >
            {menu}
          </li>
        ))}

        {!userInfo?.name ? (
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
          // Logged in: show user name and Logout
          <>
            <li className="text-slate-300">{userInfo.name}</li>
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