# RPi-Weather-Station-Datalogger
An embedded IoT system for real-time temperature and humidity monitoring using Raspberry Pi, DHT22 sensor, and an LCD 1602 display. The project features local data logging to a SQLite database
## Features
* **Real-Time Data Collection:** Reads temperature and humidity using the DHT22 sensor.
* **Fault Tolerance:** Includes built-in error handling (`try-except`) to ignore sensor connection drops or timing issues, ensuring database integrity.
* **Local Data Logging:** Automatically logs valid data with exact timestamps into a lightweight SQLite database (`pogoda.db`).
* **Headless Operation:** Designed to run in the background as a continuous data logger.

## Hardware Components
* **Raspberry Pi** (Model B Rev 2, 2011.12)
* **DHT22** Temperature & Humidity Sensor
* **Breadboard & Jumper Wires**
* *(Work in Progress)* **LCD 1602 Display** for local data visualization.

## Database Schema
The data is stored locally in `weather_data.db` using the following structure:

| Column | Type | Description |
| :--- | :--- | :--- |
| `data_godzina` | TEXT | Timestamp of the reading (YYYY-MM-DD HH:MM:SS) |
| `temperatura` | REAL | Temperature in Celsius (°C) |
| `wilgotnosc` | REAL | Relative humidity (%) |

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/RPi-Weather-Station-Datalogger.git](https://github.com/YOUR_USERNAME/RPi-Weather-Station-Datalogger.git)
   cd RPi-Weather-Station-Datalogger
