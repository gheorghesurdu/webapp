import datetime
import time

from gpiozero import CPUTemperature

import model

data = model.DHTData()

cpu = CPUTemperature()

try:
    while True:

        reading_time = datetime.datetime.now()

        print('CPU Temperature : {0}C'.format(cpu.temperature))


        data.add_cpu_reading(time=reading_time, name='CPU', value='{0}C'.format(cpu.temperature))


        time.sleep(2.0)

finally:
    data.close()
