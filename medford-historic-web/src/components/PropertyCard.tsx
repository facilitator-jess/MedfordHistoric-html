'use client';

import { Property } from '@/types/property';
import { useState } from 'react';

interface PropertyCardProps {
  property: Property;
}

export default function PropertyCard({ property }: PropertyCardProps) {
  const [showDetails, setShowDetails] = useState(false);
  const info = property.property_info;

  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
      {/* Image */}
      {property.images.length > 0 && (
        <div className="relative h-48 bg-gray-200">
          <img
            src={property.images[0].src}
            alt={property.images[0].alt || `Photo of ${info.historic_name || info.address}`}
            className="w-full h-full object-cover"
            onError={(e) => {
              const target = e.target as HTMLImageElement;
              target.style.display = 'none';
            }}
          />
          {property.images.length > 1 && (
            <div className="absolute top-2 right-2 bg-black bg-opacity-50 text-white px-2 py-1 rounded text-sm">
              +{property.images.length - 1} more
            </div>
          )}
        </div>
      )}

      {/* Content */}
      <div className="p-6">
        {/* Title */}
        <h3 className="text-xl font-semibold text-gray-800 mb-2">
          {info.historic_name || info.address}
        </h3>

        {/* Address */}
        {info.address && (
          <p className="text-gray-600 mb-3">
            📍 {info.address}
          </p>
        )}

        {/* Key Details */}
        <div className="space-y-2 mb-4">
          {info.style_form && (
            <div className="flex items-center text-sm">
              <span className="font-medium text-gray-700 w-20">Style:</span>
              <span className="text-gray-600">{info.style_form}</span>
            </div>
          )}
          
          {info.construction_date && (
            <div className="flex items-center text-sm">
              <span className="font-medium text-gray-700 w-20">Built:</span>
              <span className="text-gray-600">{info.construction_date}</span>
            </div>
          )}
          
          {info.condition && (
            <div className="flex items-center text-sm">
              <span className="font-medium text-gray-700 w-20">Condition:</span>
              <span className={`px-2 py-1 rounded text-xs ${
                info.condition.toLowerCase().includes('excellent') 
                  ? 'bg-green-100 text-green-800'
                  : info.condition.toLowerCase().includes('good')
                  ? 'bg-blue-100 text-blue-800'
                  : 'bg-yellow-100 text-yellow-800'
              }`}>
                {info.condition}
              </span>
            </div>
          )}
        </div>

        {/* Toggle Details */}
        <button
          onClick={() => setShowDetails(!showDetails)}
          className="text-blue-600 hover:text-blue-800 text-sm font-medium"
        >
          {showDetails ? 'Hide Details' : 'Show Details'}
        </button>

        {/* Expanded Details */}
        {showDetails && (
          <div className="mt-4 pt-4 border-t border-gray-200 space-y-3">
            {info.architect_builder && (
              <div>
                <span className="font-medium text-gray-700">Architect/Builder:</span>
                <p className="text-gray-600">{info.architect_builder}</p>
              </div>
            )}
            
            {info.uses && (
              <div>
                <span className="font-medium text-gray-700">Uses:</span>
                <p className="text-gray-600">{info.uses}</p>
              </div>
            )}
            
            {info.outbuildings && (
              <div>
                <span className="font-medium text-gray-700">Outbuildings:</span>
                <p className="text-gray-600">{info.outbuildings}</p>
              </div>
            )}
            
            {info.acreage && (
              <div>
                <span className="font-medium text-gray-700">Acreage:</span>
                <p className="text-gray-600">{info.acreage}</p>
              </div>
            )}
            
            {property.metadata.recorded_by && (
              <div>
                <span className="font-medium text-gray-700">Recorded by:</span>
                <p className="text-gray-600">{property.metadata.recorded_by}</p>
              </div>
            )}
            
            {property.metadata.date && (
              <div>
                <span className="font-medium text-gray-700">Date:</span>
                <p className="text-gray-600">{property.metadata.date}</p>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
