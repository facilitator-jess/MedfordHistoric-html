import { Property, SearchFilters } from '@/types/property';

export async function loadProperties(): Promise<Property[]> {
  try {
    const response = await fetch('/json_data/all_properties.json');
    if (!response.ok) {
      throw new Error('Failed to load properties');
    }
    return await response.json();
  } catch (error) {
    console.error('Error loading properties:', error);
    return [];
  }
}

export function filterProperties(properties: Property[], filters: SearchFilters): Property[] {
  return properties.filter(property => {
    const info = property.property_info;
    
    // Search term filter
    if (filters.searchTerm) {
      const searchLower = filters.searchTerm.toLowerCase();
      const searchableText = [
        info.address,
        info.historic_name,
        info.style_form,
        info.architect_builder,
        property.architectural_description,
        property.historical_narrative
      ].join(' ').toLowerCase();
      
      if (!searchableText.includes(searchLower)) {
        return false;
      }
    }
    
    // Street filter
    if (filters.street && info.address) {
      if (!info.address.toLowerCase().includes(filters.street.toLowerCase())) {
        return false;
      }
    }
    
    // Style filter
    if (filters.style && info.style_form) {
      if (!info.style_form.toLowerCase().includes(filters.style.toLowerCase())) {
        return false;
      }
    }
    
    // Condition filter
    if (filters.condition && info.condition) {
      if (!info.condition.toLowerCase().includes(filters.condition.toLowerCase())) {
        return false;
      }
    }
    
    // Construction date filter
    if (filters.constructionDate && info.construction_date) {
      if (!info.construction_date.includes(filters.constructionDate)) {
        return false;
      }
    }
    
    return true;
  });
}

export function getUniqueValues(properties: Property[], field: keyof Property['property_info']): string[] {
  const values = properties
    .map(p => p.property_info[field])
    .filter(Boolean) as string[];
  
  return [...new Set(values)].sort();
}

export function getStreetNames(properties: Property[]): string[] {
  const streets = properties
    .map(p => p.property_info.address)
    .filter((address): address is string => Boolean(address))
    .map(address => {
      const parts = address.split(' ');
      return parts.slice(2).join(' '); // Skip house number and street number
    });
  
  return [...new Set(streets)].sort();
}
