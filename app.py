from flask import Flask, render_template, redirect, request, session


from controller.profile_controller import ProfileController
from flask_session import Session

from controller import *

app = Flask(__name__, template_folder="view", static_folder="view/assets")
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        status, data = ProfileController.login(username, password)
        if status:
            session["username"] = username
            return render_template("profile.html", profile=data)
        else:
            message = data
    return render_template("login.html", message=message)


@app.route("/profile", methods=["POST", "GET", "DELETE"])
def profile():
    if not session.get("username"):
        return render_template("login.html")

    if request.method == "POST":
        name = request.form.get("name")
        family = request.form.get("family")
        username = request.form.get("username")
        password = request.form.get("password")
        status, data = ProfileController.save(name, family, username, password)
    elif request.method == "DELETE":
        ProfileController.remove(request.args.get("id"))

    # return data, 204
    return render_template("profile.html", profile=ProfileController.find_by_username(session.get("username"))[1])


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        # if request.form.get("password") == request.form.get("repeat_password"):

        status, data = ProfileController.save(
            request.form.get("name"),
            request.form.get("family"),
            request.form.get("email"),
            request.form.get("password"))
        return render_template("login.html")


    return render_template("register.html")


@app.route("/post", methods=["POST", "GET"])
def post():
    if not session.get("username"):
        return render_template("login.html")
    if request.method == "POST":
        pass
    return render_template("post.html", posts=ProfileController.find_by_username(session.get("username"))[1].posts)


@app.route("/forget")
def forget():
    return render_template("forget-password.html")


@app.route("/logout")
def logout():
    session["username"] = None
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)
