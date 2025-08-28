'use client';

import { useState, useEffect } from 'react';
import { Property, SearchFilters } from '@/types/property';
import { loadProperties, filterProperties, getUniqueValues, getStreetNames } from '@/lib/properties';
import SearchFilters from '@/components/SearchFilters';
import PropertyCard from '@/components/PropertyCard';

export default function Home() {
  const [properties, setProperties] = useState<Property[]>([]);
  const [filteredProperties, setFilteredProperties] = useState<Property[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Load properties on component mount
  useEffect(() => {
    async function loadData() {
      try {
        setLoading(true);
        const data = await loadProperties();
        setProperties(data);
        setFilteredProperties(data);
      } catch (err) {
        setError('Failed to load properties');
        console.error(err);
      } finally {
        setLoading(false);
      }
    }

    loadData();
  }, []);

  // Handle filter changes
  const handleFiltersChange = (filters: SearchFilters) => {
    const filtered = filterProperties(properties, filters);
    setFilteredProperties(filtered);
  };

  // Get unique values for filter options
  const streets = getStreetNames(properties);
  const styles = getUniqueValues(properties, 'style_form');
  const conditions = getUniqueValues(properties, 'condition');
  const constructionDates = getUniqueValues(properties, 'construction_date');

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <p className="text-gray-600">Loading historical properties...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <p className="text-red-600 mb-4">{error}</p>
          <button 
            onClick={() => window.location.reload()}
            className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
          >
            Try Again
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <h1 className="text-3xl font-bold text-gray-900">
            Medford Historic Properties
          </h1>
          <p className="mt-2 text-gray-600">
            Explore {properties.length} historic properties in Medford, Massachusetts
          </p>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Search and Filters */}
        <SearchFilters
          onFiltersChange={handleFiltersChange}
          streets={streets}
          styles={styles}
          conditions={conditions}
          constructionDates={constructionDates}
        />

        {/* Results Summary */}
        <div className="mb-6">
          <p className="text-gray-600">
            Showing {filteredProperties.length} of {properties.length} properties
          </p>
        </div>

        {/* Property Grid */}
        {filteredProperties.length === 0 ? (
          <div className="text-center py-12">
            <div className="text-gray-400 text-6xl mb-4">🏠</div>
            <h3 className="text-lg font-medium text-gray-900 mb-2">No properties found</h3>
            <p className="text-gray-600">Try adjusting your search criteria</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {filteredProperties.map((property) => (
              <PropertyCard key={property.filename} property={property} />
            ))}
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="bg-white border-t mt-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <p className="text-center text-gray-600">
            Data from the Medford Historical Commission • Built with Next.js and TypeScript
          </p>
        </div>
      </footer>
    </div>
  );
}
