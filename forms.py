from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Optional, URL, Length


class AddCupcakeForm(FlaskForm):
    """Form for adding a cupcake"""
    flavor = StringField("Cupcake Flavor",
                       validators=[InputRequired(), Length(max=50)]
                       )
    size = StringField("Size",
                validators=[InputRequired(), Length(max=15)]
                )

    rating = IntegerField("Rating",
                validators=[InputRequired()]
                )


    image_url = StringField("Image URL",
                    validators=[Optional(), URL(), Length(max=500)]
                )
