from flask import Blueprint, render_template, request, flash, redirect, url_for
from sql.db import DB  # Make sure to import your database module
from datetime import datetime

food_blueprint = Blueprint('food', __name__, url_prefix='/food')

@food_blueprint.route("/search", methods=["GET"])
def search():
    rows = []
    allowed_columns = ["Label", "Category"]
    query = "SELECT * FROM Food WHERE 1=1"
    args = {}

    # TODO search-2 get name, country, state, column, order, limit request args
    name = request.args.get("name")
    category = request.args.get("category")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", 10)

    # TODO search-3 append a LIKE filter for name if provided
    if name:
        query += " AND Label LIKE %(name)s"
        args["name"] = f"%{name}%"

    # TODO search-4 append an equality filter for category if provided
    if category:
        query += " AND Category = %(category)s"
        args["category"] = category

    # TODO search-6 append sorting if column and order are provided and within the allows columns and allowed order asc,desc
    if column in allowed_columns and order in ["asc", "desc"]:
        query += f" ORDER BY {column} {order}"

    # TODO search-7 append limit (default 10) or limit greater than or equal to 1 and less than or equal to 100
    try:
        limit = int(request.args.get("limit", 10))
        if 1 <= limit <= 100:
            query += " LIMIT %(limit)s"
            args["limit"] = limit
        else:
            raise ValueError("Limit must be between 1 and 100.")
    except ValueError:
        flash("Invalid limit value.", "danger")
        return redirect(url_for("food.search"))

    try:
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
    except Exception as e:
        flash(str(e), "danger")

    allowed_columns = [(column, column.replace("_", " ").title()) for column in allowed_columns]

    return render_template("food_list.html", rows=rows, allowed_columns=allowed_columns)

@food_blueprint.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        has_error = False
        label = request.form.get("label")
        url = request.form.get("url")
        enerc_kcal = request.form.get("enerc_kcal")
        protein = request.form.get("protein")
        fat = request.form.get("fat")
        carbohydrate = request.form.get("carbohydrate")
        fiber = request.form.get("fiber")
        category = request.form.get("category")
        weight = request.form.get("weight")

        if not label:
            flash("Label is required.", "danger")
            has_error = True

        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO Food (Label, Url, Enerc_Kcal, Protein, Fat, Carbohydrate, Fiber, Category, Weight, Created, Modified)
                VALUES (%(label)s, %(url)s, %(enerc_kcal)s, %(protein)s, %(fat)s, %(carbohydrate)s, %(fiber)s, %(category)s, %(weight)s, %(created)s, %(modified)s)
                """, {
                    "label": label,
                    "url": url,
                    "enerc_kcal": enerc_kcal,
                    "protein": protein,
                    "fat": fat,
                    "carbohydrate": carbohydrate,
                    "fiber": fiber,
                    "category": category,
                    "weight": weight,
                    "created": datetime.now(),
                    "modified": datetime.now()
                })

                if result.status:
                    flash("Added Food", "success")
            except Exception as e:
                flash(str(e), "danger")

    return render_template("manage_food.html", food=request.form)

@food_blueprint.route("/edit", methods=["GET", "POST"])
def edit():
    id = request.args.get("id")

    if not id:
        flash("Food ID is required.", "danger")
        return redirect(url_for("food.search"))

    if request.method == "POST":
        has_error = False

        label = request.form.get("label")
        url = request.form.get("url")
        enerc_kcal = request.form.get("enerc_kcal")
        protein = request.form.get("protein")
        fat = request.form.get("fat")
        carbohydrate = request.form.get("carbohydrate")
        fiber = request.form.get("fiber")
        category = request.form.get("category")
        weight = request.form.get("weight")

        if not label:
            flash("Label is required.", "danger")
            has_error = True

        if not has_error:
            try:
                result = DB.update("""
                UPDATE Food
                SET Label=%(label)s, Url=%(url)s, Enerc_Kcal=%(enerc_kcal)s, Protein=%(protein)s,
                    Fat=%(fat)s, Carbohydrate=%(carbohydrate)s, Fiber=%(fiber)s, Category=%(category)s,
                    Weight=%(weight)s, Modified=%(modified)s
                WHERE FoodID=%(id)s
                """, {
                    "id": id,
                    "label": label,
                    "url": url,
                    "enerc_kcal": enerc_kcal,
                    "protein": protein,
                    "fat": fat,
                    "carbohydrate": carbohydrate,
                    "fiber": fiber,
                    "category": category,
                    "weight": weight,
                    "modified": datetime.now()
                })

                if result.status:
                    flash("Updated record", "success")
            except Exception as e:
                flash(str(e), "danger")

    row = {}
    try:
        result = DB.selectOne("SELECT * FROM Food WHERE FoodID=%(id)s", {"id": id})
        if result.status:
            row = result.row
    except Exception as e:
        flash(str(e), "danger")

    return render_template("manage_food.html", food=row)

@food_blueprint.route("/delete", methods=["GET"])
def delete():
    id = request.args.get("id")

    if not id:
        flash("Food ID is required.", "danger")
        return redirect(url_for("food.search"))

    try:
        result = DB.delete("DELETE FROM Food WHERE FoodID=%(id)s", {"id": id})

        if result.status:
            flash("Food deleted successfully", "success")
    except Exception as e:
        flash(str(e), "danger")

    return redirect(url_for("food.search"))
