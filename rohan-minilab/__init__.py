from flask import Blueprint, render_template

rohanminilab_bp = Blueprint('rohanminilab', __name__,
                            template_folder='templates',)

@rohanminilab_bp.route('/')
def index():
    return render_template("rohanminilab.html")