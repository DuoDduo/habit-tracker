import React from 'react';
import { Target, Zap, BarChart3, ShieldCheck, ArrowRight, Sparkles, CheckCircle2, Layout, Award } from 'lucide-react';
import { LandingIllustration } from '../common/Illustrations';

export const Landing = ({ onGetStarted }) => {
  return (
    <div className="min-h-screen bg-white text-slate-900 selection:bg-blue-100 selection:text-blue-700">
      {/* 1. Navigation */}
      <nav className="fixed top-0 w-full z-50 bg-white/80 backdrop-blur-xl border-b border-slate-100 px-6 py-4">
        <div className="max-w-7xl mx-auto flex justify-between items-center">
          <div className="flex items-center gap-2">
            <div className="bg-blue-600 p-1.5 rounded-lg shadow-lg shadow-blue-600/20">
              <Target className="text-white" size={18} />
            </div>
            <span className="text-xl font-black tracking-tighter">HabitOS</span>
          </div>
          <button 
            onClick={onGetStarted}
            className="px-5 py-2 text-sm font-bold text-blue-600 hover:bg-blue-50 rounded-xl transition-all"
          >
            Sign In
          </button>
        </div>
      </nav>

      {/* 2. Hero Section */}
      <section className="pt-32 pb-20 px-6">
        <div className="max-w-7xl mx-auto grid lg:grid-cols-2 gap-16 items-center">
          <div className="space-y-8 animate-fade-in-up">
            <div className="inline-flex items-center gap-2 px-3 py-1 bg-blue-50 border border-blue-100 text-blue-600 rounded-full text-[10px] font-black uppercase tracking-widest">
              <Sparkles size={12} />
              <span>Version 1.2 is here</span>
            </div>
            
            <h1 className="text-5xl md:text-7xl font-black tracking-tight leading-[1.05]">
              Master your <br />
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-indigo-600">
                Consistency Engine.
              </span>
            </h1>
            
            <p className="text-lg text-slate-500 max-w-lg leading-relaxed font-medium">
              HabitOS is the premium dashboard for high-achievers. Transform your daily routines into visual progress and data-driven success.
            </p>

            <div className="flex flex-col sm:flex-row gap-4 pt-4">
              <button 
                onClick={onGetStarted}
                className="group flex items-center justify-center gap-3 px-8 py-4 bg-blue-600 hover:bg-blue-700 text-white rounded-2xl font-black text-sm transition-all shadow-xl shadow-blue-600/30 active:scale-95"
              >
                Start Your Journey
                <ArrowRight size={18} className="group-hover:translate-x-1 transition-transform" />
              </button>
              <div className="flex items-center gap-3 px-6 py-4 bg-slate-50 border border-slate-100 rounded-2xl text-xs font-bold text-slate-400">
                <CheckCircle2 size={16} className="text-blue-500" />
                <span>80% Success Rate Reported</span>
              </div>
            </div>
          </div>

          <div className="relative animate-float delay-500">
            {/* Social Proof Mini-Cards */}
            <div className="absolute -top-6 -left-6 z-20 bg-white p-4 rounded-2xl shadow-xl border border-blue-50 animate-bounce-slow">
               <div className="flex items-center gap-3">
                  <div className="flex -space-x-2">
                    {[1, 2, 3].map(i => (
                      <div key={i} className="w-8 h-8 rounded-full bg-blue-100 border-2 border-white flex items-center justify-center text-[10px] font-bold">
                        {String.fromCharCode(64 + i)}
                      </div>
                    ))}
                  </div>
                  <div className="text-[10px] font-black uppercase text-blue-600">Join 2k+ Achievers</div>
               </div>
            </div>

            {/* Premium Illustration Preview */}
            <div className="relative z-10 w-full h-auto">
               <LandingIllustration className="w-full h-full drop-shadow-2xl" />
            </div>
            
            {/* Floating Accents */}
            <div className="absolute -top-10 -right-10 w-32 h-32 bg-blue-400/20 blur-3xl rounded-full" />
            <div className="absolute -bottom-10 -left-10 w-40 h-40 bg-indigo-400/20 blur-3xl rounded-full" />
          </div>
        </div>
      </section>

      {/* 3. Features Grid */}
      <section className="py-24 bg-slate-50/50 border-y border-slate-100 px-6">
        <div className="max-w-7xl mx-auto space-y-16">
          <div className="text-center space-y-4 max-w-2xl mx-auto">
             <h2 className="text-3xl font-black tracking-tight">Built for Performance</h2>
             <p className="text-slate-500 font-medium">Why thousands of professionals choose HabitOS for their daily achievement tracking.</p>
          </div>

          <div className="grid md:grid-cols-3 gap-8">
            <FeatureCard 
              icon={<Award className="text-blue-600" />}
              title="Streak Mastery"
              description="Our protective logic ensures your hard-earned progress is visualized and celebrated daily."
            />
            <FeatureCard 
              icon={<Layout className="text-indigo-600" />}
              title="Premium Interface"
              description="A clutter-free, animated workspace designed to reduce cognitive load and focus on growth."
            />
            <FeatureCard 
              icon={<BarChart3 className="text-emerald-600" />}
              title="Deep Analytics"
              description="Unlock insights into your behavioral patterns with beautiful, real-time data visualizations."
            />
          </div>
        </div>
      </section>

      {/* 4. Social Proof / Quote */}
      <section className="py-24 px-6 text-center">
         <div className="max-w-4xl mx-auto space-y-10">
            <div className="flex justify-center">
               <div className="p-4 bg-blue-50 rounded-3xl">
                 <ShieldCheck className="text-blue-600" size={40} />
               </div>
            </div>
            <blockquote className="text-2xl md:text-4xl font-black italic text-slate-900 tracking-tight leading-snug">
              "Whatever you do, do it heartily, as to the Lord."
            </blockquote>
            <p className="text-slate-400 font-bold uppercase tracking-[0.3em] text-xs">The Excellence Philosophy</p>
         </div>
      </section>

      {/* 5. Final CTA */}
      <section className="pb-32 px-6">
        <div className="max-w-5xl mx-auto bg-blue-600 rounded-[3rem] p-12 md:p-20 text-center text-white relative overflow-hidden shadow-2xl shadow-blue-600/40">
           <div className="absolute top-0 right-0 w-64 h-64 bg-white/10 blur-3xl rounded-full translate-x-1/2 -translate-y-1/2" />
           <div className="relative z-10 space-y-8">
             <h2 className="text-3xl md:text-5xl font-black tracking-tight">Ready to build your engine?</h2>
             <p className="text-blue-100 text-lg font-medium max-w-xl mx-auto">
               Join HabitOS today and take the first step towards a more consistent, data-driven version of yourself.
             </p>
             <button 
               onClick={onGetStarted}
               className="px-10 py-5 bg-white text-blue-600 hover:bg-blue-50 rounded-2xl font-black text-sm transition-all shadow-xl active:scale-95"
             >
               Initialize Your Space
             </button>
           </div>
        </div>
      </section>

      {/* Simple Footer */}
      <footer className="py-12 border-t border-slate-100 px-6 text-center">
         <div className="flex flex-col items-center gap-4">
            <div className="flex items-center gap-2">
              <Target className="text-slate-300" size={16} />
              <span className="text-sm font-black text-slate-300 tracking-tighter">HabitOS</span>
            </div>
            <p className="text-[10px] text-slate-400 font-bold uppercase tracking-widest">
              Created by Blessing Oluwapelumi James // v1.2.0
            </p>
         </div>
      </footer>
    </div>
  );
};

const FeatureCard = ({ icon, title, description }) => (
  <div className="bg-white p-8 rounded-[2.5rem] border border-slate-100 shadow-sm hover:shadow-xl hover:shadow-blue-500/5 transition-all group">
    <div className="w-14 h-14 bg-slate-50 rounded-2xl flex items-center justify-center mb-6 border border-slate-100 group-hover:bg-white group-hover:scale-110 transition-all">
      {icon}
    </div>
    <h3 className="text-xl font-black mb-3">{title}</h3>
    <p className="text-slate-500 text-sm leading-relaxed font-medium">
      {description}
    </p>
  </div>
);
