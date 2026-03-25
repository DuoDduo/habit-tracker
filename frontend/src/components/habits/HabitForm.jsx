/**
 * Habit Form Component
 * Refined for Professional UX/UI & Responsiveness
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
    if (errors[name]) {
      setErrors((prev) => ({ ...prev, [name]: null }));
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const validation = validateHabitForm(formData);
    if (!validation.isValid) {
      setErrors(validation.errors);
      return;
    }
    await onSubmit(formData);
  };

  // Shared Tailwind classes for a unified look
  const inputBaseClasses = `
    w-full px-4 py-2.5 rounded-lg border transition-all duration-200 outline-none
    text-gray-900 placeholder-gray-400
    focus:ring-2 focus:ring-offset-1
  `;

  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      {/* Habit Name */}
      <div className="group">
        <label htmlFor="name" className="block text-sm font-medium text-gray-700 mb-1.5 transition-colors group-focus-within:text-blue-600">
          Habit Name <span className="text-red-400">*</span>
        </label>
        <input
          type="text"
          id="name"
          name="name"
          value={formData.name}
          onChange={handleChange}
          placeholder="e.g., Morning Meditation"
          className={`${inputBaseClasses} ${
            errors.name 
              ? 'border-red-300 focus:border-red-500 focus:ring-red-100' 
              : 'border-gray-300 focus:border-blue-500 focus:ring-blue-100'
          }`}
        />
        {errors.name && (
          <p className="mt-1.5 text-xs font-medium text-red-500 animate-in slide-in-from-top-1">
            {errors.name}
          </p>
        )}
      </div>

      {/* Description */}
      <div>
        <label htmlFor="specification" className="block text-sm font-medium text-gray-700 mb-1.5">
          Description <span className="text-gray-400 font-normal">(Optional)</span>
        </label>
        <textarea
          id="specification"
          name="specification"
          value={formData.specification}
          onChange={handleChange}
          placeholder="Describe your goal or motivation..."
          rows="3"
          className={`${inputBaseClasses} border-gray-300 focus:border-blue-500 focus:ring-blue-100 resize-none`}
        />
      </div>

      {/* Periodicity Selection */}
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-3">
          How often? <span className="text-red-400">*</span>
        </label>
        {/* Responsive Grid: 1 col on tiny screens, 2 cols on small+ */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
          {PERIODICITY_OPTIONS.map((option) => {
            const isSelected = formData.periodicity === option.value;
            return (
              <label
                key={option.value}
                className={`
                  relative flex items-center p-4 rounded-xl border-2 cursor-pointer transition-all duration-200
                  ${isSelected 
                    ? 'border-blue-600 bg-blue-50/50 shadow-sm ring-1 ring-blue-600' 
                    : 'border-gray-100 bg-white hover:border-gray-200 hover:bg-gray-50'
                  }
                `}
              >
                <input
                  type="radio"
                  name="periodicity"
                  value={option.value}
                  checked={isSelected}
                  onChange={handleChange}
                  className="sr-only" // Hide native radio but keep accessible
                />
                <div className="flex flex-col">
                  <div className="flex items-center gap-2">
                    <span className="text-xl opacity-90">{option.icon}</span>
                    <span className={`font-bold ${isSelected ? 'text-blue-900' : 'text-gray-700'}`}>
                      {option.label}
                    </span>
                  </div>
                  <p className="text-xs text-gray-500 mt-1 leading-relaxed">
                    {option.value === 'daily' ? 'Keep the streak alive every day' : 'A steady pace once a week'}
                  </p>
                </div>
                {/* Visual Checkmark for selected state */}
                {isSelected && (
                  <div className="absolute top-2 right-2 text-blue-600">
                    <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                    </svg>
                  </div>
                )}
              </label>
            );
          })}
        </div>
      </div>

      {/* Action Buttons */}
      <div className="flex flex-col-reverse sm:flex-row gap-3 mt-8 pt-6 border-t border-gray-100">
        <Button
          type="button"
          variant="secondary"
          onClick={onCancel}
          disabled={loading}
          className="w-full sm:w-1/3 py-3 font-medium text-gray-600 hover:bg-gray-100"
        >
          Cancel
        </Button>
        <Button
          type="submit"
          variant="primary"
          loading={loading}
          className="w-full sm:flex-1 py-3 font-bold shadow-lg shadow-blue-200 hover:shadow-blue-300 transition-shadow"
        >
          {loading ? 'Creating...' : 'Start this Habit'}
        </Button>
      </div>
    </form>
  );
};