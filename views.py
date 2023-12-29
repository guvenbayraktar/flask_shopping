from flask import Blueprint, render_template, redirect, request

blue = Blueprint("blue", __name__, template_folder="templates")

sepet = {}


@blue.route("/")
def shopping_list():
    return render_template("shopping_list.html", sepet=sepet)


@blue.post("/add_product")
def add_product():
    product_name = request.form["product_name"].strip(" ")
    product_amount = int(request.form["product_amount"])
    if product_name != "":
        sepet[product_name] = product_amount
    return redirect("/")


@blue.get("/remove_product/<string:name>")
def remove_product(name):
    sepet.pop(name, None)
    return redirect("/")
