from flask import Blueprint

comic = Blueprint("comic", __name__)
import app.comic.views

