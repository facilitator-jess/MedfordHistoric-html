# Medford Historic Properties Website

A modern web application for exploring historic properties in Medford, Massachusetts. Built with Next.js, TypeScript, and Tailwind CSS.

## Features

- **Property Gallery**: Browse 30+ historic properties with photos and details
- **Advanced Search**: Filter by street, architectural style, condition, and construction date
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Property Details**: Expandable cards showing comprehensive property information
- **Modern UI**: Clean, accessible interface with Tailwind CSS

## Data Source

The application uses JSON data extracted from historical property records maintained by the Medford Historical Commission. Each property includes:

- Property information (address, historic name, construction date, etc.)
- Architectural details (style, architect, condition)
- Historical metadata (recorder, organization, date)
- Images (photographs and maps)

## Technology Stack

- **Framework**: Next.js 15 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Data**: JSON files served from `/public/json_data/`

## Getting Started

### Prerequisites

- Node.js 18+ 
- npm or yarn

### Installation

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

3. Open [http://localhost:3000](http://localhost:3000) in your browser

### Build for Production

```bash
npm run build
npm start
```

## Project Structure

```
src/
├── app/                 # Next.js app router pages
├── components/          # React components
│   ├── PropertyCard.tsx
│   └── SearchFilters.tsx
├── lib/                 # Utility functions
│   └── properties.ts
└── types/               # TypeScript type definitions
    └── property.ts
```

## Data Structure

The application expects JSON data in the following format:

```typescript
interface Property {
  filename: string;
  file_path: string;
  metadata: PropertyMetadata;
  property_info: PropertyInfo;
  images: PropertyImage[];
  architectural_description: string;
  historical_narrative: string;
  bibliography: string;
}
```

## Features in Detail

### Search & Filtering
- **Text Search**: Search across property names, addresses, styles, and descriptions
- **Street Filter**: Filter by specific streets (Hillside Avenue, Governors Avenue, etc.)
- **Style Filter**: Filter by architectural style (Colonial Revival, Queen Anne, etc.)
- **Condition Filter**: Filter by property condition (Excellent, Good, Fair)
- **Date Filter**: Filter by construction date range

### Property Cards
- **Image Display**: Shows primary property photo with image count indicator
- **Key Information**: Address, style, construction date, and condition
- **Expandable Details**: Click to show additional information like architect, uses, acreage
- **Condition Indicators**: Color-coded condition badges

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Medford Historical Commission for providing the historical property data
- Next.js team for the excellent framework
- Tailwind CSS for the utility-first styling approach
