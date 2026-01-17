/**
 * Custom Hook for Habits Management
 * Author: Blessing Oluwapelumi James
 */

import { useState, useEffect, useCallback } from 'react';
import { habitApi } from '../api/habitApi';
import toast from 'react-hot-toast';
import { MESSAGES } from '../utils/constants';

export const useHabits = () => {
  const [habits, setHabits] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch all habits
  const fetchHabits = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await habitApi.getAllHabits();
      setHabits(data);
    } catch (err) {
      setError(err.message);
      toast.error(MESSAGES.ERROR.FETCH_HABITS);
    } finally {
      setLoading(false);
    }
  }, []);

  // Create habit
  const createHabit = useCallback(async (habitData) => {
    try {
      const newHabit = await habitApi.createHabit(habitData);
      setHabits((prev) => [newHabit, ...prev]);
      toast.success(MESSAGES.SUCCESS.HABIT_CREATED);
      return newHabit;
    } catch (err) {
      toast.error(MESSAGES.ERROR.HABIT_CREATE);
      throw err;
    }
  }, []);

  // Delete habit
  const deleteHabit = useCallback(async (habitId) => {
    try {
      await habitApi.deleteHabit(habitId);
      setHabits((prev) => prev.filter((h) => h.habit_id !== habitId));
      toast.success(MESSAGES.SUCCESS.HABIT_DELETED);
    } catch (err) {
      toast.error(MESSAGES.ERROR.HABIT_DELETE);
      throw err;
    }
  }, []);

  // Check off habit
  const checkOffHabit = useCallback(async (habitId) => {
    try {
      const updatedHabit = await habitApi.checkOffHabit(habitId);
      setHabits((prev) =>
        prev.map((h) => (h.habit_id === habitId ? updatedHabit : h))
      );
      toast.success(MESSAGES.SUCCESS.HABIT_CHECKED);
      return updatedHabit;
    } catch (err) {
      toast.error(MESSAGES.ERROR.HABIT_CHECK);
      throw err;
    }
  }, []);

  // Load habits on mount
  useEffect(() => {
    fetchHabits();
  }, [fetchHabits]);

  return {
    habits,
    loading,
    error,
    fetchHabits,
    createHabit,
    deleteHabit,
    checkOffHabit,
  };
};