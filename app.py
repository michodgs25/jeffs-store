import os
from flask import (
    Flask, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
mongo = PyMongo(app)


@app.route("/")
@app.route("/get_index")
def get_index():
    return render_template("index.html")


@app.route("/products")
def products():
    products = list(mongo.db.products.find())
    return render_template("index.html", products=products)


@app.route("/product/add", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        product = {
            "product_id": request.form.get("product_id"),
            "product_name": request.form.get("product_name"),
            "product_price": request.form.get("product_price"),
            "product_currency": request.form.get("product_currency")
        }
        mongo.db.products.insert_one(product)
        return redirect(url_for("products"))
    product = mongo.db.products.find().sort("product_name", 1)
    return render_template("add_product.html", products=products)


@app.route("/product/edit/<product_id>", methods=["POST", "GET"])
def edit_product(product_id):
    product = mongo.db.products.find_one({"_id": ObjectId(product_id)})
    if not product:

        return render_template("error.html")
    if request.method == "POST":
        submit = {
            "product_id": request.form.get("product_id"),
            "product_name": request.form.get("product_name"),
            "product_price": request.form.get("product_price"),
            "product_currency": request.form.get("product_currency")
        }
        mongo.db.products.update({"_id": ObjectId(product_id)}, submit)
        return redirect(url_for("products"))

        mongo.db.products.update_one({"_id": ObjectId(product_id)}, submit)
    product = mongo.db.products.find_one({"_id": ObjectId(product_id)})
    return render_template("edit_product.html", products=products)


@app.route("/product/delete/<product_id>")
def delete_product(product_id):
    mongo.db.products.remove({"_id": ObjectId(product_id)})
    return redirect(url_for("products"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
