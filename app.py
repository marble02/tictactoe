from flask import Flask, render_template, session, redirect, url_for, request
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():

    if "board" not in session:
        # session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
        # row = []
        # for i in range(20):
        #     row.append(None)
        # session["board"] = [[None for i in range(10)] for j in range(10)]
        # session["turn"] = "X"
        return redirect("/clear")

    return render_template("game.html", game=session["board"], turn=session["turn"])

@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    session["board"][row][col] = session["turn"]
    if session["turn"] == "X":
        session["turn"] = "O"
    elif session["turn"] == "O":
        session["turn"] = "X"
    return redirect(url_for("index"))

@app.route("/clear", methods=["GET", "POST"])
def clearBoard():
    # session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
    session["board"] = [[None for i in range(10)] for j in range(10)]
    session["turn"] = "X"
    return render_template("game.html", game=session["board"], turn=session["turn"])