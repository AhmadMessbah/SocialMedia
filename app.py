from flask import Flask, render_template, redirect, request, session
from flask_session import Session

from controllers.profile_controller import ProfileController
app = Flask(__name__, template_folder="view", static_folder="view/assets")
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def home():
    return render_template("template.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # if find_by_username_password(username,password):
        # print(username,password)
        session["username"] = username
        return render_template("profile.html", profile_list=ProfileController.find_all()[1])
    return render_template("login.html")


@app.route("/profile", methods=["POST", "GET", "DELETE"])
def profile():
    if request.method == "POST":
        name = request.form.get("name")
        family = request.form.get("family")
        username = request.form.get("username")
        password = request.form.get("password")
        ProfileController.save(name, family, username, password)
    elif request.method == "DELETE":
        ProfileController.remove(request.args.get("id"))

    # if not session.get("username"):
    #     return render_template("login.html")
    return render_template("profile.html", profile_list=ProfileController.find_all()[1])


@app.route("/logout")
def logout():
    session["username"] = None
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
