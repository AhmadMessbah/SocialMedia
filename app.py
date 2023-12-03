from audioop import reverse

from flask import Flask, render_template, redirect, request, session
from controller.like_controller import LikeController
from flask_session import Session

from controller.profile_controller import ProfileController

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
    if not session.get("username"):
        return render_template("login.html")

    if request.method == "POST":
        name = request.form.get("name")
        family = request.form.get("family")
        username = request.form.get("username")
        password = request.form.get("password")
        ProfileController.save(name, family, username, password)
    elif request.method == "DELETE":
        ProfileController.remove(request.args.get("id"))

    return render_template("profile.html", profile_list=ProfileController.find_all()[1])


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        # if request.form.get("password") == request.form.get("repeat_password"):

        status, data = ProfileController.save(
            request.form.get("name"),
            request.form.get("family"),
            request.form.get("email"),
            request.form.get("password"))

    return render_template("register.html")


# @app.route("/like",methods=["POST","GET","DELETE"])
# def like(request ,pk):
# object=get_object_or_404(MyModel,pk=pk)
# if object.likes.filter(user=request.user).exists():
#  object.likes.remove(request.user)
# else:
# object.likes.add(request.user)
# object.save()
# return render_template("like.html", like_list=LikeController.find_all()[1])
# return redirect(reverse('my_app:object_detail',kwargs={'pk':pk}))

# if not session.get("username"):
#     return render_template("login.html")
# return render_template("profile.html", profile_list=ProfileController.find_all()[1])

@app.route("/forget")
def forget():
    return  render_template("forget-password.html")

@app.route("/logout")
def logout():
    session["username"] = None
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
