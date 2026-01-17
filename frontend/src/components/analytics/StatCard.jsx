/**
 * Statistics Card Component
 * Author: Blessing Oluwapelumi James
 */

import React from 'react';
import { Card } from '../common/Card';

export const StatCard = ({ 
  icon: IconComponent, 
  label, 
  value, 
  color = 'blue',
  subtitle 
}) => {
  const colorClasses = {
    blue: 'bg-blue-100 text-blue-600',
    green: 'bg-green-100 text-green-600',
    purple: 'bg-purple-100 text-purple-600',
    orange: 'bg-orange-100 text-orange-600',
    red: 'bg-red-100 text-red-600',
  };

  const textColorClasses = {
    blue: 'text-blue-600',
    green: 'text-green-600',
    purple: 'text-purple-600',
    orange: 'text-orange-600',
    red: 'text-red-600',
  };

  return (
    <Card hover>
      <div className="flex items-center gap-4">
        <div className={`${colorClasses[color]} p-3 rounded-lg`}>
          <IconComponent size={28} />
        </div>
        <div className="flex-1">
          <p className="text-sm text-gray-600 font-medium">{label}</p>
          <p className={`text-3xl font-bold ${textColorClasses[color]}`}>
            {value}
          </p>
          {subtitle && (
            <p className="text-xs text-gray-500 mt-1">{subtitle}</p>
          )}
        </div>
      </div>
    </Card>
  );
};