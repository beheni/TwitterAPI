
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
import follower_map

app = Flask(__name__)

# def hello_world():
#     return 'Hello from Flask!'

@app.route('/')
def map_func():
    return render_template("index.html")

@app.route('/reroute', methods=["POST"])
def reroute():
    if request.method == "POST":
        dct = request.form
        nickname = dct["name"]
        follower_map.main(nickname)
        return render_template("Map.html")
