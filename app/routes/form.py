from flask import Blueprint, render_template, redirect
# Let's get session here too!
from app import dbfuncs
# Make sure to import your form!

bp = Blueprint("form", __name__, url_prefix="/form")

@bp.route('/', methods=('GET', 'POST'))
def form():
   # Instantiate your form! Then DO STUFF!
   # If form validates, add a new car to the session!
   # If form validates, add a new car to the DB! (check dbfuncs 👀)
    info = {
        "title":"NEW CAR FORM!",
        "header":"ADD A NEW CAR 😎"
    }
    cars = dbfuncs.get_all_cars() # RENDER CARS ON FORM!
    owners = dbfuncs.get_all_owners() # RENDER OWNERS SO THEY KNOW WHO CAN OWN A CAR
    return render_template("page.html", info=info, form=form, cars=cars, owners=owners)