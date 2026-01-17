/**
 * Empty State Component
 * Author: Blessing Oluwapelumi James
 */

import React from 'react';
import { Plus } from 'lucide-react';

export const EmptyState = ({ 
  icon: IconComponent,
  title,
  description,
  actionLabel,
  onAction
}) => {
  return (
    <div className="text-center py-16">
      {/* Icon */}
      <div className="inline-flex items-center justify-center w-20 h-20 bg-gray-100 rounded-full mb-6">
        {IconComponent ? (
          <IconComponent size={40} className="text-gray-400" />
        ) : (
          <span className="text-5xl">📋</span>
        )}
      </div>
      
      {/* Content */}
      <h3 className="text-xl font-semibold text-gray-800 mb-2">
        {title || 'No habits yet'}
      </h3>
      <p className="text-gray-600 mb-6 max-w-md mx-auto">
        {description || 'Start building better habits by creating your first one'}
      </p>
      
      {/* Action Button */}
      {onAction && (
        <button
          onClick={onAction}
          className="btn-primary inline-flex items-center gap-2"
        >
          <Plus size={20} />
          {actionLabel || 'Create your first habit'}
        </button>
      )}
    </div>
  );
};