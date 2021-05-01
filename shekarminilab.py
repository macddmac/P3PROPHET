from flask import Blueprint, render_template, request
from shekarbubblesort import Bubblesort


sk = Blueprint('sk', __name__, url_prefix="/sk", static_folder="static", template_folder="templates")


@sk.route('/bubblesort', methods = ["GET","POST"])
def bubbleSort():
    inarr = []
    if request.form:
        integer = request.form.get("integer")
        inarr = integer.split()
        input = integer.split()
        if(request.form["select"] == "integer"):

            try:
                for j in range (0,len(inarr)):
                    inarr[j] = int(inarr[j])
                for j in range (0,len(input)):
                    input[j] = int(input[j])
                return render_template("shekarminilab.html",sorted_list = Bubblesort(inarr).sarr,input_list = input)
            except ValueError:
                return render_template("shekarminilab.html",sorted_list = "Can Only Contain An Integer",input_list = "Error")

    return render_template("shekarminilab.html",sorted_list = Bubblesort(inarr).oarr,input_list = inarr)
@sk.route("/home")
def index():
    return render_template("shekarminilab.html")
