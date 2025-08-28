export interface PropertyImage {
  src: string;
  alt: string;
  style: string;
}

export interface PropertyMetadata {
  recorded_by?: string;
  organization?: string;
  date?: string;
}

export interface PropertyInfo {
  assessors_number?: string;
  usgs_quad?: string;
  area?: string;
  form_number?: string;
  town_city?: string;
  place?: string;
  address?: string;
  historic_name?: string;
  uses?: string;
  construction_date?: string;
  source?: string;
  style_form?: string;
  architect_builder?: string;
  exterior_material?: string;
  outbuildings?: string;
  major_alterations?: string;
  condition?: string;
  moved?: string;
  acreage?: string;
  setting?: string;
}

export interface Property {
  filename: string;
  file_path: string;
  metadata: PropertyMetadata;
  property_info: PropertyInfo;
  images: PropertyImage[];
  architectural_description: string;
  historical_narrative: string;
  bibliography: string;
}

export interface SearchFilters {
  street?: string;
  style?: string;
  condition?: string;
  constructionDate?: string;
  searchTerm?: string;
}
