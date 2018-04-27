from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_script import Manager, Shell
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
manager = Manager(app)

from app import views, models
