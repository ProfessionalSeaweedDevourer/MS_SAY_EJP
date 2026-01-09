import React, { useState } from 'react';
import { UserProvider } from './context/UserContext';
import Navbar from './components/Navbar';
import Dashboard from './components/Dashboard';
import Settings from './components/Settings';
import Register from './components/Register';
import Login from './components/Login';
import Forum from './components/Forum';

function App() {
  const [activeTab, setActiveTab] = useState('Dashboard');

  const renderContent = () => {
    switch (activeTab) {
      case 'Dashboard': return <Dashboard />;
      case 'Forum': return <Forum />;
      case 'Settings': return <Settings />;
      case 'Login': return <Login setActiveTab={setActiveTab} />;
      case 'Register': return <Register setActiveTab={setActiveTab} />;
      default: return <div className="p-8 text-center text-slate-500">준비 중인 기능입니다.</div>;
    }
  }; // switch default를 활용, 아직 실제 링크가 걸리지 않은 미완성 기능을 일괄 처리.

  return (
    <UserProvider>
      <div className="min-h-screen bg-slate-50">
        <Navbar activeTab={activeTab} setActiveTab={setActiveTab} />
        <main className="max-w-4xl mx-auto py-10">
          {renderContent()}
        </main>
      </div>
    </UserProvider>
  );
}

export default App;