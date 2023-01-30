from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView

import model



app = Flask(__name__)
app.config['SECRET_KEY'] = 'mosfet'

app.config['FLASK_ADMIN_FLUID_LAYOUT'] = True
app.config['MODEL'] = model.DHTData()



admin = Admin(app, name='IoT-Impulsus GmbH', template_mode='bootstrap4', url='/')
admin.add_view(ModelView(model.DHTSensor))
admin.add_view(ModelView(model.SensorReading))
admin.add_view(ModelView(model.CPUTemperature))


app.run(debug = True)
