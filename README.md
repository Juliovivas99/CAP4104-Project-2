# Health Tracker App with Weather Data

A Streamlit-based health tracking application that helps users monitor their daily health metrics while providing real-time weather data to encourage outdoor activities.

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
