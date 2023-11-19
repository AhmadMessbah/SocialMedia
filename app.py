from flask import Flask, render_template, request

from model.da.database import DatabaseManager
from model.entity.profile import Profile
from model.entity.like import Like

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

def like():
    if request.method=="Like":
        like=Like()
        like.profile=request.form.get("profile"),
        like.post=request.form.get("post")

        da=DatabaseManager()
        da.save(like)

        return render_template("home.html",like_list=da.find_by_id(Like))

app.run(host="192.168.1.3", port=80)
