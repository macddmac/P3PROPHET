from flask import Flask, redirect, url_for, render_template, request, session
import requests as r
app = Flask(__name__)

@app.route("/random_cat_fact", methods=["GET"])
def random_cat_fact():
    x = r.get("https://catfact.ninja/fact?max_length=140")
    data = x.json()
    fact = data.get("fact")

    return fact

if __name__ == "__main__":
    app.run(debug=True, port=3000)