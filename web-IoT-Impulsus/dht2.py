# Eine unsaubere Version von dht_read.py ohne den peewee ORM


import sqlite3
import time

import Adafruit_DHT



    conn = sqlite3.connect('IoT.db')
    c = conn.cursor()


    c.execute('SELECT name, dht_type, pin FROM dhtsensor')
    sensors = []
    for row in c:
        name, dht_type, pin = row
        print('Configuring sensor: {0} of type: {1} on pin: {2}'.format(name, dht_type, pin))

        if dht_type == 'DHT22':
            dht_type = Adafruit_DHT.DHT22
        elif dht_type == 'DHT11':
            dht_type = Adafruit_DHT.DHT11
        else:
            raise RuntimeError('Unknown sensor type: {0}'.format(dht_type))

        sensors.append((name, dht_type, pin))


    while True:

        reading_time = int(time.time())

        for s in sensors:
            name, dht_type, pin = s
            humidity, temperature = Adafruit_DHT.read_retry(dht_type, pin)
            print('Read sensor: {0} humidity: {1:0.2}% temperature: {2:0.2}C'.format(name, humidity, temperature))


            c.execute('INSERT INTO readings VALUES (?, ?, ?)',
                      (reading_time, '{0} Humidity'.format(name), humidity))
            c.execute('INSERT INTO readings VALUES (?, ?, ?)',
                      (reading_time, '{0} Temperature'.format(name), temperature))
            conn.commit()
        time.sleep(2.0)
