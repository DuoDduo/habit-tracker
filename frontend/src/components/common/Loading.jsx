/**
 * Loading Spinner Component
 * Author: Blessing Oluwapelumi James
 */

import React from 'react';

export const Loading = ({ message = 'Loading...', size = 'lg' }) => {
  const sizeClasses = {
    sm: 'h-6 w-6',
    md: 'h-10 w-10',
    lg: 'h-16 w-16',
  };

  return (
    <div className="flex flex-col items-center justify-center py-12">
      <div className={`${sizeClasses[size]} border-4 border-blue-200 border-t-blue-600 rounded-full animate-spin`}></div>
      <p className="mt-4 text-gray-600 font-medium">{message}</p>
    </div>
  );
};