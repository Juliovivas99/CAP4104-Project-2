import streamlit as st
import pandas as pd
import numpy as np
import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import json
import time

# Load environment variables
load_dotenv()

# App configuration
st.set_page_config(
    page_title="Health Tracker App",
    page_icon="🏃‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'health_data' not in st.session_state:
    st.session_state.health_data = pd.DataFrame(
        columns=['date', 'water_intake', 'calories', 'exercise_minutes']
    )

if 'location' not in st.session_state:
    st.session_state.location = {
        'city': 'New York',
        'state': 'NY'
    }

if 'coordinates' not in st.session_state:
    st.session_state.coordinates = None

if 'weather_data' not in st.session_state:
    st.session_state.weather_data = None

# Geocoding function
def get_coordinates(city, state, force_refresh=False):
    # Return cached coordinates if available and not forcing refresh
    if not force_refresh and st.session_state.coordinates is not None:
        return st.session_state.coordinates

    try:
        # Using OpenStreetMap's Nominatim API
        search_query = f"{city}, {state}, USA"
        headers = {
            'User-Agent': 'HealthTrackerApp/1.0',
        }
        url = f"https://nominatim.openstreetmap.org/search?q={search_query}&format=json&limit=1"
        
        # Add a small delay to respect rate limits
        time.sleep(1)
        
        response = requests.get(url, headers=headers)
        data = response.json()
        
        if data and len(data) > 0:
            coords = {
                'lat': float(data[0]['lat']),
                'lon': float(data[0]['lon'])
            }
            # Cache the coordinates
            st.session_state.coordinates = coords
            return coords
        else:
            st.error(f"Could not find coordinates for {city}, {state}")
            return None
    except Exception as e:
        st.error(f"Error in geocoding: {str(e)}")
        return None

# Weather API integration
def get_weather(lat, lon, force_refresh=False):
    # Return cached weather data if available and not forcing refresh
    if not force_refresh and st.session_state.weather_data is not None:
        return st.session_state.weather_data

    try:
        # Add a small delay to respect rate limits
        time.sleep(1)
        
        # First, get the grid endpoint for the location
        headers = {
            'User-Agent': '(Health Tracker App, contact@healthtracker.com)',
            'Accept': 'application/json'
        }
        points_url = f"https://api.weather.gov/points/{lat:.4f},{lon:.4f}"
        points_response = requests.get(points_url, headers=headers)
        points_data = points_response.json()
        
        if 'properties' not in points_data:
            st.error("Unable to get weather grid point")
            return None
            
        # Get location information
        location_info = {
            'city': points_data['properties'].get('relativeLocation', {}).get('properties', {}).get('city', 'Unknown City'),
            'state': points_data['properties'].get('relativeLocation', {}).get('properties', {}).get('state', 'Unknown State')
        }
            
        # Get the forecast URL from the points response
        forecast_url = points_data['properties']['forecast']
        forecast_response = requests.get(forecast_url, headers=headers)
        forecast_data = forecast_response.json()
        
        # Get current period's forecast
        current_period = forecast_data['properties']['periods'][0]
        
        weather_data = {
            'temp': current_period['temperature'],
            'condition': current_period['shortForecast'],
            'description': current_period['detailedForecast'],
            'wind_speed': current_period['windSpeed'],
            'wind_direction': current_period['windDirection'],
            'location': location_info
        }
        
        # Cache the weather data
        st.session_state.weather_data = weather_data
        return weather_data
    except Exception as e:
        st.error(f"Error fetching weather data: {str(e)}")
        return None

# Wireframe Layout
"""
# 🏃‍♂️ Health Tracker App
Track your daily health metrics and get personalized recommendations based on weather conditions.
"""

# Sidebar for user preferences
with st.sidebar:
    st.header("Settings")
    
    # Location input
    st.subheader("📍 Location Settings")
    new_city = st.text_input("City", value=st.session_state.location['city'])
    new_state = st.text_input("State (2-letter code)", value=st.session_state.location['state'], max_chars=2)
    
    if st.button("Update Location"):
        if len(new_state) == 2:  # Ensure state is a 2-letter code
            # Clear cached data when location changes
            st.session_state.coordinates = None
            st.session_state.weather_data = None
            
            st.session_state.location = {
                'city': new_city,
                'state': new_state.upper()
            }
            st.success("Location updated!")
            # Force a rerun to update all components
            st.rerun()
        else:
            st.error("Please enter a valid 2-letter state code")
    
    # Refresh weather data button
    if st.button("🔄 Refresh Weather"):
        st.session_state.weather_data = None
        st.rerun()
    
    st.markdown("---")
    
    # Theme selection
    theme = st.selectbox(
        "Choose Theme",
        ["Light", "Dark"],
        key="theme"
    )
    
    # Enable/disable health tips
    show_tips = st.checkbox("Show Health Tips", value=True)
    
    # Historical data range
    days_to_view = st.slider(
        "Days of History to View",
        min_value=1,
        max_value=30,
        value=7
    )

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.header("Daily Health Log")
    
    # Health metrics input
    water = st.number_input("Water Intake (liters)", 0.0, 10.0, step=0.1)
    if water > 5.0:
        st.warning("⚠️ High water intake detected. Make sure this is accurate.")
    
    calories = st.number_input("Calories Consumed", 0, 5000, step=50)
    if calories > 3500:
        st.warning("⚠️ High calorie intake detected. Make sure this is accurate.")
    
    exercise = st.number_input("Exercise Minutes", 0, 300, step=5)
    
    # Submit button
    if st.button("Save Daily Entry"):
        new_entry = pd.DataFrame([{
            'date': datetime.now().strftime('%Y-%m-%d'),
            'water_intake': water,
            'calories': calories,
            'exercise_minutes': exercise
        }])
        
        st.session_state.health_data = pd.concat(
            [st.session_state.health_data, new_entry],
            ignore_index=True
        )
        st.success("✅ Daily health metrics saved successfully!")

with col2:
    st.header("🌤️ Weather & Activity")
    
    # Location display
    current_location = f"{st.session_state.location['city']}, {st.session_state.location['state']}"
    st.subheader(f"📍 {current_location}")
    
    # Get coordinates and weather data
    if st.session_state.coordinates is None:
        with st.spinner("Fetching location data..."):
            coords = get_coordinates(st.session_state.location['city'], st.session_state.location['state'])
    else:
        coords = st.session_state.coordinates
    
    if coords:
        if st.session_state.weather_data is None:
            with st.spinner("Fetching weather data..."):
                weather_data = get_weather(coords['lat'], coords['lon'])
        else:
            weather_data = st.session_state.weather_data
            
        if weather_data:
            st.metric("Temperature", f"{weather_data['temp']}°F")
            st.write(f"Condition: {weather_data['condition']}")
            st.write(f"Wind: {weather_data['wind_speed']} {weather_data['wind_direction']}")
            
            # Exercise recommendation based on weather
            if ("Clear" in weather_data['condition'] or "Sunny" in weather_data['condition']) and \
               weather_data['temp'] > 50 and weather_data['temp'] < 85:
                st.success("👍 Great weather for outdoor exercise!")
            elif "Rain" in weather_data['condition'] or "Snow" in weather_data['condition'] or \
                 weather_data['temp'] < 32 or weather_data['temp'] > 90:
                st.warning("🏠 Weather conditions suggest indoor activities today.")
            else:
                st.info("🌤️ Moderate weather conditions - use your judgment for outdoor activities.")
            
            # Detailed forecast
            with st.expander("See detailed forecast"):
                st.write(weather_data['description'])

# Health guidelines
with st.expander("📋 Health Guidelines"):
    st.info("""
    Daily Recommendations:
    - Water: 2-3 liters
    - Calories: 2000-2500 (varies by individual)
    - Exercise: 30-60 minutes
    """)

# Display historical data
st.header("📈 Health Trends")

if not st.session_state.health_data.empty:
    # Filter data for selected date range
    recent_data = st.session_state.health_data.tail(days_to_view)
    
    # Display metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Water Intake")
        st.area_chart(recent_data.set_index('date')['water_intake'])
    
    with col2:
        st.subheader("Exercise Minutes")
        st.line_chart(recent_data.set_index('date')['exercise_minutes'])
    
    with col3:
        st.subheader("Calories Consumed")
        st.bar_chart(recent_data.set_index('date')['calories'])

# Map with nearby fitness locations
st.header("Nearby Fitness Locations")

# Update map based on current location
if coords:
    locations = pd.DataFrame({
        'lat': [
            coords['lat'],
            coords['lat'] + 0.01,
            coords['lat'] - 0.01
        ],
        'lon': [
            coords['lon'],
            coords['lon'] + 0.01,
            coords['lon'] - 0.01
        ],
        'name': ['Current Location', 'Local Gym', 'Community Center']
    })
    st.map(locations)
else:
    st.error("Unable to display map - location coordinates not found")

# Health tips
if show_tips:
    st.header("💡 Daily Health Tips")
    tips = [
        "Take regular breaks from sitting",
        "Stay hydrated throughout the day",
        "Include both cardio and strength training",
        "Get at least 7-8 hours of sleep",
        "Practice mindful eating"
    ]
    tip_of_the_day = tips[datetime.now().day % len(tips)]
    st.info(f"Tip of the Day: {tip_of_the_day}")

# Footer with accessibility note
st.markdown("""
---
💡 **Accessibility Features**:
- Use keyboard shortcuts (press '?' to view)
- Adjust text size in browser settings
- High contrast theme available
""")

# Apply theme
if st.session_state.theme == "Dark":
    st.markdown("""
        <style>
        .stApp {
            background-color: #1E1E1E;
            color: #FFFFFF;
        }
        </style>
    """, unsafe_allow_html=True) 