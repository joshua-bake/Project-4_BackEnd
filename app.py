from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from config.environment import db_URI
from flask_cors import CORS


app = Flask(__name__)


@app.route("/hello", methods=["GET"])
def hello():
    return "Hello World!"


app.config["SQLALCHEMY_DATABASE_URI"] = db_URI

CORS(app)

db = SQLAlchemy(app)

marsh = Marshmallow(app)

bcrypt = Bcrypt(app)

from controllers import users, decks, cards

app.register_blueprint(users.router, url_prefix="/api")
app.register_blueprint(cards.router, url_prefix="/api")
app.register_blueprint(decks.router, url_prefix="/api")
