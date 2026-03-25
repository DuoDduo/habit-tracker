import React from 'react';

/**
 * GrowthIllustration - A high-impact visual for the App Hero
 */
export const GrowthIllustration = ({ className = "" }) => (
  <svg 
    viewBox="0 0 400 400" 
    fill="none" 
    xmlns="http://www.w3.org/2000/svg" 
    className={className}
  >
    <defs>
      <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stopColor="#3B82F6" stopOpacity="0.2" />
        <stop offset="100%" stopColor="#6366F1" stopOpacity="0.05" />
      </linearGradient>
      <linearGradient id="glow" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stopColor="#3B82F6" stopOpacity="0.6" />
        <stop offset="100%" stopColor="#6366F1" stopOpacity="0.1" />
      </linearGradient>
    </defs>
    
    {/* Background Glow */}
    <circle cx="200" cy="200" r="150" fill="url(#grad1)" />
    
    {/* The Path */}
    <path 
      d="M200 350C200 350 250 300 250 250C250 200 150 180 150 130C150 80 200 50 200 50" 
      stroke="#3B82F6" 
      strokeWidth="4" 
      strokeLinecap="round" 
      strokeDasharray="8 12"
      className="animate-pulse"
    />
    
    {/* Achievement Nodes */}
    <g className="animate-float">
      <rect x="230" y="230" width="40" height="40" rx="12" fill="white" shadow="0 10px 15px rgba(0,0,0,0.1)" />
      <path d="M242 250L248 256L258 244" stroke="#3B82F6" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" />
      
      <rect x="130" y="150" width="40" height="40" rx="12" fill="white" />
      <path d="M142 170L148 176L158 164" stroke="#3B82F6" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" />
      
      <rect x="220" y="80" width="40" height="40" rx="12" fill="white" />
      <path d="M232 100L238 106L248 94" stroke="#3B82F6" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" />
    </g>

    {/* The Peak */}
    <circle cx="200" cy="50" r="15" fill="#3B82F6" className="animate-pulse" />
    <circle cx="200" cy="50" r="25" stroke="#3B82F6" strokeOpacity="0.2" strokeWidth="2" />
  </svg>
);

/**
 * LandingIllustration - A sophisticated dashboard preview illustration
 */
export const LandingIllustration = ({ className = "" }) => (
  <svg 
    viewBox="0 0 500 400" 
    fill="none" 
    xmlns="http://www.w3.org/2000/svg" 
    className={className}
  >
    <rect x="50" y="50" width="400" height="300" rx="40" fill="white" stroke="#EFF6FF" strokeWidth="2" />
    
    {/* Header Bars */}
    <rect x="80" y="80" width="120" height="12" rx="6" fill="#F1F5F9" />
    <rect x="220" y="80" width="80" height="12" rx="6" fill="#F1F5F9" />
    
    {/* Grid Content */}
    <rect x="80" y="120" width="160" height="100" rx="24" fill="#EBF5FF" className="animate-pulse" />
    <rect x="260" y="120" width="160" height="100" rx="24" fill="#EEF2FF" className="animate-pulse" style={{ animationDelay: '0.5s' }} />
    
    {/* Chart Area */}
    <rect x="80" y="240" width="340" height="80" rx="24" fill="#F8FAFC" />
    <path 
      d="M100 300L140 280L180 290L220 260L260 270L300 250L340 265L380 255" 
      stroke="#3B82F6" 
      strokeWidth="4" 
      strokeLinecap="round" 
      strokeLinejoin="round" 
    />
    
    {/* Floating Decoration */}
    <circle cx="430" cy="100" r="20" fill="#3B82F6" fillOpacity="0.1" />
    <circle cx="430" cy="100" r="8" fill="#3B82F6" />
  </svg>
);
