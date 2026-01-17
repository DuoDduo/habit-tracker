/**
 * Habit List Component
 * Author: Blessing Oluwapelumi James
 */

import React from 'react';
import { HabitCard } from './HabitCard';
import { EmptyState } from '../ui/EmptyState';
import { Target } from 'lucide-react';

export const HabitList = ({ 
  habits, 
  onCheckOff, 
  onDelete,
  onCreateClick 
}) => {
  if (habits.length === 0) {
    return (
      <EmptyState
        icon={Target}
        title="No habits found"
        description="Start your journey by creating your first habit. Build consistency one day at a time!"
        actionLabel="Create your first habit"
        onAction={onCreateClick}
      />
    );
  }

  return (
    <div className="grid gap-4">
      {habits.map((habit) => (
        <HabitCard
          key={habit.habit_id}
          habit={habit}
          onCheckOff={onCheckOff}
          onDelete={onDelete}
        />
      ))}
    </div>
  );
};