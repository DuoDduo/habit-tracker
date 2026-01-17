/**
 * Application Constants
 * Author: Blessing Oluwapelumi James
 */

export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:5000/api';

export const PERIODICITY = {
  DAILY: 'daily',
  WEEKLY: 'weekly',
};

export const PERIODICITY_OPTIONS = [
  { value: 'daily', label: 'Daily', icon: '📅' },
  { value: 'weekly', label: 'Weekly', icon: '📊' },
];

export const FILTER_OPTIONS = [
  { value: 'all', label: 'All Habits' },
  { value: 'daily', label: 'Daily' },
  { value: 'weekly', label: 'Weekly' },
];

export const MESSAGES = {
  SUCCESS: {
    HABIT_CREATED: 'Habit created successfully! 🎉',
    HABIT_DELETED: 'Habit deleted successfully',
    HABIT_CHECKED: 'Great job! Habit checked off ✅',
  },
  ERROR: {
    HABIT_CREATE: 'Failed to create habit',
    HABIT_DELETE: 'Failed to delete habit',
    HABIT_CHECK: 'Failed to check off habit',
    FETCH_HABITS: 'Failed to load habits',
    FETCH_ANALYTICS: 'Failed to load analytics',
  },
};

export const COLORS = {
  daily: {
    bg: 'bg-blue-100',
    text: 'text-blue-700',
    border: 'border-blue-200',
  },
  weekly: {
    bg: 'bg-purple-100',
    text: 'text-purple-700',
    border: 'border-purple-200',
  },
};