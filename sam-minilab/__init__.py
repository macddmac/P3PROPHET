from flask import Blueprint, render_template

samminilab_bp = Blueprint('samminilab', __name__,
                            template_folder='templates',)

@samminilab_bp.route('/')
def index():
    return render_template("samminilab.html")