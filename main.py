from flask import Flask, render_template, url_for, request, redirect, session
from flask_socketio import SocketIO, emit
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
import os
from dotenv import load_dotenv


app = Flask(__name__)
app.config["SECRET_KEY"] = "abcduifhdeuj1234"
socketio = SocketIO(app)

client = MongoClient("mongodb://localhost:27017")

db = client.get_database("okaycool")
coll = db.get_collection("messagessent")
usernamepass = db.get_collection("usernamepassword")

a = []

@app.route('/', methods=["GET", "POST"])
def home_page():
    return render_template('index.html', coll=list(coll.find()))

@app.route('/login', methods=["GET", "POST"])
def login():
    if not 'loginname' in session: 
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            a = usernamepass.find_one({'username' : username})
            if not a:
                return render_template('login.html', failed=True)
            else:
                if (check_password_hash(a['password'], password)):
                    session['loginname'] = username
                    print(username)
                    return redirect(url_for('home_page'))
                else:
                    return render_template('login.html', failed=True)
        else:
            return render_template('login.html')
    else: return redirect(url_for("home_page"))
    
@app.route('/logout')
def remove_session():
    session.pop('loginname')
    return redirect(url_for('home_page'))

@app.route('/register', methods=["GET", "POST"])
def register():
    if not 'loginname' in session:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            usernamepass.insert_one({'username' : username, 'password' : generate_password_hash(password, "sha256")})
            return redirect(url_for("home_page"))
        else:
            return render_template("register.html")
    else:
        return redirect(url_for("home_page"))

@socketio.on("messagesent")
def test_stuff(data):
    coll.insert_one({'username' : session['loginname'], 'message' : data})
    emit("updateData", {"username" : session['loginname'], "data" : data["data"]}, broadcast=True)

if __name__ ==  '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)