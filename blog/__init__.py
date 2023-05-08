from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config 

app = Flask(__name__) #Istanza Flask
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app,db)#permette di modificare la struttura db in maniera semplice

with app.app_context():
    if db.engine.url.drivername == 'sqlite':
        migrate.init_app(app,db,render_as_batch=True)#render_as_batch == venire in contro alle limitazione di questo DB
    else :
        migrate.init_app(app,db)

    

from blog import models,routes
