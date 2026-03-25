/**
 * Analytics Dashboard Component
 * Professional, Responsive & Insight-driven
 * Author: Blessing Oluwapelumi James
 */

import React from 'react';
import { Target, TrendingUp, Calendar, BarChart3, Activity, Zap, Info } from 'lucide-react';
import { StatCard } from './StatCard';
import { Loading } from '../common/Loading';
import { ErrorMessage } from '../common/ErrorMessage';

export const AnalyticsDashboard = ({ analytics, loading, error, onRetry }) => {
  if (loading) {
    return (
      <div className="min-h-[400px] flex flex-col items-center justify-center bg-white/50 rounded-2xl border border-dashed border-gray-200">
        <Loading message="Aggregating your progress..." />
      </div>
    );
  }

  if (error) {
    return (
      <div className="p-6 bg-white rounded-2xl border border-red-100 shadow-sm">
        <ErrorMessage message={error} onRetry={onRetry} />
      </div>
    );
  }

  // Calculate some quick insights for the professional "Summary Header"
  const completionRate = analytics.total_habits > 0 
    ? Math.round(((analytics.daily_habits + analytics.weekly_habits) / analytics.total_habits) * 100) 
    : 0;

  return (
    <div className="space-y-8 animate-in fade-in duration-500">
      {/* 1. Header & Quick Insight Section */}
      <div className="flex flex-col md:flex-row md:items-end justify-between gap-4 px-1">
        <div className="space-y-1">
          <div className="flex items-center gap-2">
            <h2 className="text-2xl font-extrabold text-gray-900 tracking-tight transition-all">
              Performance Insights
            </h2>
            <div className="flex items-center gap-1.5 text-[10px] font-bold text-blue-600 bg-blue-50 px-2 py-0.5 rounded-md border border-blue-100 uppercase tracking-widest">
              <Activity size={12} className="animate-pulse" />
              Live
            </div>
          </div>
          <p className="text-sm text-gray-500 max-w-md">
            Detailed breakdown of your habit consistency and system engagement.
          </p>
        </div>

        {/* Global Progress Pill - Visible on larger screens */}
        <div className="hidden lg:flex items-center gap-3 bg-white p-2 pr-4 rounded-xl border border-gray-100 shadow-sm">
          <div className="w-10 h-10 rounded-lg bg-emerald-50 flex items-center justify-center text-emerald-600">
            <Zap size={20} fill="currentColor" />
          </div>
          <div>
            <p className="text-[10px] font-bold text-gray-400 uppercase leading-none mb-1">Consistency Score</p>
            <p className="text-lg font-bold text-gray-800 leading-none">{completionRate}%</p>
          </div>
        </div>
      </div>

      {/* 2. Primary Metrics Grid */}
      {/* Responsive Breakpoints: 1 col (mobile), 2 col (tablet), 4 col (desktop) */}
      <div className="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-5">
        <div className="hover:scale-[1.02] transition-transform duration-300">
          <StatCard
            icon={Target}
            label="Total Habits"
            value={analytics.total_habits || 0}
            color="blue"
            subtitle="Active objectives"
          />
        </div>
        
        <div className="hover:scale-[1.02] transition-transform duration-300">
          <StatCard
            icon={TrendingUp}
            label="Longest Streak"
            value={`${analytics.longest_streak || 0}d`}
            color="green"
            subtitle="All-time record"
          />
        </div>
        
        <div className="hover:scale-[1.02] transition-transform duration-300">
          <StatCard
            icon={Calendar}
            label="Daily Habits"
            value={analytics.daily_habits || 0}
            color="purple"
            subtitle="High frequency"
          />
        </div>
        
        <div className="hover:scale-[1.02] transition-transform duration-300">
          <StatCard
            icon={BarChart3}
            label="Weekly Habits"
            value={analytics.weekly_habits || 0}
            color="orange"
            subtitle="Strategic pacing"
          />
        </div>
      </div>

      {/* 3. System Info Footer (Metric ID) */}
      <div className="pt-4 border-t border-gray-100 flex flex-col sm:flex-row items-center justify-between gap-3 opacity-60 hover:opacity-100 transition-opacity">
        <div className="flex items-center gap-2 text-[10px] font-mono text-gray-400">
          <Info size={12} />
          SYSTEM_UID: 92134091 // SHARD_A
        </div>
        <p className="text-[10px] font-medium text-gray-400 italic">
          Last synced: {new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
        </p>
      </div>
    </div>
  );
};