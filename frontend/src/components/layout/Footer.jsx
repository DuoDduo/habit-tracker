/**
 * HabitOS Global Footer
 * Updated for Dark Mode Aesthetics & Cybersecurity Theme
 * Author: Blessing Oluwapelumi James
 */

import React from 'react';
import { Github, Code2, Globe, ShieldCheck, Cpu, Terminal, Database, Lock, Power } from 'lucide-react';

export const Footer = () => {
  const currentYear = new Date().getFullYear();
  
  return (
    <footer className="bg-[#0F172A] border-t border-slate-800 transition-all">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-14">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-12 items-start">
          
          {/* 1. Identity & Cyber Profile */}
          <div className="md:col-span-2 space-y-6">
            <div className="flex items-center gap-3">
              <div className="relative flex h-2.5 w-2.5">
                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-500 opacity-75"></span>
                <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-blue-500"></span>
              </div>
              <span className="font-mono text-[10px] tracking-[0.2em] uppercase text-slate-500 font-black">
                System_Link // Status: Secured
              </span>
            </div>
            
            <div>
              <p className="text-xl font-black text-white tracking-tight">
                Blessing Oluwapelumi James
              </p>
              <p className="text-xs font-bold text-blue-400 uppercase tracking-widest mt-1">
                B.Sc. Cybersecurity Student // Data Science Enthusiast
              </p>
            </div>
            
            <p className="text-sm text-slate-400 leading-relaxed max-w-sm font-medium">
              Engineering secure architectures at the intersection of behavioral data and system integrity. Dedicated to local data sovereignty and encrypted habit nodes.
            </p>
          </div>

          {/* 2. Environment (Tech Stack) */}
          <div className="flex flex-col space-y-5">
            <div className="flex items-center gap-2">
              <Cpu size={14} className="text-slate-500" />
              <span className="font-mono text-[10px] tracking-[0.2em] uppercase text-slate-500 font-black">Environment</span>
            </div>
            <div className="flex flex-wrap gap-2">
              {['React 19', 'Flask', 'SQLAlchemy', 'SQLite 3', 'Tailwind v4'].map((tech) => (
                <span key={tech} className="px-2.5 py-1 bg-slate-900 text-slate-300 text-[9px] font-black rounded border border-slate-800 uppercase tracking-tighter flex items-center gap-1.5 hover:border-blue-500/50 transition-colors">
                  {tech === 'SQLite 3' && <Database size={10} className="text-blue-500" />}
                  {tech}
                </span>
              ))}
            </div>
          </div>

          {/* 3. Connectivity & Verification */}
          <div className="flex flex-col md:items-end space-y-5">
            <div className="flex items-center gap-2">
              <Terminal size={14} className="text-slate-500" />
              <span className="font-mono text-[10px] tracking-[0.2em] uppercase text-slate-500 font-black">Connectivity</span>
            </div>
            <div className="flex items-center gap-4">
              <FooterIcon href="https://github.com" icon={<Github size={20} />} />
              <FooterIcon href="#" icon={<Globe size={20} />} />
              <FooterIcon href="#" icon={<Code2 size={20} />} />
              <div className="h-6 w-px bg-slate-800 mx-2" />
              <div className="text-blue-500 animate-pulse" title="AES-256 Verified">
                <Lock size={22} strokeWidth={2.5} />
              </div>
            </div>
          </div>
        </div>

        {/* 4. Bottom System Bar */}
        <div className="mt-16 pt-8 border-t border-slate-800/50 flex flex-col md:flex-row justify-between items-center gap-8">
          <div className="flex flex-col md:flex-row items-center gap-5">
            <div className="flex items-center gap-2 bg-slate-900/50 px-4 py-1.5 rounded-full border border-slate-800">
               <Power size={10} className="text-blue-500" />
               <p className="text-[10px] font-mono text-slate-400 uppercase tracking-widest">
                 © {currentYear} // v1.0.4-stable // Abeokuta_Node
               </p>
            </div>
            <span className="hidden md:block text-slate-800">|</span>
            <p className="text-[10px] font-mono text-slate-500">
              HASH_STATE: <span className="text-blue-500/80 font-bold">LOCAL_DB_ENCRYPTED</span>
            </p>
          </div>
          
          <p className="text-[11px] text-slate-500 italic font-medium tracking-tight">
            "Whatever you do, do it heartily, as to the Lord."
          </p>
        </div>
      </div>
    </footer>
  );
};

const FooterIcon = ({ href, icon }) => (
  <a 
    href={href} 
    target="_blank" 
    rel="noreferrer" 
    className="text-slate-500 hover:text-blue-400 hover:scale-110 transition-all duration-300"
  >
    {icon}
  </a>
);