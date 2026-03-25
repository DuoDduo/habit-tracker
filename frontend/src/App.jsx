/**
 * HabitOS v1.0 - Main Application Entry
 * Features: Professional Sidebar Layout, Terminal Hero, and Integrated Analytics
 * Author: Blessing Oluwapelumi James
 * Matric No: 92134091
 */

import React, { useState, useMemo, useEffect } from 'react';
import { Plus, Terminal, Search, ArrowRight, Activity, Sparkles, Target } from 'lucide-react';

// Layout & Branding
import { Header } from './components/layout/Header';
import { Footer } from './components/layout/Footer';
import { Sidebar } from './components/layout/Sidebar';

/// Core Components
import { Login } from './components/auth/Login';
import { Loading } from './components/common/Loading';
import { ErrorMessage } from './components/common/ErrorMessage';
import { HabitList } from './components/habits/HabitList';
import { HabitFilters } from './components/habits/HabitFilters';
import { CreateHabitModal } from './components/habits/CreateHabitModal';
import { AnalyticsDashboard } from './components/analytics/AnalyticsDashboard';
import { Landing } from './components/marketing/Landing';
import { GrowthIllustration } from './components/common/Illustrations';

// Custom Hooks
import { useHabits } from './hooks/useHabits';
import { useAnalytics } from './hooks/useAnalytics';
import { useModal } from './hooks/useModal';

