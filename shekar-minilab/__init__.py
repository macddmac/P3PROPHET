from flask import Blueprint, render_template

shekarminilab_bp = Blueprint('shekarminilab', __name__,
                            template_folder='templates',)

@shekarminilab_bp.route('/')
def index():
    return render_template("shekarminilab.html")

# defining classes
class place:
    def starting(user, place=0, points=0):
        user.place = place
        user.points = points

    # getter for weight
    # set variable
    def get_place(user):
        return user.place

    # getter for height
    # set variable
    def get_points(user):
        return user.set_points

    # getter for weight
    # set variable
    def set_weight(self, x):
        self._weight = x

    #setter for height
    def set_height(self, x):
        self._height = x


    @property
    def weight(self):
        return self._weight

    @property
    def height(self):
        return self._height

samuel = Caloric()

# setting the weight with setter from before
samuel.set_weight(160)

# setting the height using setter from before
samuel.set_height(71)

# getting weight with getter
print(samuel.get_weight())


# getting height with getter
print(samuel.get_height())


print(samuel.weight)
print(samuel.height)