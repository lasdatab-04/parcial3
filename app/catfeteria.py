
from flask import (
    Blueprint, render_template
)

from app.db import get_db

bp = Blueprint('catfeteria', __name__, url_prefix='/catfeteria')

@bp.route('/', methods=('GET', 'POST'))
def index():

    return render_template('catfeteria/index1.html')
