from flask import Flask, render_template, request, redirect
from user import User

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create_user", methods=["POST"])
def create_user():

    User.create(request.form)
    return redirect("/users")


@app.route("/users")
def show_users():
    users = User.find_all()

    return render_template("result.html", users=users)



if __name__ == "__main__":
    app.run(debug=True)
