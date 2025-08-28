'use client';

import { useState } from 'react';
import { SearchFilters } from '@/types/property';

interface SearchFilterPanelProps {
  onFiltersChange: (filters: SearchFilters) => void;
  streets: string[];
  styles: string[];
  conditions: string[];
  constructionDates: string[];
}

export default function SearchFilterPanel({
  onFiltersChange,
  streets,
  styles,
  conditions,
  constructionDates
}: SearchFilterPanelProps) {
  const [filters, setFilters] = useState<SearchFilters>({});

  const handleFilterChange = (key: keyof SearchFilters, value: string) => {
    const newFilters = { ...filters, [key]: value || undefined };
    setFilters(newFilters);
    onFiltersChange(newFilters);
  };

  const clearFilters = () => {
    const emptyFilters: SearchFilters = {};
    setFilters(emptyFilters);
    onFiltersChange(emptyFilters);
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md mb-6">
      <h2 className="text-xl font-semibold mb-4 text-gray-800">Search & Filter Properties</h2>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {/* Search Term */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Search
          </label>
          <input
            type="text"
            placeholder="Search by name, address, style..."
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            value={filters.searchTerm || ''}
            onChange={(e) => handleFilterChange('searchTerm', e.target.value)}
          />
        </div>

        {/* Street Filter */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Street
          </label>
          <select
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            value={filters.street || ''}
            onChange={(e) => handleFilterChange('street', e.target.value)}
          >
            <option value="">All Streets</option>
            {streets.map((street) => (
              <option key={street} value={street}>
                {street}
              </option>
            ))}
          </select>
        </div>

        {/* Style Filter */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Architectural Style
          </label>
          <select
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            value={filters.style || ''}
            onChange={(e) => handleFilterChange('style', e.target.value)}
          >
            <option value="">All Styles</option>
            {styles.map((style) => (
              <option key={style} value={style}>
                {style}
              </option>
            ))}
          </select>
        </div>

        {/* Condition Filter */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Condition
          </label>
          <select
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            value={filters.condition || ''}
            onChange={(e) => handleFilterChange('condition', e.target.value)}
          >
            <option value="">All Conditions</option>
            {conditions.map((condition) => (
              <option key={condition} value={condition}>
                {condition}
              </option>
            ))}
          </select>
        </div>

        {/* Construction Date Filter */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Construction Date
          </label>
          <select
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            value={filters.constructionDate || ''}
            onChange={(e) => handleFilterChange('constructionDate', e.target.value)}
          >
            <option value="">All Dates</option>
            {constructionDates.map((date) => (
              <option key={date} value={date}>
                {date}
              </option>
            ))}
          </select>
        </div>

        {/* Clear Filters Button */}
        <div className="flex items-end">
          <button
            onClick={clearFilters}
            className="w-full px-4 py-2 bg-gray-500 text-white rounded-md hover:bg-gray-600 transition-colors"
          >
            Clear Filters
          </button>
        </div>
      </div>
    </div>
  );
}
