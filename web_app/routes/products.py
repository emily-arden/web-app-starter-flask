
from flask import Blueprint, request, render_template, jsonify, flash, redirect #, url_for


product_routes = Blueprint("product_routes", __name__)

@product_routes.route('/products')
def index():
    print("VISITING THE PRODUCTS INDEX PAGE")
    return render_template("products/index.html")

@product_routes.route('/products/new')
def new():
    print("VISITING THE NEW PRODUCT PAGE")
    print("REQUEST PARAMS:", dict(request.args))
    return render_template("products/form.html")



def cocktails():
    f = r"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=Gin"
    data = request.form["Ingredient"]
    tt = json.loads(data.text)

    for i in (tt["drinks"]):
        print(i["strDrink"], "\n")
        url = i["strDrinkThumb"]
        webbrowser.open(url)
cocktails()


@product_routes.route('/products/create', methods=["POST"])
def create():
    print("CREATING A PRODUCT...")
    print("FORM DATA:", dict(request.form))
    #return jsonify(request.form)

    product_name = request.form["product_name"]
    flash(f"Product '{product_name}' created successfully!", "success") # use the "success" category to correspond with twitter bootstrap alert colors
    return redirect("/products")
