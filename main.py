import os

from dotenv import load_dotenv
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask_socketio import emit
from flask_socketio import SocketIO
from pymongo import MongoClient

app = Flask(__name__)
app.config["SECRET_KEY"] = "abcduifhdeuj1234"
socketio = SocketIO(app)

client = MongoClient(
    f"mongodb://{os.getenv('envUsername')}:{os.getenv('envPassword')}@ac-siyibou-shard-00-00.nducqa6.mongodb.net:27017,ac-siyibou-shard-00-01.nducqa6.mongodb.net:27017,ac-siyibou-shard-00-02.nducqa6.mongodb.net:27017/?ssl=true&replicaSet=atlas-mkrclc-shard-0&authSource=admin&retryWrites=true&w=majority"
)

db = client.get_database("okaycool")
coll = db.get_collection("messagessent")
usernamepass = db.get_collection("usernamepassword")

a = []


@app.route("/", methods=["GET", "POST"])
def home_page():
    return render_template("index.html", coll=list(coll.find()))


@app.route("/login", methods=["GET", "POST"])
def login():
    if not "loginname" in session:
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            a = usernamepass.find_one({
                "username": username,
                "password": password
            })
            if not a:
                return render_template("login.html", failed=True)
            else:
                session["loginname"] = username
                print(username)
                return redirect(url_for("home_page"))
        else:
            return render_template("login.html")
    else:
        return redirect(url_for("home_page"))


@app.route("/logout")
def remove_session():
    session.pop("loginname")
    return redirect(url_for("home_page"))


@socketio.on("messagesent")
def test_stuff(data):
    coll.insert_one({"username": session["loginname"], "message": data})
    emit(
        "updateData",
        {
            "username": session["loginname"],
            "data": data["data"]
        },
        broadcast=True,
    )


if __name__ == "__main__":
    socketio.run(app, debug=True)
