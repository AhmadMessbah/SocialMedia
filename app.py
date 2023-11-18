from flask import Flask, render_template, request

from model.da.database import DatabaseManager
from model.entity.profile import Profile

app = Flask(__name__, template_folder="view")


@app.route("/")
def home():
    da = DatabaseManager()
    return render_template("home.html", profile_list = da.find_all(Profile))


@app.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "POST":
        profile = Profile()
        profile.name= request.form.get("name"),
        profile.family = request.form.get("family")

        da = DatabaseManager()
        da.save(profile)

        return render_template("home.html", profile_list = da.find_all(Profile))

app.run(host="192.168.39.100", port=80)
