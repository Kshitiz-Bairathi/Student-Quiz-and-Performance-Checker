from flask import Flask, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'default_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///access.db"
db = SQLAlchemy(app)

# Push the context manually once
app.app_context().push()

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# Custom unauthorized handler
@login_manager.unauthorized_handler
def unauthorized():
    flash("Please log in First to access the page", 'danger')
    return redirect(url_for('Main.home'))

from FlaskMIS.Admin.routes import Admin
from FlaskMIS.Main.routes import Main
from FlaskMIS.Student.routes import Student

app.register_blueprint(Admin)
app.register_blueprint(Main)
app.register_blueprint(Student)