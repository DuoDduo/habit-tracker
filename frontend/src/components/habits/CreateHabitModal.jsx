/**
 * Create Habit Modal Component
 * Author: Blessing Oluwapelumi James
 */

import React, { useState } from 'react';
import { Modal } from '../common/Modal';
import { HabitForm } from './HabitForm';

export const CreateHabitModal = ({ isOpen, onClose, onCreate }) => {
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (formData) => {
    setLoading(true);
    try {
      await onCreate(formData);
      onClose();
    } catch (error) {
      console.error('Failed to create habit:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Modal isOpen={isOpen} onClose={onClose} title="Create New Habit" size="md">
      <HabitForm 
        onSubmit={handleSubmit}
        onCancel={onClose}
        loading={loading}
      />
    </Modal>
  );
};