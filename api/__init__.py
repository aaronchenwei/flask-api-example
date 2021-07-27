from flask import Blueprint
api = Blueprint('api', __name__)

from .app import *
from .errors import *
from .health import *