function App() {
  const [activeFilter, setActiveFilter] = useState('all');
  const [activeView, setActiveView] = useState('dashboard'); // 'dashboard' | 'analytics'
  const [user, setUser] = useState(null);
  const [showLogin, setShowLogin] = useState(false);
  const [isInitializing, setIsInitializing] = useState(true);
  
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

  // Load User from LocalStorage
  useEffect(() => {
    const savedUser = localStorage.getItem('habit_os_user');
    if (savedUser) {
      setUser(JSON.parse(savedUser));
    }
    setIsInitializing(false);
  }, []);

  // Filter Logic
  const filteredHabits = useMemo(() => {
    if (activeFilter === 'all') return habits;
    return habits.filter((habit) => habit.periodicity === activeFilter);
  }, [habits, activeFilter]);

  // Unified Action Handlers
  const handleLogin = (userData) => {
    localStorage.setItem('habit_os_user', JSON.stringify(userData));
    setUser(userData);
  };

  const handleLogout = () => {
    localStorage.removeItem('habit_os_user');
    setUser(null);
    setShowLogin(false);
    setActiveView('dashboard');
  };

  const handleViewChange = (view) => {
    setActiveView(view);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

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

  if (isInitializing) {
    return <div className="min-h-screen bg-slate-50 flex items-center justify-center">
      <div className="w-10 h-10 border-4 border-blue-600 border-t-transparent rounded-full animate-spin" />
    </div>;
  }

  if (!user) {
    return showLogin ? (
      <Login onLogin={handleLogin} onBack={() => setShowLogin(false)} />
    ) : (
      <Landing onGetStarted={() => setShowLogin(true)} />
    );
  }

  return (
    <div className="flex min-h-screen bg-[#F8FAFC] selection:bg-blue-100">
      {/* 1. System Sidebar (Desktop Only) */}
      <Sidebar 
        user={user} 
        activeView={activeView}
        onViewChange={handleViewChange}
        onLogout={handleLogout} 
        onCreateClick={openModal} 
      />

      {/* 2. Main Content Stage */}
      <div className="flex-1 flex flex-col min-w-0">
        <Header 
          user={user} 
          activeView={activeView}
          onViewChange={handleViewChange}
          onLogout={handleLogout} 
        />

        <main className="flex-1 overflow-y-auto px-4 sm:px-8 py-8">
          <div className="max-w-6xl mx-auto space-y-0">
            
            {activeView === 'dashboard' ? (
              <>
                {/* 3. Hero Branding */}
                <section className="relative bg-gradient-to-br from-blue-50 to-white text-slate-800 p-8 sm:p-14 rounded-[2.5rem] mb-12 overflow-hidden border border-blue-100 shadow-xl shadow-blue-500/5 animate-fade-in-up">
                  {/* Background Accents */}
                  <div className="absolute inset-0 z-0">
                    <div className="absolute top-0 right-0 w-1/3 h-full bg-blue-100/30 blur-3xl rounded-full translate-x-1/2 -translate-y-1/2 animate-pulse-soft" />
                    <div className="absolute bottom-0 left-0 w-1/3 h-full bg-indigo-100/20 blur-3xl rounded-full -translate-x-1/2 translate-y-1/2 animate-pulse-soft delay-1000" />
                  </div>

                  <div className="relative z-10 flex flex-col md:flex-row items-center justify-between gap-10">
                    <div className="flex-1 space-y-8 text-center md:text-left">
                      <div className="space-y-3">
                         <div className="inline-flex items-center gap-2 text-blue-600 font-black text-[10px] uppercase tracking-[0.3em] bg-blue-50 px-3 py-1 rounded-full border border-blue-100">
                           <Sparkles size={12} />
                           Your Growth Journey
                         </div>
                         
                         <h1 className="text-4xl sm:text-6xl font-black tracking-tighter leading-[1.1]">
                           Ready to thrive,
                           <span className="block text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-indigo-600">
                             {user?.name || 'User'}?
                           </span>
                         </h1>
                      </div>

                      <div className="space-y-6">
                        <p className="text-slate-500 text-lg sm:text-xl leading-relaxed max-w-xl font-medium">
                          Build better routines, track your progress, and <span className="text-blue-600 font-bold">achieve your goals</span> with the HabitOS personal dashboard.
                        </p>

                        <div className="flex flex-wrap justify-center md:justify-start gap-4">
                          <button 
                            onClick={openModal}
                            className="flex items-center gap-3 px-10 py-5 bg-blue-600 hover:bg-blue-700 text-white rounded-2xl font-black text-sm transition-all shadow-xl shadow-blue-600/30 group active:scale-95"
                          >
                            Add Your First Habit
                            <Plus size={18} className="group-hover:rotate-90 transition-transform" />
                          </button>
                        </div>
                      </div>
                    </div>

                    {/* Animated Illustration Container */}
                    <div className="hidden lg:block w-72 h-72 rounded-full relative animate-float">
                       <GrowthIllustration className="w-full h-full" />
                       <Sparkles size={40} className="absolute top-10 right-10 text-blue-300 animate-pulse" />
                    </div>
                  </div>
                </section>

                {/* 4. Progress Overview Section */}
                <section className="sticky top-0 z-30 bg-[#F8FAFC]/90 backdrop-blur-xl py-4 mb-8 border-b border-gray-100 flex flex-col md:flex-row justify-between items-center gap-6 animate-fade-in-up [animation-delay:200ms]">
                  <div className="flex items-center gap-4 w-full md:w-auto">
                     <div className="p-3 bg-blue-600 rounded-2xl shadow-lg shadow-blue-600/20">
                       <Target size={20} className="text-white" />
                     </div>
                     <div>
                       <h3 className="text-xl font-black text-gray-900 leading-none">Your Habits</h3>
                       <p className="text-xs text-gray-400 font-bold mt-1 uppercase tracking-wider">Tracking {filteredHabits.length} habits today</p>
                     </div>
                  </div>

                  <div className="flex items-center gap-3 w-full md:w-auto">
                    <HabitFilters
                      activeFilter={activeFilter}
                      onFilterChange={setActiveFilter}
                    />
                  </div>
                </section>

                {/* 5. Habits Execution Grid */}
                <section className="pb-24 animate-fade-in-up [animation-delay:400ms]">
                  {habitsLoading ? (
                    <div className="flex flex-col items-center justify-center py-20 gap-4">
                       <div className="w-10 h-10 border-4 border-blue-600 border-t-transparent rounded-full animate-spin" />
                       <p className="text-sm font-bold text-slate-400 animate-pulse">Syncing your progress with HabitOS...</p>
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
              </>
            ) : (
              /* Dedicated Analytics View */
              <section className="mb-12 animate-in fade-in slide-in-from-bottom-6 duration-700 pb-24">
                <AnalyticsDashboard
                  analytics={analytics}
                  loading={analyticsLoading}
                  error={analyticsError}
                  onRetry={fetchAnalytics}
                />
              </section>
            )}
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