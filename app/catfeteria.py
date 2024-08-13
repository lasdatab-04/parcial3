
from flask import (
    Blueprint, render_template
)


bp = Blueprint('catfeteria', __name__, url_prefix='/catfeteria')

@bp.route('/', methods=('GET', 'POST'))
def index():

    return render_template('catfeteria/index1.html')

@bp.route('/index1', methods=('GET', 'POST'))
def index1():

    return render_template('catfeteria/exit.html')

@bp.route('/exit', methods=('GET', 'POST'))
def exit():

    return render_template('catfeteria/Menu2.html')

@bp.route('/Menu2', methods=('GET', 'POST'))
def Menu2():

    return render_template('catfeteria/Reserva.html')



