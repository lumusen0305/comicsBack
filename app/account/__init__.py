from flask import Blueprint

account = Blueprint("account", __name__)
import app.account.views

