import React from 'react';
import { LayoutDashboard, Target, PieChart, Settings, LogOut, Plus, Terminal } from 'lucide-react';

export const Sidebar = ({ user, activeView, onViewChange, onLogout, onCreateClick }) => {
  const getInitials = (name) => {
    if (!name) return '??';
    const parts = name.split(' ');
    if (parts.length >= 2) return `${parts[0][0]}${parts[1][0]}`.toUpperCase();
    return name.substring(0, 2).toUpperCase();
  };

  return (
    <aside className="hidden lg:flex flex-col w-64 bg-white text-slate-500 h-screen sticky top-0 border-r border-gray-100 shrink-0 shadow-sm shadow-blue-500/5">
      {/* Brand Header */}
      <div className="p-6">
        <div className="flex items-center gap-3">
          <div className="bg-blue-600 p-2 rounded-xl shadow-lg shadow-blue-600/20">
            <Target className="text-white" size={20} />
          </div>
          <span className="text-xl font-black text-slate-900 tracking-tighter">HabitOS</span>
        </div>
      </div>

      {/* Main Navigation */}
      <nav className="flex-1 px-4 py-4 space-y-1.5">
        <SideLink 
          icon={<LayoutDashboard size={18} />} 
          label="Dashboard" 
          active={activeView === 'dashboard'} 
          onClick={() => onViewChange('dashboard')}
        />
        <SideLink 
          icon={<PieChart size={18} />} 
          label="Analytics" 
          active={activeView === 'analytics'}
          onClick={() => onViewChange('analytics')}
        />
        <SideLink icon={<Settings size={18} />} label="Preferences" />
        <div className="pt-4 pb-2 px-4 text-[10px] font-bold text-slate-400 uppercase tracking-[0.2em]">
          Resources
        </div>
        <SideLink icon={<Terminal size={18} />} label="Activity Logs" />
      </nav>

      {/* Primary Action */}
      <div className="p-4">
        <button 
          onClick={onCreateClick}
          className="w-full flex items-center justify-center gap-2 py-3.5 bg-blue-600 hover:bg-blue-700 text-white rounded-2xl font-bold transition-all shadow-xl shadow-blue-900/20 active:scale-95"
        >
          <Plus size={18} strokeWidth={3} />
          Create New Habit
        </button>
      </div>

      {/* User Session Control */}
      <div className="p-4 border-t border-gray-100 bg-gray-50/50">
        <div className="flex items-center gap-3 p-3 bg-white rounded-2xl border border-gray-100 shadow-sm shadow-blue-500/5 group hover:border-blue-200 transition-all">
          <div className="w-10 h-10 rounded-xl bg-blue-600 flex items-center justify-center text-white font-black text-sm shadow-lg shadow-blue-600/20">
            {getInitials(user?.name)}
          </div>
          <div className="flex-1 min-w-0">
            <p className="text-xs font-black text-slate-900 truncate tracking-tight">{user?.name || 'Local User'}</p>
            <p className="text-[10px] text-slate-400 font-bold uppercase truncate tracking-widest">{user?.matricNo || 'Workspace Lead'}</p>
          </div>
          <button 
            onClick={onLogout}
            title="Sign Out"
            className="ml-auto text-slate-400 hover:text-red-500 p-2 rounded-xl hover:bg-red-50 transition-all"
          >
            <LogOut size={16} />
          </button>
        </div>
      </div>
    </aside>
  );
};

const SideLink = ({ icon, label, active = false, onClick }) => (
  <button 
    onClick={onClick}
    className={`
    w-full flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-bold transition-all duration-200
    ${active 
      ? 'bg-blue-50 text-blue-600 border border-blue-100 shadow-sm shadow-blue-600/10' 
      : 'hover:bg-gray-50 hover:text-blue-600 border border-transparent'}
  `}>
    {icon}
    {label}
  </button>
);