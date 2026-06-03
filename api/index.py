from flask import Flask, render_template, request, redirect, send_file
from flask_sqlalchemy import SQLAlchemy
import sys
import os

# Add parent directory to path to import models
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models import *

app = Flask(__name__, template_folder='../templates', static_folder='../static')

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///instance/portfolio.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

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


@app.route("/admin")
def admin():
    return render_template("admin.html")
