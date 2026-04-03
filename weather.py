import sqlite3
from datetime import datetime
import adafruit_dht
import time
import board

dhtDevice = adafruit_dht.DHT22(board.D4)
DB_NAME = "weather_data.db"

def init_db():
    """tworzenie bazy i tabeli"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        '''
            CREATE TABLE IF NOT EXISTS measurements(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                temperature REAL,
                humidity REAL
            )
        '''
    )
    conn.commit()
    conn.close()
    print("Baza danych zainicjalizowana.")

def log_to_db(temp, hum):
    """zapisywanie pomiarow do bazy danych"""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(
            "INSERT INTO measurements (timestamp, temperature, humidity) VALUES (?, ?, ?)",
            (now, temp, hum)
        )
        conn.commit()
        conn.close()
        print(f"[{now}] Zapisano: {temp}*C, {hum}%")
    except sqlite3.Error as e:
        print(f"Błąd SQLite: {e}")

init_db()

while True:
    try:
        #odczyt temp i wilgotnosci
        temp = dhtDevice.temperature
        humidity = dhtDevice.humidity

        if temp is not None and humidity is not None:
            print(f"Temp: {temp:.1f}C")
            print(f"Humidity: {humidity:.1f}%")

            log_to_db(temp, humidity)

    except RuntimeError as error:
        print(f"Error: {error.args[0]}; retrying...")
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)
