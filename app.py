import os
from flask import Flask, render_template, flash, redirect, jsonify
# from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, Cupcake, db, DEFAULT_IMAGE_URL

"""Flask app for Cupcakes"""
app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///cupcakes")


connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# toolbar = DebugToolbarExtension(app)
