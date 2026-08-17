# OpenWeather Data Pipeline

A Python application structured to pull, parse, and log data using the OpenWeather API.

## Features

- **Key Management:** Reads API authentication tokens from a localized `config.json` file.
- **Data Logging:** Dumps responses into a .txt file (`weather_data.txt`).

## Technologies Used

- **Language:** Python 3.x
- **Network Dependency:** `requests`
- **Data Serialization:** `json`
- **Data Source:** OpenWeather API

## Getting Started

### Prerequisites

- Python 3.8 or higher.
- A free API key from OpenWeather.

### Installation & Run

1. Clone the repository:
   ```bash
   git clone https://github.com
   ```
2. Install the necessary network library:
   ```bash
   pip install requests
   ```
3. Create a `src/config.json` file in the project directory and format it like this:
   ```json
   {
     "API_WEATHER_KEY": "your_actual_openweather_api_key_here"
     "API_WEATHER_KEY": "your_openweather_key_here"
   }
   ```
4. Run the application:
   ```bash
   python main.py
   ```

## Usage

1. Run the script from your terminal.
2. Enter the target city when prompted.
3. View the data in the console or `src/weather_data.txt`.