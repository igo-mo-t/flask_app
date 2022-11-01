from flask import Blueprint
main = Blueprint('main', __name__)
# main = Blueprint('main', __name__, template_folder='templates_dir', static_folder='static_dir')
from . import views