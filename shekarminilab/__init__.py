from flask import Blueprint, render_template
from flask import request
from shekarminilab.minilab import Exercise

shekarminilab_bp = Blueprint('shekarminilab', __name__,
                            template_folder='templates')

@shekarminilab_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template("shekarminilab.html", Exercise=Exercise(int(request.form.get("series"))))
    return render_template("shekarminilab.html", Exercise=Exercise(1))

