/**
 * Habit Form Component
 * Author: Blessing Oluwapelumi James
 */

import React, { useState } from 'react';
import { Button } from '../common/Button';
import { PERIODICITY_OPTIONS } from '../../utils/constants';
import { validateHabitForm } from '../../utils/validators';

export const HabitForm = ({ onSubmit, onCancel, loading = false }) => {
  const [formData, setFormData] = useState({
    name: '',
    specification: '',
    periodicity: 'daily',
  });
  const [errors, setErrors] = useState({});

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
    // Clear error for this field
    if (errors[name]) {
      setErrors((prev) => ({ ...prev, [name]: null }));
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    // Validate
    const validation = validateHabitForm(formData);
    if (!validation.isValid) {
      setErrors(validation.errors);
      return;
    }

    // Submit
    await onSubmit(formData);
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      {/* Name */}
      <div>
        <label htmlFor="name" className="block text-sm font-semibold text-gray-700 mb-2">
          Habit Name *
        </label>
        <input
          type="text"
          id="name"
          name="name"
          value={formData.name}
          onChange={handleChange}
          placeholder="e.g., Drink Water"
          className={`input ${errors.name ? 'border-red-500 focus:ring-red-500' : ''}`}
        />
        {errors.name && (
          <p className="mt-1 text-sm text-red-600">{errors.name}</p>
        )}
      </div>

      {/* Specification */}
      <div>
        <label htmlFor="specification" className="block text-sm font-semibold text-gray-700 mb-2">
          Description
        </label>
        <textarea
          id="specification"
          name="specification"
          value={formData.specification}
          onChange={handleChange}
          placeholder="What do you want to achieve?"
          rows="3"
          className="input"
        />
        <p className="mt-1 text-xs text-gray-500">Optional: Add more details about your habit</p>
      </div>

      {/* Periodicity */}
      <div>
        <label htmlFor="periodicity" className="block text-sm font-semibold text-gray-700 mb-2">
          Periodicity *
        </label>
        <div className="grid grid-cols-2 gap-3">
          {PERIODICITY_OPTIONS.map((option) => (
            <label
              key={option.value}
              className={`flex items-center gap-3 p-4 border-2 rounded-lg cursor-pointer transition ${
                formData.periodicity === option.value
                  ? 'border-blue-600 bg-blue-50'
                  : 'border-gray-200 hover:border-gray-300'
              }`}
            >
              <input
                type="radio"
                name="periodicity"
                value={option.value}
                checked={formData.periodicity === option.value}
                onChange={handleChange}
                className="w-4 h-4 text-blue-600"
              />
              <div>
                <div className="flex items-center gap-2">
                  <span className="text-xl">{option.icon}</span>
                  <span className="font-semibold text-gray-800">{option.label}</span>
                </div>
                <p className="text-xs text-gray-500 mt-1">
                  {option.value === 'daily' ? 'Track every day' : 'Track once per week'}
                </p>
              </div>
            </label>
          ))}
        </div>
        {errors.periodicity && (
          <p className="mt-1 text-sm text-red-600">{errors.periodicity}</p>
        )}
      </div>

      {/* Actions */}
      <div className="flex gap-3 mt-6 pt-4 border-t">
        <Button
          type="button"
          variant="secondary"
          onClick={onCancel}
          disabled={loading}
          className="flex-1"
        >
          Cancel
        </Button>
        <Button
          type="submit"
          variant="primary"
          loading={loading}
          className="flex-1"
        >
          Create Habit
        </Button>
      </div>
    </form>
  );
};