from flask import Flask, render_template
from flask import request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask import send_file
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
db = SQLAlchemy(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/skills")
def skills():
    return render_template("skills.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        contact = Contact(
            name=request.form["name"],
            email=request.form["email"],
            subject=request.form["subject"],
            message=request.form["message"],
        )

        db.session.add(contact)
        db.session.commit()

        return redirect("/thankyou")

    return render_template("contact.html")


@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")


@app.route("/resume")
def resume():
    return send_file("static/resume/resume.pdf", as_attachment=True)


@app.route("/admin")
def admin():

    contacts = Contact.query.all()

    return render_template("admin.html", contacts=contacts)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
