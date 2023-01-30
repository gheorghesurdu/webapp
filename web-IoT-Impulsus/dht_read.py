import datetime
import time

import Adafruit_DHT

import model


data = model.DHTData()


data.define_sensor('DHT1', Adafruit_DHT.DHT11, 18)
data.define_sensor('DHT2', Adafruit_DHT.DHT22, 25)

try:
    while True:

        reading_time = datetime.datetime.now()

        for sensor in data.get_sensors():

            humidity, temperature = Adafruit_DHT.read_retry(sensor.dht_type, sensor.pin)
            print('Read sensor: {0} humidity: {1:0.2f}% temperature: {2:0.2f}C'.format(sensor.name, humidity, temperature))

            data.add_reading(time=reading_time, name='{0} Humidity'.format(sensor.name), value=humidity)
            data.add_reading(time=reading_time, name='{0} Temperature'.format(sensor.name), value=temperature)

        time.sleep(2.0)
finally:

    data.close()
