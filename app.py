
from flask import Flask, render_template
 
app = Flask(__name__)
 
 
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route("/services.html")
def services():
    return render_template("services.html")

@app.route("/contacts.html")
def contact():
    return render_template("contacts.html")

@app.route("/login.html")
def login():
    return render_template("login.html")

@app.route("/pricing.html")
def pricing():
    return render_template("pricing.html")

@app.route("/product.html")
def product():
    return render_template("product.html")

@app.route("/projects.html")
def projects():
    return render_template("projects.html")

@app.route("/shopping-cart.html")
def shopping_cart():
    return render_template("shopping-cart.html")

@app.route("/signup.html")
def signup():
    return render_template("signup.html")

@app.route("/team.html")
def team():
    return render_template("team.html")

@app.route("/testimonials.html")
def testimonials():
    return render_template("testimonials.html")