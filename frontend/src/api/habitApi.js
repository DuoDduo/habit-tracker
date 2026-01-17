/**
 * API Client for Habit Tracker Backend
 * Author: Blessing Oluwapelumi James
 * Matric No: 92134091
 */

import axios from 'axios';
import { API_BASE_URL } from '../utils/constants';

// Create axios instance
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for logging
api.interceptors.request.use(
  (config) => {
    console.log(`[API] ${config.method.toUpperCase()} ${config.url}`);
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor for error handling
api.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    console.error('[API Error]', error.response?.data || error.message);
    return Promise.reject(error);
  }
);

/**
 * Habit API
 */
export const habitApi = {
  // Get all habits
  getAllHabits: async () => {
    const response = await api.get('/habits');
    return response.data;
  },

  // Get single habit
  getHabit: async (habitId) => {
    const response = await api.get(`/habits/${habitId}`);
    return response.data;
  },

  // Create habit
  createHabit: async (habitData) => {
    const response = await api.post('/habits', habitData);
    return response.data;
  },

  // Delete habit
  deleteHabit: async (habitId) => {
    const response = await api.delete(`/habits/${habitId}`);
    return response.data;
  },

  // Check off habit
  checkOffHabit: async (habitId, timestamp = null) => {
    const response = await api.post(`/habits/${habitId}/check-off`, 
      timestamp ? { timestamp } : {}
    );
    return response.data;
  },
};

/**
 * Analytics API
 */
export const analyticsApi = {
  // Get longest streak
  getLongestStreak: async () => {
    const response = await api.get('/analytics/longest-streak');
    return response.data;
  },

  // Get habits by periodicity
  getHabitsByPeriodicity: async (period) => {
    const response = await api.get('/analytics/by-periodicity', {
      params: { period },
    });
    return response.data;
  },

  // Get tracked habits
  getTrackedHabits: async () => {
    const response = await api.get('/analytics/tracked-habits');
    return response.data;
  },

  // Get struggling habits
  getStrugglingHabits: async (threshold = 3) => {
    const response = await api.get('/analytics/struggling', {
      params: { threshold },
    });
    return response.data;
  },

  // Get analytics summary
  getAnalyticsSummary: async () => {
    const response = await api.get('/analytics/summary');
    return response.data;
  },
};

export default api;