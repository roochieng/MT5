import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask import Flask
from dotenv import load_dotenv
from flask_login import LoginManager
from flask_migrate import Migrate
import logging



app = Flask(__name__)

app.secret_key = os.urandom(24)


load_dotenv()

# Access the DATABASE_URL environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True
handler = logging.FileHandler('app.log')
app.logger.addHandler(handler)


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
 