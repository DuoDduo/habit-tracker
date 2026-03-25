/**
 * Habit Card Component
 * Refined for High-Density Systems & Mobile Responsiveness
 * Author: Blessing Oluwapelumi James
 */

import React, { useState, useMemo } from 'react';
import { Trash2, Check, Flame, Calendar, Zap, Sparkles, Activity } from 'lucide-react';
import { Card } from '../common/Card';
import { Badge } from '../common/Badge';
import { StreakDisplay } from './StreakDisplay';

export const HabitCard = ({ habit, onCheckOff, onDelete }) => {
  const [isDeleting, setIsDeleting] = useState(false);
  const [isChecking, setIsChecking] = useState(false);

  const isNew = useMemo(() => {
    const createdDate = new Date(habit.created_at);
    const now = new Date();
    const diffInHours = (now - createdDate) / (1000 * 60 * 60);
    return diffInHours < 24;
  }, [habit.created_at]);

  const handleCheckOff = async () => {
    setIsChecking(true);
    try {
      await onCheckOff(habit.habit_id);
    } catch (error) {
      console.error("Action failed:", error);
    } finally {
      setIsChecking(false);
    }
  };

  const handleDelete = async () => {
    if (window.confirm(`Confirm Deletion: "${habit.name}"? This is irreversible.`)) {
      setIsDeleting(true);
      try {
        await onDelete(habit.habit_id);
      } catch (error) {
        setIsDeleting(false);
      }
    }
  };

  const getButtonStyles = () => {
    if (isChecking) return 'bg-slate-100 text-slate-400 cursor-not-allowed';
    if (habit.is_broken) return 'bg-orange-500 hover:bg-orange-600 shadow-lg shadow-orange-200 active:scale-95';
    return 'bg-indigo-600 hover:bg-indigo-700 shadow-lg shadow-indigo-200 active:scale-90 text-white';
  };

  return (
    <Card hover className="relative group overflow-hidden border border-slate-100 shadow-sm card-hover bg-white rounded-[2rem]">
      {/* Decorative background glow for 'New' habits */}
      {isNew && (
        <div className="absolute -top-12 -right-12 w-24 h-24 bg-emerald-500/10 blur-3xl rounded-full" />
      )}

      {/* Vertical Status Indicator */}
      <div 
        className={`absolute left-0 top-0 bottom-0 w-1.5 transition-all duration-700 ${
          habit.is_broken ? 'bg-orange-400' : 'bg-indigo-500'
        }`} 
      />

      <div className="p-6">
        <div className="flex flex-col lg:flex-row items-start justify-between gap-6">
          
          <div className="flex-1 min-w-0 w-full space-y-4">
            {/* Header Metadata */}
            <div className="flex items-center flex-wrap gap-2">
              {isNew && (
                <span className="flex items-center gap-1 text-[10px] bg-emerald-100 text-emerald-700 px-2.5 py-1 rounded-full font-black uppercase tracking-tighter border border-emerald-200 animate-pulse">
                  <Sparkles size={10} strokeWidth={3} /> NEW HABIT
                </span>
              )}
              
              <Badge type={habit.periodicity} className="bg-slate-100 text-slate-600 border-none px-3 py-1 text-[10px] font-bold uppercase tracking-widest">
                {habit.periodicity}
              </Badge>

              {habit.is_broken && (
                <span className="flex items-center gap-1 text-[10px] bg-orange-50 text-orange-600 px-2.5 py-1 rounded-full font-bold uppercase tracking-widest border border-orange-100">
                  <Activity size={10} /> Needs Reset
                </span>
              )}
            </div>

            {/* Habit Title & Specification */}
            <div>
              <h3 className="text-2xl font-black text-slate-900 tracking-tight leading-none mb-2 group-hover:text-indigo-600 transition-colors">
                {habit.name}
              </h3>
              {habit.specification && (
                <p className="text-sm text-slate-500 leading-relaxed max-w-md line-clamp-2">
                  {habit.specification}
                </p>
              )}
            </div>

            {/* Progress Metrics Hub */}
            <div className="grid grid-cols-3 gap-1 p-1 bg-slate-50/50 rounded-2xl border border-slate-100 glass">
              <div className="flex flex-col items-center justify-center py-3 bg-white/80 backdrop-blur-md rounded-xl shadow-sm border border-slate-100/50">
                <span className="text-[9px] font-black text-slate-400 uppercase tracking-widest mb-1">Streak</span>
                <div className={`flex items-center gap-1 text-lg font-black ${habit.is_broken ? 'text-slate-300' : 'text-blue-600'}`}>
                  <Flame size={16} fill={habit.is_broken ? "none" : "currentColor"} />
                  {habit.current_streak}
                </div>
              </div>
              <div className="flex flex-col items-center justify-center py-3">
                <span className="text-[9px] font-black text-slate-400 uppercase tracking-widest mb-1">Record</span>
                <span className="text-lg font-black text-slate-700">{habit.longest_streak}</span>
              </div>
              <div className="flex flex-col items-center justify-center py-3">
                <span className="text-[9px] font-black text-slate-400 uppercase tracking-widest mb-1">Total</span>
                <span className="text-lg font-black text-blue-600">{habit.completion_count}</span>
              </div>
            </div>
          </div>

          {/* Action Hub */}
          <div className="flex lg:flex-col items-center justify-between w-full lg:w-auto gap-4">
            <button
              onClick={handleCheckOff}
              disabled={isChecking || isDeleting}
              className={`
                flex-1 lg:w-20 lg:h-20 flex flex-col items-center justify-center rounded-[2rem] transition-all duration-500
                ${getButtonStyles()}
              `}
            >
              {isChecking ? (
                <div className="w-6 h-6 border-2 border-indigo-400 border-t-transparent rounded-full animate-spin" />
              ) : habit.is_broken ? (
                <>
                  <Zap className="text-white" size={28} />
                  <span className="text-[9px] text-white font-black uppercase mt-1 hidden lg:block tracking-widest">Restart</span>
                </>
              ) : (
                <>
                  <Check className="text-white" size={36} strokeWidth={3} />
                  <span className="text-[9px] text-white font-black uppercase mt-1 hidden lg:block tracking-widest">Done</span>
                </>
              )}
            </button>

            <button 
              onClick={handleDelete}
              disabled={isChecking || isDeleting}
              className="p-3 text-slate-300 hover:text-red-500 hover:bg-red-50 rounded-2xl transition-all sm:opacity-0 group-hover:opacity-100 focus:opacity-100"
              title="Delete Habit"
            >
               <Trash2 size={20} />
            </button>
          </div>
        </div>

        {/* Dynamic Streak Component Integration */}
        <div className="mt-8">
          <StreakDisplay 
            currentStreak={habit.current_streak}
            longestStreak={habit.longest_streak}
            periodicity={habit.periodicity}
            isBroken={habit.is_broken}
            onAction={handleCheckOff} 
            loading={isChecking}
          />
        </div>

        {/* System Metadata Footer */}
        <div className="mt-6 pt-5 border-t border-slate-50 flex flex-col sm:flex-row items-center justify-between gap-4">
            <div className="flex items-center gap-2 text-[10px] font-bold text-slate-400 uppercase tracking-widest">
              <Calendar size={14} className="text-slate-300" />
              <span>Started {new Date(habit.created_at).toLocaleDateString()}</span>
            </div>
            
            <div className="flex items-center gap-3">
              <span className="text-[9px] font-black text-slate-300 uppercase tracking-widest">Performance Scale</span>
              <div className="flex gap-1.5 p-1.5 bg-slate-100 rounded-full border border-slate-200/50">
                {[...Array(5)].map((_, i) => (
                  <div 
                    key={i} 
                    className={`w-2.5 h-1.5 rounded-full transition-all duration-500 ${
                      i < 3 
                        ? 'bg-blue-600 shadow-[0_0_8px_rgba(37,99,235,0.3)]' 
                        : 'bg-slate-300'
                    }`} 
                  />
                ))}
              </div>
            </div>
        </div>
      </div>
    </Card>
  );
};