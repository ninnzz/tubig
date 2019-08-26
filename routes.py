"""=
Define all routes here
"""
from config import Config
from flask import Blueprint
from flask import request, make_response, render_template

<<<<<<< HEAD
handler = Blueprint("router", __name__)


@handler.route("/")
@handler.route("/home")
def home_feed():
	return render_template('index.html')

@handler.route("/about")
def about_us():
	return render_template('about_us.html')
=======
from models import db, User, Stats

handler = Blueprint('router', __name__)
>>>>>>> 89d93566849c03c3a858032dc2e5b19aa3809523



# TODO
# Dito kayo mag aadd ng mga route
# You can edit this file