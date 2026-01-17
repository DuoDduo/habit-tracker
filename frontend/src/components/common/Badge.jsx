/**
 * Reusable Badge Component
 * Author: Blessing Oluwapelumi James
 */

import React from 'react';
import { COLORS } from '../../utils/constants';

export const Badge = ({ 
  children, 
  type = 'daily',
  className = '' 
}) => {
  // Use your existing constant logic
  const colors = COLORS[type?.toLowerCase()] || COLORS.daily;
  
  return (
    <span
      className={`
        ${colors.bg} 
        ${colors.text} 
        /* Match the border to the text color with low opacity for a modern look */
        border border-current/10 
        px-2.5 
        py-0.5 
        rounded-md 
        text-[10px] 
        font-mono 
        font-bold 
        uppercase 
        tracking-wider 
        inline-flex 
        items-center 
        justify-center
        ${className}
      `}
    >
      {children}
    </span>
  );
};