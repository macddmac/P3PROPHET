from flask import Blueprint, render_template

rohanminilab_bp = Blueprint('rohanminilab', __name__,
                            template_folder='templates',)

@rohanminilab_bp.route('/')
def index():
    return render_template("rohanminilab.html")

# Set class
class Car:

    # Initializer
    def init(self, color):
        self.color = color

    # Getter
    def get_color(self):
        return self._color

    # Setter
    def set_color(self, x):
        self._color = x

    @property
    def color(self):
        return self._color


# Object creation
final = Car()

# Setter determines color
final.set_color('White')

# Getter retrieves the color
print(final.get_color())

print(final.color)