from flask import Blueprint, render_template

shekarminilab_bp = Blueprint('shekarminilab', __name__,
                            template_folder='templates',)

@shekarminilab_bp.route('/')
def index():
    return render_template("shekarminilab.html")