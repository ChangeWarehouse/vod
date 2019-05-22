from flask import Blueprint

admin = Blueprint('admin',__name__)

from app.controller import user,login