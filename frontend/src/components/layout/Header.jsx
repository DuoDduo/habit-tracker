/**
 * HabitOS Global Header
 * Features: Mobile-responsive navigation, user identity, and glassmorphism.
 * Author: Blessing Oluwapelumi James
 */

import React, { useState } from 'react';
import { Target, Activity, LayoutDashboard, Settings, Menu, X, BarChart2, User, Bell } from 'lucide-react';

export const Header = ({ user, activeView, onViewChange, onLogout }) => {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  // Mock global progress (this would usually come from a Context/State)
  const dailyProgress = 65; 

  const getInitials = (name) => {
    if (!name) return '??';
    const parts = name.split(' ');
    if (parts.length >= 2) return `${parts[0][0]}${parts[1][0]}`.toUpperCase();
    return name.substring(0, 2).toUpperCase();
  };

  return (
    <header className="sticky top-0 z-50 w-full bg-white/70 backdrop-blur-xl border-b border-gray-100/80">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between py-3.5">
          
          {/* 1. Brand Section */}
          <div className="flex items-center gap-3 sm:gap-4">
            <div className="relative group cursor-pointer">
              {/* Progress Ring Overlay */}
              <svg className="absolute -inset-1.5 w-[calc(100%+12px)] h-[calc(100%+12px)] -rotate-90 pointer-events-none">
                <circle
                  cx="50%" cy="50%" r="20"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2.5"
                  className="text-gray-100"
                />
                <circle
                  cx="50%" cy="50%" r="20"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2.5"
                  strokeDasharray={125.6}
                  strokeDashoffset={125.6 - (125.6 * dailyProgress) / 100}
                  className="text-blue-600 transition-all duration-1000 ease-out"
                />
              </svg>
              
              <div className="relative bg-blue-600 p-2 rounded-xl shadow-lg shadow-blue-200 group-hover:scale-105 transition-transform">
                <Target className="text-white" size={20} />
              </div>
            </div>
            
            <div className="flex flex-col">
              <h1 className="text-lg font-black tracking-tighter text-gray-900 flex items-center gap-1.5 leading-none">
                HabitOS
                <span className="text-[9px] font-bold bg-blue-50 text-blue-600 px-1.5 py-0.5 rounded-full uppercase tracking-widest border border-blue-100">
                  v1.2
                </span>
              </h1>
              <div className="hidden sm:flex items-center gap-1.5 text-[10px] text-gray-400 font-bold uppercase tracking-widest mt-1">
                <Activity size={10} className="text-blue-500" />
                <span>Achievement Engine</span>
              </div>
            </div>
          </div>

          {/* 2. Desktop Nav (Center) */}
          <nav className="hidden md:flex items-center bg-gray-100/50 p-1 rounded-xl border border-gray-200/50">
            <NavItem 
              icon={<LayoutDashboard size={16} />} 
              label="Dashboard" 
              active={activeView === 'dashboard'} 
              onClick={() => onViewChange('dashboard')}
            />
            <NavItem 
              icon={<BarChart2 size={16} />} 
              label="Analytics" 
              active={activeView === 'analytics'}
              onClick={() => onViewChange('analytics')}
            />
          </nav>
          
          {/* 3. Identity & Tools (Right) */}
          <div className="flex items-center gap-2 sm:gap-4">
            <button 
              onClick={onLogout}
              className="hidden sm:flex items-center gap-2 px-3 py-1.5 text-[10px] font-black uppercase tracking-widest text-slate-400 hover:text-red-500 hover:bg-red-50 rounded-lg transition-all border border-transparent hover:border-red-100"
            >
              Sign Out
            </button>
            
            <div className="h-8 w-px bg-gray-100 hidden sm:block mx-1" />

            <div className="flex items-center gap-3 pl-1 group cursor-pointer">
              <div className="hidden lg:flex flex-col text-right">
                <span className="text-xs font-black text-gray-900 leading-none truncate max-w-[120px]">
                  {user?.name || 'Guest User'}
                </span>
                <span className="text-[9px] font-bold text-slate-400 uppercase mt-1">
                  Achievement Lead
                </span>
              </div>
              <div className="h-9 w-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 p-0.5 shadow-md shadow-blue-100 transition-transform group-hover:scale-105">
                <div className="w-full h-full rounded-[10px] bg-white flex items-center justify-center overflow-hidden font-black text-[10px] text-blue-600">
                   {getInitials(user?.name)}
                </div>
              </div>
            </div>

            {/* Mobile Menu Toggle */}
            <button 
              className="md:hidden p-2 text-gray-600 hover:bg-gray-100 rounded-xl transition-colors"
              onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
            >
              {isMobileMenuOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
          </div>
        </div>
      </div>

      {/* 4. Mobile Navigation Drawer */}
      {isMobileMenuOpen && (
        <div className="md:hidden absolute top-full left-0 w-full bg-white border-b border-gray-100 animate-in slide-in-from-top-2 duration-200">
          <nav className="flex flex-col p-4 gap-2">
            <MobileNavItem 
              icon={<LayoutDashboard size={20} />} 
              label="Dashboard" 
              active={activeView === 'dashboard'} 
              onClick={() => {
                onViewChange('dashboard');
                setIsMobileMenuOpen(false);
              }}
            />
            <MobileNavItem 
              icon={<BarChart2 size={20} />} 
              label="Analytics" 
              active={activeView === 'analytics'}
              onClick={() => {
                onViewChange('analytics');
                setIsMobileMenuOpen(false);
              }}
            />
            <MobileNavItem icon={<Settings size={20} />} label="Account Settings" />
            <div className="mt-4 pt-4 border-t border-gray-50 flex flex-col gap-3">
               <p className="text-[10px] font-mono text-gray-400 uppercase px-3">
                 Session ID: {user?.matric || 'GUEST_USER'}
               </p>
               <button 
                 onClick={onLogout}
                 className="flex items-center gap-3 w-full px-4 py-3 rounded-xl text-sm font-bold text-red-600 hover:bg-red-50 transition-colors"
               >
                 <X size={20} />
                 Sign Out
               </button>
            </div>
          </nav>
        </div>
      )}
    </header>
  );
};

// Helper components for clean code
const NavItem = ({ icon, label, active = false, onClick }) => (
  <button 
    onClick={onClick}
    className={`
    flex items-center gap-2 px-4 py-2 text-sm font-bold rounded-lg transition-all
    ${active ? 'bg-white text-blue-600 shadow-sm' : 'text-gray-500 hover:text-gray-900'}
  `}>
    {icon}
    {label}
  </button>
);

const MobileNavItem = ({ icon, label, active = false, onClick }) => (
  <button 
    onClick={onClick}
    className={`
    flex items-center gap-3 w-full px-4 py-3 rounded-xl text-sm font-bold transition-colors
    ${active ? 'bg-blue-50 text-blue-600' : 'text-gray-600 hover:bg-gray-50'}
  `}>
    {icon}
    {label}
  </button>
);