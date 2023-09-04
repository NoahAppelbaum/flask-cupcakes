import os
from flask import Flask, render_template, flash, redirect, jsonify, request
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

@app.get("/api/cupcakes")
def get_all_cupcakes():
    """return json of list of all cupcakes"""

    cupcakes = Cupcake.query.all()

    serialized = [cupcake.serialize() for cupcake in cupcakes]

    return jsonify(cupcakes = serialized)

@app.get("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    """returns json data about particular cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    return jsonify(cupcake = cupcake.serialize())

@app.post("/api/cupcakes")
def add_cupcake():
    """adds a cupcake to the db"""
    flavor = request.json["flavor"]

    size = request.json["size"]

    rating = request.json["rating"]

    image_url = request.json.get("image_url", None)

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating,
                          image_url=image_url)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)
