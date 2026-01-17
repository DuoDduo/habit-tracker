import React from 'react';
import { Target, Activity, LayoutDashboard, Settings } from 'lucide-react';

export const Header = () => {
  return (
    <header className="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-gray-100">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between py-4">
          
          {/* Logo & Branding */}
          <div className="flex items-center gap-4">
            <div className="relative">
              <div className="bg-primary-600 p-2.5 rounded-xl shadow-lg shadow-primary-200">
                <Target className="text-white" size={24} />
              </div>
              {/* Decorative status ring */}
              <div className="absolute -top-1 -right-1 w-3 h-3 bg-green-500 border-2 border-white rounded-full" />
            </div>
            
            <div>
              <h1 className="text-xl font-extrabold tracking-tight text-gray-900 flex items-center gap-2">
                <span className="text-gradient">HabitOS</span>
                <span className="text-[10px] font-mono bg-gray-100 px-1.5 py-0.5 rounded text-gray-500 uppercase tracking-tighter">Beta</span>
              </h1>
              <div className="flex items-center gap-2 text-xs text-gray-500 font-medium">
                <Activity size={12} className="text-primary-500" />
                <span>Engineered for Consistency</span>
              </div>
            </div>
          </div>

          {/* Desktop Navigation - Clean & Minimal */}
          <nav className="hidden lg:flex items-center bg-gray-50 p-1 rounded-lg border border-gray-100">
            <button className="flex items-center gap-2 px-4 py-1.5 text-sm font-medium text-primary-700 bg-white rounded-md shadow-sm">
              <LayoutDashboard size={16} />
              Dashboard
            </button>
            <button className="flex items-center gap-2 px-4 py-1.5 text-sm font-medium text-gray-500 hover:text-gray-700 transition">
              Analytics
            </button>
          </nav>
          
          {/* Identity & Meta-data */}
          <div className="flex items-center gap-6">
            <div className="hidden sm:block text-right">
              <div className="flex flex-col">
                <span className="text-sm font-bold text-gray-900">B.O. James</span>
                <span className="text-[10px] font-mono text-gray-400 uppercase tracking-widest">ID: 92134091</span>
              </div>
            </div>
            
            <button className="p-2 text-gray-400 hover:text-primary-600 hover:bg-primary-50 rounded-full transition-colors">
              <Settings size={20} />
            </button>
          </div>

        </div>
      </div>
    </header>
  );
};