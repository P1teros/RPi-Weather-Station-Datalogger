import adafruit_dht
import time
import board

dhtDevice = adafruit_dht.DHT22(board.D4)

while True:
        try:
                #odczyt temp i wilgotnosci
                temp = dhtDevice.temperature
                humidity = dhtDevice.humidity
                print(f"Temp: {temp:.1f}C")
                print(f"Humidity: {humidity:.1f}%")
          
        except RuntimeError as error:
                print(f"Error: {error.args[0]}; retrying...")
                time.sleep(2.0)
                continue
          
        except Exception as error:
                dhtDevice.exit()
                raise error

        time.sleep(30.0)

