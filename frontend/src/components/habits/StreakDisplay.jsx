/**
 * Streak Visual Display Component
 * Refined for Human Clarity: Focuses on "Starting Again" after a miss.
 * Author: Blessing Oluwapelumi James
 */

import React from 'react';
import { getStreakEmoji } from '../../utils/formatters';
import { PlusCircle, RotateCcw, Award } from 'lucide-react';

export const StreakDisplay = ({ 
  currentStreak, 
  longestStreak,
  periodicity,
  isBroken,
  onAction,
  loading = false
}) => {
  const emoji = getStreakEmoji(currentStreak);
  const unit = periodicity === 'daily' ? 'day' : 'week';
  const label = currentStreak === 1 ? unit : `${unit}s`;
  
  // Calculate how close they are to their record
  const percentage = longestStreak > 0 ? (currentStreak / longestStreak) * 100 : 0;

  return (
    <div className="mt-4 pt-5 border-t border-gray-100">
      {/* 1. Status Header */}
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className={`
            flex items-center justify-center w-12 h-12 rounded-2xl text-2xl
            ${isBroken ? 'bg-gray-100 border-2 border-dashed border-gray-300' : 'bg-orange-50 border border-orange-100'}
          `}>
            {/* If broken, show a "reset" icon; if active, show the fire/emoji */}
            {isBroken ? <RotateCcw size={20} className="text-gray-400" /> : emoji}
          </div>
          
          <div>
            <h4 className={`text-lg font-bold leading-tight ${isBroken ? 'text-gray-500' : 'text-gray-900'}`}>
              {isBroken ? 'Streak Ended' : `${currentStreak} ${label} streak`}
            </h4>
            <p className="text-xs text-gray-500">
              {isBroken ? 'You missed a check-in' : 'You’re doing great!'}
            </p>
          </div>
        </div>

        {/* Longest Streak (Always visible for motivation) */}
        <div className="flex flex-col items-end">
          <div className="flex items-center gap-1 text-blue-600 font-bold text-sm">
            <Award size={14} />
            <span>{longestStreak} {label}</span>
          </div>
          <span className="text-[10px] text-gray-400 uppercase font-bold tracking-tight">Personal Best</span>
        </div>
      </div>

      {/* 2. Progress Bar (Visualizing the journey back to the top) */}
      {!isBroken && (
        <div className="space-y-2 mb-4">
          <div className="w-full bg-gray-100 rounded-full h-2">
            <div
              className="h-2 rounded-full bg-blue-600 transition-all duration-1000"
              style={{ width: `${Math.min(percentage, 100)}%` }}
            />
          </div>
          {currentStreak < longestStreak && (
            <p className="text-[10px] text-gray-500 italic text-right">
              {longestStreak - currentStreak} more to beat your record!
            </p>
          )}
        </div>
      )}

      {/* 3. The Action: For Broken Streaks Only */}
      {isBroken && (
        <div className="bg-blue-50/50 border border-blue-100 p-4 rounded-2xl animate-in zoom-in-95">
          <p className="text-sm text-blue-800 font-medium mb-3 text-center">
             Don't let a miss stop you! Start a new streak today and get back on track.
          </p>
          <button 
            type="button"
            onClick={onAction}
            disabled={loading}
            className={`
              w-full flex items-center justify-center gap-2 py-3 rounded-xl font-bold transition-all
              ${loading 
                ? 'bg-gray-200 text-gray-400 cursor-not-allowed' 
                : 'bg-blue-600 text-white hover:bg-blue-700 shadow-md active:scale-95'
              }
            `}
          >
            {loading ? (
              <div className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin" />
            ) : (
              <PlusCircle size={18} />
            )}
            {loading ? 'Starting...' : 'Start New Streak'}
          </button>
        </div>
      )}
    </div>
  );
};