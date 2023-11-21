from flask import *

#from controller.profile_controller import PersonController

app = Flask(__name__, template_folder="view", static_folder="view/assets")


@app.route("/")
def home():
    return render_template("index.html")

#@app.route("/profile", methods = ["GET","POST", "DELETE"])
#def profile():
    #if request.method == "POST":
     #   PersonController.save(
      #      request.form.get("name"),
       #     request.form.get("family"),
        #    request.form.get("username"),
         #   request.form.get("password"))

    #if request.method == "DELETE":
       # PersonController.remove(int(request.args.get("id")))

   # status,data = PersonController.find_all()
    #if status:
        #return render_template("profile.html", profile_list = data)

app.run(host="", port="80", debug=True)
