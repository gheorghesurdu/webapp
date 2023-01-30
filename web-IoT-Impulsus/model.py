from peewee import *


db = SqliteDatabase('IoT.db', check_same_thread=False)



class DHTSensor(Model):
    name = CharField()
    dht_type = CharField()
    pin = IntegerField()

    class Meta:
        database = db


class SensorReading(Model):
    time = DateTimeField()
    name = CharField()
    value = FloatField()

    class Meta:
        database = db

class CPUTemperature(Model):
    time = DateTimeField()
    name = 'CPU'
    value = FloatField()

    class Meta:
        database = db


class DHTData(object):

    def __init__(self):

        db.connect()

        db.create_tables([DHTSensor, SensorReading, CPUTemperature], safe=True)

    def define_sensor(self, name, dht_type, pin):

        DHTSensor.get_or_create(name=name, dht_type=dht_type, pin=pin)

    def get_sensors(self):

        return DHTSensor.select()

    def get_recent_readings(self, name, limit=30):

        return SensorReading.select() \
                            .where(SensorReading.name == name) \
                            .order_by(SensorReading.time.desc()) \
                            .limit(limit)

    def get_recent_cpu_readings(self, name, limit=30):
        return CPUTemperature.select() \
                            .where(CPUTemperature.name == name) \
                            .order_by(CPUTemperature.time.desc()) \
                            .limit(limit)

    def add_reading(self, time, name, value):

        SensorReading.create(time=time, name=name, value=value)

    def add_cpu_reading(self, time, name, value):

        CPUTemperature.create(time=time, name=name, value=value)

    def close(self):

        db.close()
