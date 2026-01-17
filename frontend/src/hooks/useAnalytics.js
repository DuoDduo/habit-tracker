/**
 * Custom Hook for Analytics
 * Author: Blessing Oluwapelumi James
 */

import { useState, useEffect, useCallback } from 'react';
import { analyticsApi } from '../api/habitApi';
import toast from 'react-hot-toast';
import { MESSAGES } from '../utils/constants';

export const useAnalytics = () => {
  const [analytics, setAnalytics] = useState({
    longestStreak: 0,
    totalHabits: 0,
    dailyCount: 0,
    weeklyCount: 0,
    activeStreaks: 0,
    brokenHabits: 0,
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch analytics
  const fetchAnalytics = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);
      const summary = await analyticsApi.getAnalyticsSummary();
      setAnalytics(summary);
    } catch (err) {
      setError(err.message);
      toast.error(MESSAGES.ERROR.FETCH_ANALYTICS);
    } finally {
      setLoading(false);
    }
  }, []);

  // Load analytics on mount
  useEffect(() => {
    fetchAnalytics();
  }, [fetchAnalytics]);

  return {
    analytics,
    loading,
    error,
    fetchAnalytics,
  };
};