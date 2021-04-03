from flask import Blueprint, render_template

samminilab_bp = Blueprint('samminilab', __name__,
                            template_folder='templates',)

@samminilab_bp.route('/')
def index():
    return render_template("samminilab.html")

# class
class Caloric:
    def init(self, weight=0, height=0):
        self.weight = weight
        self.height = height

    # getter for weight
    def get_weight(self):
        return self._weight

    #getter for height
    def get_height(self):
        return self.set_height

    #setter for weight
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