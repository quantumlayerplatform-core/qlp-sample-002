```
# Weather API

A modern web application built with FastAPI, integrating with the OpenWeatherMap API to fetch weather data.

## Features

- Fetch weather data by city using OpenWeatherMap API.

## Installation

1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment.
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and update the WEATHER_API_KEY with your API key.
6. Run the application: `uvicorn app.main:app --reload`

## API Endpoints

- `GET /weather/{city}` - Get weather data for a specified city.

## Development

The API documentation is available at `http://localhost:8000/docs` when running locally.
```