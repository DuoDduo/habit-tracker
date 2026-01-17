import React from 'react';
import { Github, Code2, Globe } from 'lucide-react';

export const Footer = () => {
  return (
    <footer className="bg-white border-t border-gray-100 mt-20">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 items-start">
          
          {/* Identity & Status */}
          <div className="space-y-3">
            <div className="flex items-center gap-2">
              <div className="w-2 h-2 bg-primary-500 rounded-full animate-pulse" />
              <span className="font-mono text-[10px] tracking-widest uppercase text-gray-400">System Active</span>
            </div>
            <p className="text-sm font-semibold text-gray-900">
              Blessing Oluwapelumi James
            </p>
            <p className="text-xs text-gray-500 leading-relaxed max-w-[240px]">
              B.Sc. Data Science Project // Exploring the intersection of AI Engineering and habit formation.
            </p>
          </div>

          {/* Tech Stack - Using the primary colors from your v4 theme */}
          <div className="flex flex-col md:items-center space-y-3">
            <span className="font-mono text-[10px] tracking-widest uppercase text-gray-400">Environment</span>
            <div className="flex flex-wrap gap-2 md:justify-center">
              {['React 19', 'Flask', 'SQLAlchemy', 'Tailwind v4'].map((tech) => (
                <span key={tech} className="px-2 py-1 bg-primary-50 text-primary-700 text-[10px] font-medium rounded border border-primary-100">
                  {tech}
                </span>
              ))}
            </div>
          </div>

          {/* Navigation & Source */}
          <div className="flex flex-col md:items-end space-y-4">
            <span className="font-mono text-[10px] tracking-widest uppercase text-gray-400">Connectivity</span>
            <div className="flex items-center gap-5">
              <a href="https://github.com" target="_blank" rel="noreferrer" className="text-gray-400 hover:text-gray-900 transition-colors">
                <Github size={18} />
              </a>
              <a href="#" className="text-gray-400 hover:text-primary-600 transition-colors">
                <Globe size={18} />
              </a>
              <a href="#" className="text-gray-400 hover:text-primary-600 transition-colors">
                <Code2 size={18} />
              </a>
            </div>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="mt-10 pt-6 border-t border-gray-50 flex flex-col md:flex-row justify-between items-center gap-4">
          <p className="text-[10px] font-mono text-gray-400 uppercase tracking-tight">
            © {new Date().getFullYear()} // v1.0.4-stable // Abeokuta, Nigeria
          </p>
          <p className="text-[10px] text-gray-400 italic">
            "Whatever you do, do it heartily, as to the Lord."
          </p>
        </div>
      </div>
    </footer>
  );
};