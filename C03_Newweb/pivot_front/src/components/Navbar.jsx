import React from 'react';

const Navbar = ({ activeTab, setActiveTab }) => {
  const menus = ['Dashboard', 'Inventory', 'Analysis', 'Settings', 'Register'];

  return (
    <nav className="flex items-center justify-between p-6 bg-slate-900 text-white">
      <h1 className="text-2xl font-bold tracking-tighter">PIVOT</h1>
      <ul className="flex gap-8">
        {menus.map((menu) => (
          <li 
            key={menu}
            className={`cursor-pointer hover:text-blue-400 transition ${activeTab === menu ? 'text-blue-500 font-semibold' : ''}`}
            onClick={() => setActiveTab(menu)}
          >
            {menu}
          </li>
        ))}
      </ul>
    </nav>
  );
};

export default Navbar;