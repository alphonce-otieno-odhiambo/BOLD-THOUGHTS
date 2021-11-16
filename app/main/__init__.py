from flask import Blueprint
from werkzeug.utils import format_string
main = Blueprint('main', __name__)

from . import views, forms