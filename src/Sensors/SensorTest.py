import adafruit_dht as DHT

from board import D26
from time import sleep

sensor = DHT.DHT22(D26, use_pulseio=False)
while True:
    try:
        temp = sensor.temperature
        humidity = sensor.humidity
        print("Temperature is: {.1f} C  Humidity is: {}%".format(temp, humidity))
    except RuntimeError as error:
        print(error.args[0])
    except Exception as error:
        sensor.exit()
        raise error

    sleep(2.0)
