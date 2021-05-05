from flask import Blueprint, render_template, request
from shekarbubblesort import Bubblesort


sk = Blueprint('sk', __name__, url_prefix="/sk", static_folder="static", template_folder="templates")


@sk.route('/bubblesort', methods = ["GET","POST"])
def bubbleSort():
    arr = []
    if request.form:
        integer = request.form.get("integer")
        arr = integer.split()

        try:
            for j in range (0,len(arr)):
                arr[j] = int(arr[j])
            for j in range (0,len(input)):
                input[j] = int(input[j])
            return render_template("shekarminilab.html",sorted_list = Bubblesort(arr).sarr,input_list = input)
        except ValueError:
            return render_template("shekarminilab.html",sorted_list = "Can Only Contain An Integer",input_list = "Error")

    return render_template("shekarminilab.html",sorted_list = Bubblesort(arr).oarr,input_list = arr)

#@sk.route("/shekarminilab")
#def index():
#    return render_template("shekarminilab.html")
