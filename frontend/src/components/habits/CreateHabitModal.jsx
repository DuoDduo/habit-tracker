/**
 * Create Habit Modal Component
 * Refined for Professional UX/UI
 * Author: Blessing Oluwapelumi James
 */

import React, { useState, useCallback } from 'react';
import { Modal } from '../common/Modal';
import { HabitForm } from './HabitForm';
import { AlertCircle, CheckCircle2 } from 'lucide-react'; // Example icon library

export const CreateHabitModal = ({ isOpen, onClose, onCreate }) => {
  const [status, setStatus] = useState('idle'); // idle | loading | success | error
  const [errorMessage, setErrorMessage] = useState('');

  const handleSubmit = async (formData) => {
    setStatus('loading');
    setErrorMessage('');
    
    try {
      await onCreate(formData);
      setStatus('success');
      
      // Brief delay so user sees the success state before auto-closing
      setTimeout(() => {
        onClose();
        setStatus('idle');
      }, 1500);
    } catch (error) {
      setStatus('error');
      setErrorMessage(error.message || 'Something went wrong. Please try again.');
    }
  };

  const handleClose = useCallback(() => {
    if (status === 'loading') return; // Prevent closing during API calls
    setStatus('idle');
    onClose();
  }, [status, onClose]);

  return (
    <Modal 
      isOpen={isOpen} 
      onClose={handleClose} 
      title="Create New Habit"
      // Responsive sizing: full screen on mobile, centered modal on desktop
      className="max-w-lg w-[95%] sm:w-full mx-auto transition-all duration-300"
    >
      <div className="p-1 sm:p-4">
        {/* Progress/Status Indicator */}
        {status === 'error' && (
          <div className="mb-4 p-3 bg-red-50 border border-red-200 text-red-700 rounded-lg flex items-center gap-2 text-sm animate-in fade-in">
            <AlertCircle size={18} />
            {errorMessage}
          </div>
        )}

        {status === 'success' && (
          <div className="mb-4 p-3 bg-green-50 border border-green-200 text-green-700 rounded-lg flex items-center gap-2 text-sm">
            <CheckCircle2 size={18} />
            Habit created successfully!
          </div>
        )}

        <p className="text-gray-500 text-sm mb-6">
          Set your goals and track your progress. Small steps lead to big changes.
        </p>

        <HabitForm 
          onSubmit={handleSubmit}
          onCancel={handleClose}
          loading={status === 'loading'}
          // Pass status down if you want to change button text/styles in the form
          status={status} 
        />
      </div>
    </Modal>
  );
};