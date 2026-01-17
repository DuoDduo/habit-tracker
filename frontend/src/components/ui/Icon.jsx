// npx tailwindcss init -p

/**
 * Icon Wrapper Component
 * Author: Blessing Oluwapelumi James
 */

import React from 'react';

export const Icon = ({ 
  icon: IconComponent, 
  size = 24, 
  className = '',
  ...props 
}) => {
  return (
    <IconComponent 
      size={size} 
      className={className}
      {...props}
    />
  );
};