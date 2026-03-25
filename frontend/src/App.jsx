/**
 * HabitOS v1.0 - Main Application Entry
 * Features: Professional Sidebar Layout, Terminal Hero, and Integrated Analytics
 * Author: Blessing Oluwapelumi James
 * Matric No: 92134091
 */

import React, { useState, useMemo, useEffect } from 'react';
import { Plus, Terminal, Search } from 'lucide-react';

// Layout & Branding
import { Header } from './components/layout/Header';
import { Footer } from './components/layout/Footer';
import { Sidebar } from './components/layout/Sidebar';
import { Hero } from './components/layout/Hero';

// Core Components
import { Loading } from './components/common/Loading';
import { ErrorMessage } from './components/common/ErrorMessage';
import { HabitList } from './components/habits/HabitList';
import { HabitFilters } from './components/habits/HabitFilters';
import { CreateHabitModal } from './components/habits/CreateHabitModal';
import { AnalyticsDashboard } from './components/analytics/AnalyticsDashboard';

// Custom Hooks
import { useHabits } from './hooks/useHabits';
import { useAnalytics } from './hooks/useAnalytics';
import { useModal } from './hooks/useModal';

function App() {
  const [activeFilter, setActiveFilter] = useState('all');
  
  // Custom Hooks Data Fetching
  const {
    habits,
    loading: habitsLoading,
    error: habitsError,
    fetchHabits,
    createHabit,
    deleteHabit,
    checkOffHabit,
  } = useHabits();

  const {
    analytics,
    loading: analyticsLoading,
    error: analyticsError,
    fetchAnalytics,
  } = useAnalytics();

  const { isOpen, openModal, closeModal } = useModal();

  // Filter Logic
  const filteredHabits = useMemo(() => {
    if (activeFilter === 'all') return habits;
    return habits.filter((habit) => habit.periodicity === activeFilter);
  }, [habits, activeFilter]);

  // Unified Action Handlers
  const handleCreateHabit = async (habitData) => {
    await createHabit(habitData);
    await fetchAnalytics();
    closeModal();
  };

  const handleDeleteHabit = async (habitId) => {
    await deleteHabit(habitId);
    await fetchAnalytics();
  };

  const handleCheckOffHabit = async (habitId) => {
    await checkOffHabit(habitId);
    await fetchAnalytics();
  };

  const handleRetry = () => {
    fetchHabits();
    fetchAnalytics();
  };

  return (
    <div className="flex min-h-screen bg-[#F8FAFC] selection:bg-blue-100">
      {/* 1. System Sidebar (Desktop Only) */}
      <Sidebar onCreateClick={openModal} />

      {/* 2. Main Content Stage */}
      <div className="flex-1 flex flex-col min-w-0">
        <Header />

        <main className="flex-1 overflow-y-auto px-4 sm:px-8 py-8">
          <div className="max-w-6xl mx-auto space-y-0">
            
            {/* 3. Hero Terminal Branding */}
            <Hero 
              userName="B.O. James" 
              habitCount={habits.length} 
              onCreateClick={openModal} 
            />

            {/* 4. Analytics Data Visualization */}
            <section className="mb-12 animate-in fade-in slide-in-from-bottom-6 duration-700">
              <div className="flex items-center gap-3 mb-6 px-2">
                <div className="h-5 w-1 bg-blue-600 rounded-full" />
                <h2 className="text-xl font-black text-gray-900 tracking-tight uppercase tracking-[0.1em] text-sm">
                  System Telemetry
                </h2>
              </div>
              <AnalyticsDashboard
                analytics={analytics}
                loading={analyticsLoading}
                error={analyticsError}
                onRetry={fetchAnalytics}
              />
            </section>

            {/* 5. Content Control Bar (Filters) */}
            <section className="sticky top-0 z-30 bg-[#F8FAFC]/90 backdrop-blur-xl py-4 mb-8 border-b border-gray-100 flex flex-col md:flex-row justify-between items-center gap-6">
              <div className="flex items-center gap-4 w-full md:w-auto">
                 <div className="p-2 bg-white rounded-xl border border-gray-200 shadow-sm">
                   <Terminal size={18} className="text-gray-400" />
                 </div>
                 <div>
                   <h3 className="text-lg font-bold text-gray-900 leading-none">Habit Nodes</h3>
                   <p className="text-xs text-gray-400 font-mono mt-1">Status: Monitoring {filteredHabits.length} items</p>
                 </div>
              </div>

              <div className="flex items-center gap-3 w-full md:w-auto">
                <HabitFilters
                  activeFilter={activeFilter}
                  onFilterChange={setActiveFilter}
                />
              </div>
            </section>

            {/* 6. Habits Execution Grid */}
            <section className="pb-24">
              {habitsLoading ? (
                <div className="flex flex-col items-center justify-center py-20 gap-4">
                   <div className="w-10 h-10 border-4 border-blue-600 border-t-transparent rounded-full animate-spin" />
                   <p className="text-sm font-mono text-gray-400 animate-pulse">Decrypting local SQLite storage...</p>
                </div>
              ) : habitsError ? (
                <ErrorMessage message={habitsError} onRetry={handleRetry} />
              ) : (
                <HabitList
                  habits={filteredHabits}
                  onCheckOff={handleCheckOffHabit}
                  onDelete={handleDeleteHabit}
                  onCreateClick={openModal}
                />
              )}
            </section>
          </div>
        </main>
        
        <Footer />
      </div>

      {/* Global Modals */}
      <CreateHabitModal
        isOpen={isOpen}
        onClose={closeModal}
        onCreate={handleCreateHabit}
      />
    </div>
  );
}

export default App;