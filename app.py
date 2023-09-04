import os
from flask import Flask, render_template, flash, redirect, jsonify, request
# from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, Cupcake, db, DEFAULT_IMAGE_URL
# from sqlalchemy.exc import  DataError

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
    try:
        flavor = request.json["flavor"]

        size = request.json["size"]

        rating = request.json["rating"]

        image_url = request.json.get("image_url", None)

        new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating,
                          image_url=image_url)

    #Return bad request response on missing or bad data
    except KeyError:
        error_message = {"Error": "Incorrect or missing data"}
        return (jsonify(error_message), 400)

    # Worry about more exceptions... later this week!
    # except DataError:
    #     error_message = {"Error": "Incorrect data types"}
    #     return (jsonify(error_message), 400)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)


@app.patch("/api/cupcakes/<int:cupcake_id>")
def update_cupcake(cupcake_id):
    """Updates cupcake record in db"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    update_data = request.json

    for key in update_data:
        if update_data.get(key):
            setattr(cupcake, key, update_data[key])

    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())

@app.delete("/api/cupcakes/<int:cupcake_id>")
def delete_cupcake(cupcake_id):
    """Deletes cupcake from db"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(deleted = cupcake_id)
