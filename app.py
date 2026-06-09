from flask import Flask, render_template, request, redirect, send_file
from flask_sqlalchemy import SQLAlchemy
from models import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/contacts.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app) 


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
            name=request.form.get("name"),
            email=request.form.get("email"),
            subject=request.form.get("subject"),
            message=request.form.get("message")
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
    return send_file(
        "static/resume/resume.pdf",
        as_attachment=True
    )


# @app.route("/admin")
# def admin():
#     contacts = Contact.query.all()
#     return render_template("admin.html", contacts=contacts)


# Create database tables
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)