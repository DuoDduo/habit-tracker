/**
 * Habit Card Component
 * Author: Blessing Oluwapelumi James
 */

import React, { useState } from 'react';
import { Trash2, Check, Calendar, TrendingUp } from 'lucide-react';
import { Card } from '../common/Card';
import { Badge } from '../common/Badge';
import { Button } from '../common/Button';
import { StreakDisplay } from './StreakDisplay';
import { formatRelativeTime } from '../../utils/formatters';

export const HabitCard = ({ 
  habit, 
  onCheckOff, 
  onDelete 
}) => {
  const [isDeleting, setIsDeleting] = useState(false);
  const [isChecking, setIsChecking] = useState(false);

  const handleCheckOff = async () => {
    setIsChecking(true);
    try {
      await onCheckOff(habit.habit_id);
    } finally {
      setIsChecking(false);
    }
  };

  const handleDelete = async () => {
    if (window.confirm(`Delete "${habit.name}"? This action cannot be undone.`)) {
      setIsDeleting(true);
      try {
        await onDelete(habit.habit_id);
      } catch {
        setIsDeleting(false);
      }
    }
  };

  return (
    <Card hover className="transition-all duration-200">
      <div className="flex items-start justify-between gap-4">
        {/* Main Content */}
        <div className="flex-1 min-w-0">
          {/* Header */}
          <div className="flex items-center gap-3 mb-3">
            <h3 className="text-xl font-bold text-gray-800 truncate">
              {habit.name}
            </h3>
            <Badge type={habit.periodicity}>
              {habit.periodicity}
            </Badge>
            {habit.is_broken && (
              <span className="text-xs bg-red-100 text-red-700 px-2 py-1 rounded-full font-semibold">
                Broken
              </span>
            )}
          </div>

          {/* Description */}
          {habit.specification && (
            <p className="text-gray-600 mb-4 line-clamp-2">
              {habit.specification}
            </p>
          )}

          {/* Stats */}
          <div className="flex flex-wrap items-center gap-4 text-sm mb-4">
            {/* Current Streak */}
            <div className="flex items-center gap-2">
              <div className="bg-green-100 p-1.5 rounded">
                <TrendingUp size={16} className="text-green-600" />
              </div>
              <div>
                <span className="text-gray-500">Current:</span>
                <span className="ml-1 font-bold text-green-600">
                  {habit.current_streak}
                </span>
              </div>
            </div>

            {/* Longest Streak */}
            <div className="flex items-center gap-2">
              <div className="bg-blue-100 p-1.5 rounded">
                <TrendingUp size={16} className="text-blue-600" />
              </div>
              <div>
                <span className="text-gray-500">Best:</span>
                <span className="ml-1 font-bold text-blue-600">
                  {habit.longest_streak}
                </span>
              </div>
            </div>

            {/* Completions */}
            <div className="flex items-center gap-2">
              <div className="bg-purple-100 p-1.5 rounded">
                <Calendar size={16} className="text-purple-600" />
              </div>
              <div>
                <span className="text-gray-500">Total:</span>
                <span className="ml-1 font-bold text-purple-600">
                  {habit.completion_count}
                </span>
              </div>
            </div>
          </div>

          {/* Created Date */}
          <p className="text-xs text-gray-400">
            Created {formatRelativeTime(habit.created_at)}
          </p>
        </div>

        {/* Actions */}
        <div className="flex flex-col gap-2">
          <Button
            variant="success"
            size="sm"
            onClick={handleCheckOff}
            loading={isChecking}
            disabled={isDeleting}
            icon={Check}
          >
            Check Off
          </Button>
          <Button
            variant="danger"
            size="sm"
            onClick={handleDelete}
            loading={isDeleting}
            disabled={isChecking}
            icon={Trash2}
          >
            Delete
          </Button>
        </div>
      </div>

      {/* Visual Streak Display */}
      <StreakDisplay 
        currentStreak={habit.current_streak}
        longestStreak={habit.longest_streak}
        periodicity={habit.periodicity}
        isBroken={habit.is_broken}
      />
    </Card>
  );
};