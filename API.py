from flask import render_template
import requests
def amazon_api():
    url = "https://amazon-price.p.rapidapi.com/azapi-azSearch"

    querystring = {"prime":"false","query":"affiliate marketing","page":"1"}

    headers = {
        'x-rapidapi-key': "c5f23bd603msh8cf6b2cf2f62cf4p1de370jsnbc056cd17a48",
        'x-rapidapi-host': "amazon-price.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    return response.text

def error(message, code=400):
    """Render message as an apology to user when errors occur."""
    return render_template("error.html", code=code, message=message)