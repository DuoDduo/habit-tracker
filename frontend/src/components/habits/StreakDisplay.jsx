/**
 * Streak Visual Display Component
 * Author: Blessing Oluwapelumi James
 */

import React from 'react';
import { getStreakEmoji } from '../../utils/formatters';

export const StreakDisplay = ({ 
  currentStreak, 
  longestStreak,
  periodicity,
  isBroken 
}) => {
  const emoji = getStreakEmoji(currentStreak);
  const percentage = longestStreak > 0 
    ? (currentStreak / longestStreak) * 100 
    : 0;

  return (
    <div className="mt-4 pt-4 border-t">
      {/* Emoji & Message */}
      <div className="flex items-center justify-between mb-3">
        <div className="flex items-center gap-2">
          <span className="text-2xl">{emoji}</span>
          <div>
            <p className="text-sm font-semibold text-gray-800">
              {isBroken ? 'Streak Broken' : `${currentStreak} ${periodicity === 'daily' ? 'day' : 'week'} streak`}
            </p>
            <p className="text-xs text-gray-500">
              {isBroken 
                ? 'Start again today!' 
                : currentStreak === longestStreak 
                ? '🎉 Personal best!'
                : `${longestStreak - currentStreak} to beat your record`
              }
            </p>
          </div>
        </div>
      </div>

      {/* Progress Bar */}
      <div className="w-full bg-gray-200 rounded-full h-2">
        <div
          className={`h-2 rounded-full transition-all duration-500 ${
            isBroken 
              ? 'bg-red-500'
              : percentage >= 100 
              ? 'bg-gradient-to-r from-green-500 to-emerald-500'
              : 'bg-gradient-to-r from-blue-500 to-indigo-500'
          }`}
          style={{ width: `${Math.min(percentage, 100)}%` }}
        />
      </div>
    </div>
  );
};