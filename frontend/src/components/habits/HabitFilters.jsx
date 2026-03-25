/**
 * Habit Filters Component
 * Refined for Professional UX/UI & Responsive Overflow
 * Author: Blessing Oluwapelumi James
 */

import React from 'react';
import { Filter } from 'lucide-react'; // Adding an icon for context
import { FILTER_OPTIONS } from '../../utils/constants';

export const HabitFilters = ({ activeFilter, onFilterChange }) => {
  return (
    <div className="bg-white/80 backdrop-blur-md sticky top-0 z-10 py-3 mb-6">
      <div className="flex flex-col sm:flex-row items-center gap-4">
        
        {/* Label - Hidden on very small screens to save space */}
        <div className="hidden sm:flex items-center gap-2 text-gray-400">
          <Filter size={16} />
          <span className="text-xs font-bold uppercase tracking-widest">Filter</span>
        </div>

        {/* Scrollable Container for Mobile */}
        <div className="w-full overflow-x-auto no-scrollbar pb-1 sm:pb-0">
          <div className="flex items-center gap-2 min-w-max">
            {FILTER_OPTIONS.map((option) => {
              const isActive = activeFilter === option.value;
              
              return (
                <button
                  key={option.value}
                  onClick={() => onFilterChange(option.value)}
                  className={`
                    relative px-5 py-2 rounded-full text-sm font-bold transition-all duration-300
                    ${isActive 
                      ? 'text-white shadow-md shadow-blue-100' 
                      : 'text-gray-500 hover:text-gray-900 hover:bg-gray-100'
                    }
                  `}
                >
                  {/* Background Layer for Active State */}
                  {isActive && (
                    <div className="absolute inset-0 bg-blue-600 rounded-full -z-10 animate-in zoom-in-95 duration-200" />
                  )}
                  
                  <span className="relative z-10">{option.label}</span>
                  
                  {/* Indicator Dot (Optional) */}
                  {isActive && (
                    <span className="absolute -top-1 -right-1 flex h-2 w-2">
                      <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"></span>
                      <span className="relative inline-flex rounded-full h-2 w-2 bg-blue-500"></span>
                    </span>
                  )}
                </button>
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
};