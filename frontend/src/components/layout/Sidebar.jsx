import React from 'react';
import { LayoutDashboard, ShieldCheck, PieChart, Settings, LogOut, Plus, Terminal } from 'lucide-react';

export const Sidebar = ({ onCreateClick }) => {
  return (
    <aside className="hidden lg:flex flex-col w-64 bg-[#0F172A] text-slate-400 h-screen sticky top-0 border-r border-slate-800 shrink-0">
      {/* Brand Header */}
      <div className="p-6">
        <div className="flex items-center gap-3">
          <div className="bg-blue-600 p-2 rounded-xl shadow-lg shadow-blue-500/20">
            <ShieldCheck className="text-white" size={20} />
          </div>
          <span className="text-xl font-black text-white tracking-tighter">HabitOS</span>
        </div>
      </div>

      {/* Main Navigation */}
      <nav className="flex-1 px-4 py-4 space-y-1.5">
        <SideLink icon={<LayoutDashboard size={18} />} label="Overview" active />
        <SideLink icon={<PieChart size={18} />} label="Performance" />
        <SideLink icon={<Settings size={18} />} label="Security" />
        <div className="pt-4 pb-2 px-4 text-[10px] font-bold text-slate-500 uppercase tracking-[0.2em]">
          System
        </div>
        <SideLink icon={<Terminal size={18} />} label="Logs" />
      </nav>

      {/* Primary Action */}
      <div className="p-4">
        <button 
          onClick={onCreateClick}
          className="w-full flex items-center justify-center gap-2 py-3.5 bg-blue-600 hover:bg-blue-700 text-white rounded-2xl font-bold transition-all shadow-xl shadow-blue-900/20 active:scale-95"
        >
          <Plus size={18} strokeWidth={3} />
          New Habit
        </button>
      </div>

      {/* User Status / Identity */}
      <div className="p-4 border-t border-slate-800/50 bg-slate-900/50">
        <div className="flex items-center gap-3 px-2 py-3">
          <div className="w-9 h-9 rounded-xl bg-slate-800 flex items-center justify-center text-xs font-bold text-blue-400 border border-slate-700">
            BO
          </div>
          <div className="min-w-0">
            <p className="text-xs font-bold text-white truncate">B.O. James</p>
            <p className="text-[9px] text-slate-500 font-mono uppercase tracking-widest mt-0.5">ID: 92134091</p>
          </div>
          <LogOut size={14} className="ml-auto text-slate-500 hover:text-red-400 cursor-pointer transition-colors" />
        </div>
      </div>
    </aside>
  );
};

const SideLink = ({ icon, label, active = false }) => (
  <button className={`
    w-full flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-bold transition-all duration-200
    ${active 
      ? 'bg-blue-600/10 text-blue-400 border border-blue-500/10 shadow-[inset_0_0_12px_rgba(59,130,246,0.05)]' 
      : 'hover:bg-slate-800/50 hover:text-white border border-transparent'}
  `}>
    {icon}
    {label}
  </button>
);