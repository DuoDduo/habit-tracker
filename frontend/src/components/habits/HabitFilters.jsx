/**
 * Habit Filters Component
 * Author: Blessing Oluwapelumi James
 */

import React from 'react';
import { FILTER_OPTIONS } from '../../utils/constants';

export const HabitFilters = ({ activeFilter, onFilterChange }) => {
  return (
    <div className="bg-white rounded-xl shadow-sm p-4">
      <div className="flex items-center gap-2">
        <span className="text-sm font-semibold text-gray-600 mr-2">Filter:</span>
        {FILTER_OPTIONS.map((option) => (
          <button
            key={option.value}
            onClick={() => onFilterChange(option.value)}
            className={`px-4 py-2 rounded-lg font-medium transition ${
              activeFilter === option.value
                ? 'bg-blue-600 text-white'
                : 'bg-gray-100 hover:bg-gray-200 text-gray-700'
            }`}
          >
            {option.label}
          </button>
        ))}
      </div>
    </div>
  );
};