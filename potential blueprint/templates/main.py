from flask import Flask, render_template
from second import second

app = Flask(__name__)
app.register_blueprint(second, url_prefix="/admin")
# When running add /admin after url

@app.route("/")
def test():
   return "<h1>Test1</h1>"

if __name__ == "__main__":
   app.run(debug=True)
