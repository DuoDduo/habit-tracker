import React from 'react';
import { Target, TrendingUp, Calendar, BarChart3, Activity } from 'lucide-react';
import { StatCard } from './StatCard';
import { Loading } from '../common/Loading';
import { ErrorMessage } from '../common/ErrorMessage';

export const AnalyticsDashboard = ({ analytics, loading, error, onRetry }) => {
  if (loading) {
    return (
      <div className="min-h-[200px] flex items-center justify-center">
        <Loading message="Syncing system analytics..." />
      </div>
    );
  }

  if (error) {
    return <ErrorMessage message={error} onRetry={onRetry} />;
  }

  return (
    <div className="space-y-6">
      {/* Header section remains professional but clean */}
      <div className="flex items-center justify-between px-1">
        <div>
          <h2 className="text-lg font-bold text-gray-900">Performance Metrics</h2>
          <p className="text-xs text-gray-500 font-mono uppercase tracking-tighter">
            System Data // Matric: 92134091
          </p>
        </div>
        <div className="flex items-center gap-2 text-xs font-medium text-blue-600 bg-blue-50 px-2 py-1 rounded-full border border-blue-100">
          <Activity size={14} className="animate-pulse" />
          Live Stats
        </div>
      </div>

      {/* Stats Grid using your preferred color coding */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard
          icon={Target}
          label="Total Habits"
          value={analytics.total_habits || 0}
          color="blue"
          subtitle="Being tracked"
        />
        
        <StatCard
          icon={TrendingUp}
          label="Longest Streak"
          value={`${analytics.longest_streak || 0}d`}
          color="green"
          subtitle="Your best performance"
        />
        
        <StatCard
          icon={Calendar}
          label="Daily Habits"
          value={analytics.daily_habits || 0}
          color="purple"
          subtitle="Tracked every day"
        />
        
        <StatCard
          icon={BarChart3}
          label="Weekly Habits"
          value={analytics.weekly_habits || 0}
          color="orange"
          subtitle="Tracked weekly"
        />
      </div>
    </div>
  );
};