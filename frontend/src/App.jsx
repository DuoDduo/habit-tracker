/**
 * Main Application Component
 * Author: Blessing Oluwapelumi James
 * Matric No: 92134091
 */

import React, { useState, useMemo } from 'react';
import { Plus } from 'lucide-react';

// Layout
import { Header } from './components/layout/Header';
import { Footer } from './components/layout/Footer';
import { Container } from './components/layout/Container';

// Components
import { Button } from './components/common/Button';
import { Loading } from './components/common/Loading';
import { ErrorMessage } from './components/common/ErrorMessage';
import { HabitList } from './components/habits/HabitList';
import { HabitFilters } from './components/habits/HabitFilters';
import { CreateHabitModal } from './components/habits/CreateHabitModal';
import { AnalyticsDashboard } from './components/analytics/AnalyticsDashboard';

// Hooks
import { useHabits } from './hooks/useHabits';
import { useAnalytics } from './hooks/useAnalytics';
import { useModal } from './hooks/useModal';

function App() {
  // State
  const [activeFilter, setActiveFilter] = useState('all');

  // Custom Hooks
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

  // Filter habits
  const filteredHabits = useMemo(() => {
    if (activeFilter === 'all') return habits;
    return habits.filter((habit) => habit.periodicity === activeFilter);
  }, [habits, activeFilter]);

  // Handlers
  const handleCreateHabit = async (habitData) => {
    await createHabit(habitData);
    await fetchAnalytics(); // Refresh analytics
  };

  const handleDeleteHabit = async (habitId) => {
    await deleteHabit(habitId);
    await fetchAnalytics(); // Refresh analytics
  };

  const handleCheckOffHabit = async (habitId) => {
    await checkOffHabit(habitId);
    await fetchAnalytics(); // Refresh analytics
  };

  const handleRetry = () => {
    fetchHabits();
    fetchAnalytics();
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 flex flex-col">
      {/* Header */}
      <Header />

      {/* Main Content */}
      <main className="flex-1">
        <Container>
          {/* Analytics Dashboard */}
          <section className="mb-8">
            <AnalyticsDashboard
              analytics={analytics}
              loading={analyticsLoading}
              error={analyticsError}
              onRetry={fetchAnalytics}
            />
          </section>

          {/* Actions Bar */}
          <section className="mb-6">
            <div className="flex items-center justify-between gap-4 flex-wrap">
              <div>
                <h2 className="text-2xl font-bold text-gray-800">My Habits</h2>
                <p className="text-gray-600 mt-1">
                  {filteredHabits.length} {activeFilter !== 'all' ? activeFilter : ''} 
                  {filteredHabits.length === 1 ? ' habit' : ' habits'} found
                </p>
              </div>
              <Button
                variant="primary"
                icon={Plus}
                onClick={openModal}
              >
                New Habit
              </Button>
            </div>
          </section>

          {/* Filters */}
          <section className="mb-6">
            <HabitFilters
              activeFilter={activeFilter}
              onFilterChange={setActiveFilter}
            />
          </section>

          {/* Habits List */}
          <section>
            {habitsLoading ? (
              <Loading message="Loading your habits..." />
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
        </Container>
      </main>

      {/* Footer */}
      <Footer />

      {/* Create Habit Modal */}
      <CreateHabitModal
        isOpen={isOpen}
        onClose={closeModal}
        onCreate={handleCreateHabit}
      />
    </div>
  );
}

export default App;