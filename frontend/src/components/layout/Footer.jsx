import React from 'react';
import { Github, Globe, Code2, Target, Power, Heart } from 'lucide-react';

export const Footer = () => {
  const currentYear = new Date().getFullYear();
  
  return (
    <footer className="bg-white border-t border-gray-100 py-12 px-6 sm:px-12 mt-auto">
      <div className="max-w-7xl mx-auto">
        <div className="flex flex-col md:flex-row justify-between items-center gap-8 mb-10">
          <div className="space-y-4 text-center md:text-left">
            <div className="flex items-center justify-center md:justify-start gap-3">
              <div className="bg-blue-600 p-2 rounded-xl shadow-lg shadow-blue-600/20">
                <Target className="text-white" size={20} />
              </div>
              <span className="text-xl font-black text-slate-900 tracking-tighter">HabitOS</span>
            </div>
            <p className="text-sm text-slate-400 max-w-xs font-medium italic">
              Empowering personal growth through data-driven habit tracking.
            </p>
          </div>

          <div className="flex items-center gap-6">
            <FooterLink href="#" icon={<Github size={20} />} label="Source" />
            <FooterLink href="#" icon={<Globe size={20} />} label="Website" />
            <FooterLink href="#" icon={<Code2 size={20} />} label="Docs" />
          </div>
        </div>

        <div className="pt-8 border-t border-gray-100 flex flex-col sm:flex-row justify-between items-center gap-6 text-[10px] font-bold text-slate-400 uppercase tracking-[0.2em]">
          <div className="flex items-center gap-2 bg-blue-50 text-blue-600 px-4 py-2 rounded-full border border-blue-100">
            <Power size={12} className="animate-pulse" />
            <span>Achievement Engine Active</span>
          </div>
          
          <div className="flex flex-col items-center sm:items-end gap-1">
            <p>© {currentYear} HabitOS Genesis // v1.2.0</p>
            <p className="flex items-center gap-1.5 lowercase italic font-medium normal-case">
              built with <Heart size={10} className="text-red-400 fill-current" /> for personal excellence
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
};

const FooterLink = ({ href, icon, label }) => (
  <a 
    href={href} 
    className="flex flex-col items-center gap-1 group transition-all"
  >
    <div className="p-2 text-slate-400 group-hover:text-blue-600 group-hover:bg-blue-50 rounded-xl transition-all">
      {icon}
    </div>
    <span className="text-[9px] font-bold text-slate-400 group-hover:text-blue-600 uppercase tracking-widest">{label}</span>
  </a>
);