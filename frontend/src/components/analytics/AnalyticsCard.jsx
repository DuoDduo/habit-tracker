/**
 * Detailed Analytics Card Component
 * Author: Blessing Oluwapelumi James
 */

import React from 'react';
import { Card } from '../common/Card';
import { TrendingUp, TrendingDown, Minus } from 'lucide-react';

export const AnalyticsCard = ({ title, data, type = 'info' }) => {
  const getIcon = () => {
    switch (type) {
      case 'success':
        return <TrendingUp className="text-green-600" size={20} />;
      case 'warning':
        return <Minus className="text-yellow-600" size={20} />;
      case 'danger':
        return <TrendingDown className="text-red-600" size={20} />;
      default:
        return null;
    }
  };

  const getBorderColor = () => {
    switch (type) {
      case 'success':
        return 'border-l-green-500';
      case 'warning':
        return 'border-l-yellow-500';
      case 'danger':
        return 'border-l-red-500';
      default:
        return 'border-l-blue-500';
    }
  };

  return (
    <Card className={`border-l-4 ${getBorderColor()}`}>
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-semibold text-gray-800">{title}</h3>
        {getIcon()}
      </div>
      <div className="text-gray-600">
        {data}
      </div>
    </Card>
  );
};