from flask import Flask
from flask import render_template
flask_app = Flask(__name__)
from pymongo import MongoClient
client = MongoClient("mongodb+srv://<Username>:<Password>@cluster0.26bu2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.shop_db # Same name as the database on the MongoDB website.
products = db.products # Same collection name on MongoDB website.

@flask_app.route("/")

@flask_app.route("/index")
def index():
    return render_template("home.html")

@flask_app.route("/products")
def products():
    phones = list(db.products.find())
    return render_template("products.html", phones=phones)

flask_app.run(host="0.0.0.0", port=5000)