import React, { useState } from 'react';
import { Target, Sparkles, ArrowRight, User, Hash, Lock } from 'lucide-react';

export const Login = ({ onLogin, onBack }) => {
  const [name, setName] = useState('');
  const [matric, setMatric] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!name.trim()) return;
    
    setLoading(true);
    setTimeout(() => {
      onLogin({ name, matric });
      setLoading(false);
    }, 1500);
  };

  return (
    <div className="min-h-screen bg-slate-50 flex items-center justify-center p-6 selection:bg-blue-500/20">
      {/* Background Effects */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-1/4 -left-20 w-96 h-96 bg-blue-500/10 rounded-full blur-[120px] animate-pulse" />
        <div className="absolute bottom-1/4 -right-20 w-96 h-96 bg-indigo-500/10 rounded-full blur-[120px] animate-pulse delay-700" />
      </div>

      <div className="relative w-full max-w-md animate-in fade-in zoom-in duration-700">
        <div className="bg-white rounded-[2.5rem] p-10 shadow-xl shadow-blue-500/5 border border-blue-100">
          
          {/* Header */}
          <div className="text-center space-y-4 mb-10">
            <div className="flex flex-col items-center gap-4">
              <div className="p-4 bg-blue-600 rounded-3xl shadow-xl shadow-blue-600/20">
                <Target className="text-white" size={32} />
              </div>
              <div className="space-y-1">
                <h2 className="text-3xl font-black text-slate-900 tracking-tight">Welcome back</h2>
                <p className="text-slate-500 text-sm font-medium italic">Enter your workspace to continue growing.</p>
              </div>
            </div>
          </div>

          {/* Form */}
          <form onSubmit={handleSubmit} className="space-y-6">
            <div className="space-y-4">
              <div className="relative group">
                <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                  <User size={18} className="text-blue-500" />
                </div>
                <input
                  required
                  type="text"
                  placeholder="Your Full Name"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  className="w-full bg-slate-50 border border-slate-200 text-slate-900 pl-11 pr-4 py-4 rounded-2xl focus:outline-none focus:ring-2 focus:ring-blue-600/20 focus:border-blue-500 transition-all placeholder:text-slate-400 font-medium"
                />
              </div>

              <div className="relative group">
                <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                  <Hash size={18} className="text-blue-500" />
                </div>
                <input
                  type="text"
                  placeholder="ID / Reference (Optional)"
                  value={matric}
                  onChange={(e) => setMatric(e.target.value)}
                  className="w-full bg-slate-50 border border-slate-200 text-slate-900 pl-11 pr-4 py-4 rounded-2xl focus:outline-none focus:ring-2 focus:ring-blue-600/20 focus:border-blue-500 transition-all placeholder:text-slate-400 font-medium"
                />
              </div>
            </div>

            <button
              disabled={loading}
              className="relative w-full group overflow-hidden bg-blue-600 hover:bg-blue-700 disabled:opacity-50 text-white font-bold py-4 rounded-2xl transition-all shadow-lg shadow-blue-600/20 active:scale-[0.98]"
            >
              <div className="relative z-10 flex items-center justify-center gap-2">
                {loading ? (
                    <>
                      <div className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                      <span>Opening Workspace...</span>
                    </>
                ) : (
                    <>
                      <span>Sign In</span>
                      <ArrowRight size={18} className="group-hover:translate-x-1 transition-transform" />
                    </>
                )}
              </div>
            </button>

            {onBack && (
              <button 
                type="button"
                onClick={onBack}
                disabled={loading}
                className="w-full py-3 text-slate-400 hover:text-blue-600 text-xs font-bold uppercase tracking-widest transition-all hover:bg-blue-50/50 rounded-xl"
              >
                Return to Overview
              </button>
            )}
          </form>

          {/* Footer Info */}
          <div className="mt-10 pt-8 border-t border-slate-100 text-center">
            <div className="flex items-center justify-center gap-2 text-blue-600 font-black text-[10px] uppercase tracking-widest bg-blue-50 py-2 rounded-xl">
              <Lock size={12} />
              <span>Secure Local Access Control</span>
            </div>
          </div>
        </div>
        
        <div className="mt-8 text-center space-y-1">
          <p className="text-slate-400 text-[10px] font-bold uppercase tracking-[0.2em]">
            HabitOS Achievement Engine
          </p>
          <p className="text-slate-300 text-[10px] font-medium italic">
            v1.2.0 // Release "Genesis"
          </p>
        </div>
      </div>
    </div>
  );
};
