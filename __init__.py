from flask import Flask
from flask_admin import Admin

app = Flask('module1')
admin = Admin(app)

import module1.views
