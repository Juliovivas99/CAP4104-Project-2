# Health Tracker App with Weather Data

A Streamlit-based health tracking application that helps users monitor their daily health metrics while providing real-time weather data to encourage outdoor activities.

## Target Users

This application is specifically designed for:

- Health-conscious individuals aged 18-65
- People who combine indoor and outdoor exercise routines
- Users who want to track daily health metrics
- Individuals who need weather-based activity recommendations
- Users with varying accessibility needs

## Application Goals

1. **Primary Goal**: Help users maintain healthy lifestyle habits by combining health tracking with weather-aware activity recommendations
2. **Specific Objectives**:
   - Provide easy daily health metric tracking
   - Offer real-time weather-based exercise recommendations
   - Visualize health progress over time
   - Support informed decision-making about outdoor activities
   - Ensure accessibility for all users

## Demo Video

Watch our demo on how to use the app:
[Health Tracker App Demo](https://www.youtube.com/watch?v=PEvWauYYfZE)

## Features

- **Daily Health Tracking**

  - Water intake monitoring
  - Calorie consumption logging
  - Exercise minutes tracking
  - Daily progress visualization

- **Weather Integration**

  - Real-time weather data from National Weather Service
  - Location-based weather updates
  - Outdoor activity recommendations
  - Weather-based exercise suggestions

- **Data Visualization**

  - Interactive charts for health metrics
  - Historical data tracking
  - Customizable date range views
  - Progress monitoring

- **Location Features**

  - City and state-based location setting
  - Local weather conditions
  - Nearby fitness locations map
  - Easy location updates

- **Accessibility Features**
  - Dark/Light theme support
  - High contrast options
  - Readable font sizes
  - Keyboard shortcuts

## Setup Instructions

1. Clone this repository:

   ```bash
   git clone https://github.com/Juliovivas99/CAP4104-Project-2.git
   cd CAP4104-Project-2
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Using the App

### Health Tracking

1. Enter your daily metrics:
   - Water intake in liters
   - Calories consumed
   - Exercise minutes
2. Click "Save Daily Entry" to record your progress
3. View your trends in the charts below

### Weather Features

1. Set your location in the sidebar:
   - Enter your city
   - Enter your state (2-letter code)
2. View current weather conditions
3. Get exercise recommendations based on weather
4. Use the refresh button to update weather data

### Customization

- Use the sidebar to:
  - Change themes (Light/Dark)
  - Toggle health tips
  - Adjust history view range
  - Update location settings

## Technical Details

- Built with Streamlit 1.32+
- Python 3.9+ required
- Uses National Weather Service API
- OpenStreetMap for geocoding
- Pandas for data management

## API Integration

The app integrates with:

- National Weather Service API for weather data
- OpenStreetMap's Nominatim API for geocoding
- Both APIs are free and don't require API keys

## Development Notes

- State management using Streamlit's session state
- Cached API responses for better performance
- Responsive design for various screen sizes
- Error handling for API failures

## Future Enhancements

- [ ] Add user authentication
- [ ] Implement data persistence
- [ ] Add more health metrics
- [ ] Include workout suggestions
- [ ] Add social sharing features

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- National Weather Service for weather data
- OpenStreetMap for location services
- Streamlit for the amazing framework
- All contributors and users of the app

## Data Sources and Integration

The application integrates multiple data sources:

### External APIs

1. **National Weather Service API**

   - Real-time weather data
   - Detailed forecasts
   - Location-based weather conditions
   - Format: JSON responses
   - Endpoint: api.weather.gov

2. **OpenStreetMap Nominatim API**
   - Geocoding services
   - Location data
   - Format: JSON responses
   - Endpoint: nominatim.openstreetmap.org

### Internal Data Management

1. **Health Metrics Dataset**

   - Structure: Pandas DataFrame
   - Stored metrics:
     - Water intake (liters)
     - Calories consumed
     - Exercise minutes
   - Format: In-memory data structure
   - Persistence: Session-based storage

2. **Location Data**
   - City and state information
   - Cached coordinates
   - Format: JSON structure
   - Updates: Real-time API integration

## Streamlit Elements Implementation

The application utilizes a wide range of Streamlit components:

### Input Elements

- `st.number_input`: For water, calories, and exercise inputs
- `st.text_input`: For location entry
- `st.slider`: For historical data range selection
- `st.checkbox`: For enabling/disabling features
- `st.selectbox`: For theme selection
- `st.button`: For form submissions and updates

### Display Elements

- `st.metric`: For weather temperature display
- `st.line_chart`: For exercise tracking visualization
- `st.area_chart`: For water intake visualization
- `st.bar_chart`: For calorie tracking
- `st.map`: For displaying nearby locations
- `st.dataframe`: For showing historical data

### Layout Elements

- `st.columns`: For responsive layout
- `st.sidebar`: For settings and controls
- `st.expander`: For collapsible sections
- `st.header`: For section headers
- `st.subheader`: For subsection headers

### Feedback Elements

- `st.success`: For success messages
- `st.error`: For error notifications
- `st.warning`: For warning messages
- `st.info`: For informational alerts
- `st.spinner`: For loading states

### State Management

- `st.session_state`: For preserving data between reruns
- `st.rerun`: For forcing page updates

### Styling Elements

- Custom CSS via `st.markdown`
- Dark/Light theme support
- Responsive design elements

## Application Structure and Flow

### Core Components

```
app/
├── main.py              # Main application entry point
├── requirements.txt     # Project dependencies
├── README.md           # Documentation
└── utils/
    ├── weather.py      # Weather API integration
    ├── health.py       # Health metrics management
    └── visualization.py # Data visualization tools
```

### User Flow

1. **Initial Setup**

   - User enters location
   - App fetches weather data
   - Session state initialized

2. **Daily Tracking**

   - Input health metrics
   - View real-time weather
   - Get activity recommendations

3. **Data Visualization**

   - View progress charts
   - Analyze historical data
   - Track achievements

4. **Settings Management**
   - Theme preferences
   - Location updates
   - Data management

### Error Handling

- API failure recovery
- Input validation
- Data persistence backup
- Graceful degradation
