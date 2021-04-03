from flask import Blueprint, render_template

shekarminilab_bp = Blueprint('shekarminilab', __name__,
                            template_folder='templates',)

@shekarminilab_bp.route('/')
def index():
    return render_template("shekarminilab.html")

# defining classes
class leaderboard:
    def starting(user, place=0, points=0):
        user.place = place
        user.points = points

    def Shekar(user):
        user = "Shekar"

    # getter for place
    # set variable
    def get_place(user):
        return user.place

    # getter for points
    # set variable
    def get_points(user):
        return user.points

    # setter for variable place
    def set_place(user, x):
        user._place = x

    # setter for variable points
    def set_points(user, x):
        user._points = x

    @property
    def place(user):
        return user._place
    @property
    def points(user):
        return user._points

Shekar = leaderboard()

# setting the place with setter from before
Shekar.set_place(2)
# setting the points using setter from before
Shekar.set_points(55)

# printing full leaderboard with getters
print(Shekar.get_place())
print(Shekar.get_points())
print(" ")
print("place: ")
print(Shekar.place)
print("points: ")
print(Shekar.points)