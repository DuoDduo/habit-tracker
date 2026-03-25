/**
 * Hero Section Component
 * Features: Terminal typing effect and system overview
 * Author: Blessing Oluwapelumi James
 */

import React, { useState, useEffect } from 'react';
import { ShieldCheck, Activity, Zap, ArrowRight, Sparkles } from 'lucide-react';

export const Hero = ({ userName, habitCount, onCreateClick }) => {
  const [displayText, setDisplayText] = useState('');
  const fullText = `Welcome back, ${userName}.`;
  
  useEffect(() => {
    let i = 0;
    const timer = setInterval(() => {
      setDisplayText(fullText.substring(0, i));
      i++;
      if (i > fullText.length) clearInterval(timer);
    }, 100);
    return () => clearInterval(timer);
  }, [userName]);

  return (
    <section className="relative overflow-hidden rounded-[2.5rem] bg-[#0F172A] text-white p-8 sm:p-14 mb-12 shadow-2xl shadow-blue-900/30 border border-white/5">
      {/* Dynamic Background Glows */}
      <div className="absolute top-0 right-0 -mr-24 -mt-24 w-96 h-96 bg-blue-600/20 rounded-full blur-[120px] animate-pulse" />
      <div className="absolute bottom-0 left-0 -ml-24 -mb-24 w-72 h-72 bg-indigo-500/10 rounded-full blur-[100px]" />

      <div className="relative z-10 flex flex-col lg:flex-row lg:items-center justify-between gap-12">
        <div className="max-w-2xl space-y-8">
          <div className="flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/10 border border-blue-500/20 w-fit">
            <ShieldCheck size={14} className="text-blue-400" />
            <span className="text-[10px] font-black uppercase tracking-[0.2em] text-blue-400">
              System Auth: Terminal_Active
            </span>
          </div>

          <div className="space-y-4">
            <h1 className="text-4xl sm:text-6xl font-black tracking-tight leading-[1.1] min-h-[1.2em]">
              {displayText}<span className="animate-pulse text-blue-500">_</span>
              <br />
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-indigo-300">
                Consistency Engine.
              </span>
            </h1>

            <p className="text-slate-400 text-lg leading-relaxed max-w-lg font-medium">
              HabitOS bridges <span className="text-white">Cybersecurity</span> principles with <span className="text-white">Behavioral Data Science</span>. Monitor your nodes, maintain your uptime, and secure your personal growth.
            </p>
          </div>

          <div className="flex flex-wrap gap-4">
            <button 
              onClick={onCreateClick}
              className="flex items-center gap-2 px-8 py-4 bg-blue-600 hover:bg-blue-700 rounded-2xl font-bold transition-all shadow-lg shadow-blue-600/40 group active:scale-95"
            >
              Initialize Node
              <ArrowRight size={18} className="group-hover:translate-x-1 transition-transform" />
            </button>
            <button className="flex items-center gap-2 px-8 py-4 bg-slate-800/50 hover:bg-slate-700 rounded-2xl font-bold transition-all border border-slate-700/50 backdrop-blur-sm">
              View Logs
            </button>
          </div>
        </div>

        {/* System Monitor Card */}
        <div className="lg:w-80 bg-white/5 backdrop-blur-xl border border-white/10 rounded-[2rem] p-8 space-y-8 shadow-inner">
           <div className="flex items-center justify-between">
              <span className="text-xs font-black text-slate-500 uppercase tracking-[0.2em]">Environment</span>
              <Activity size={18} className="text-blue-500 animate-pulse" />
           </div>
           
           <div className="space-y-5">
              <div className="flex justify-between items-center">
                <span className="text-xs text-slate-400">Active Habits</span>
                <span className="text-xl font-black text-white">{habitCount}</span>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-xs text-slate-400">DB Engine</span>
                <span className="text-xs font-mono text-blue-400">SQLite v3.x</span>
              </div>
              
              <div className="pt-6 border-t border-white/5">
                <div className="flex justify-between text-[10px] font-bold text-slate-500 uppercase mb-2">
                   <span>System Integrity</span>
                   <span>98.2%</span>
                </div>
                <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden p-0.5">
                   <div className="bg-gradient-to-r from-blue-600 to-indigo-400 h-full rounded-full w-[98.2%]" />
                </div>
                <p className="text-[9px] text-slate-600 mt-3 font-mono leading-tight">
                  AUTH_TOKEN: AES_256_GCM <br />
                  LOCATION: ABEOKUTA_LOCAL_NODE
                </p>
              </div>
           </div>
        </div>
      </div>
    </section>
  );
};