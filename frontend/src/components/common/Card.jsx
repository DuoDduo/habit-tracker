/**
 * Reusable Card Component
 * Author: Blessing Oluwapelumi James
 */

import React from 'react';

export const Card = ({ 
  children, 
  className = '', 
  hover = false,
  padding = 'p-6',
  ...props 
}) => {
  const hoverClasses = hover ? 'hover:shadow-lg' : '';
  
  return (
    <div
      className={`card ${padding} ${className}`}
      {...props}
    >
      {children}
    </div>
  );
};