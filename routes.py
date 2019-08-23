"""
Define all routes here
"""
from config import Config
from flask import Blueprint
from flask import request, make_response, render_template

handler = Blueprint('router', __name__)

@handler.route('/')
def index():
    resp = make_response(render_template('index.html',**locals()))
    return resp 


# TODO
# Dito kayo mag aadd ng mga route
# You can edit this file