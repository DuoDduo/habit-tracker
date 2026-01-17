/**
 * Validation Utilities
 * Author: Blessing Oluwapelumi James
 */

/**
 * Validate habit name
 * @param {string} name - Habit name
 * @returns {Object} { isValid: boolean, error: string }
 */
export const validateHabitName = (name) => {
  if (!name || name.trim().length === 0) {
    return { isValid: false, error: 'Habit name is required' };
  }
  if (name.length > 255) {
    return { isValid: false, error: 'Habit name must be less than 255 characters' };
  }
  return { isValid: true, error: null };
};

/**
 * Validate periodicity
 * @param {string} periodicity - Periodicity value
 * @returns {Object} { isValid: boolean, error: string }
 */
export const validatePeriodicity = (periodicity) => {
  if (!periodicity) {
    return { isValid: false, error: 'Periodicity is required' };
  }
  if (!['daily', 'weekly'].includes(periodicity)) {
    return { isValid: false, error: 'Periodicity must be daily or weekly' };
  }
  return { isValid: true, error: null };
};

/**
 * Validate habit form data
 * @param {Object} formData - Form data
 * @returns {Object} { isValid: boolean, errors: Object }
 */
export const validateHabitForm = (formData) => {
  const errors = {};
  
  const nameValidation = validateHabitName(formData.name);
  if (!nameValidation.isValid) {
    errors.name = nameValidation.error;
  }
  
  const periodicityValidation = validatePeriodicity(formData.periodicity);
  if (!periodicityValidation.isValid) {
    errors.periodicity = periodicityValidation.error;
  }
  
  return {
    isValid: Object.keys(errors).length === 0,
    errors,
  };
};