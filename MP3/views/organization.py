from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
import pycountry

organization = Blueprint('organization', __name__, url_prefix='/organization')

@organization.route("/search", methods=["GET"])
def search():
    rows = []
    allowed_columns = ["name", "address", "website","city", "country", "state", "zip"]
    query = "SELECT DISTINCT id, name, address, city, country, state, zip, website, (SELECT COUNT(*) FROM IS601_MP3_Donations  WHERE organization_id = IS601_MP3_Organizations.id) as donations FROM IS601_MP3_Organizations WHERE 1=1"
    args = {}
    
    name = request.args.get("name")
    country = request.args.get("country")
    state = request.args.get("state")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", 10)
    # TODO search-3 append a LIKE filter for name if provided
    if name:
        query += " AND name LIKE %(name)s"
        args["name"] = f"%{name}%"

    # TODO search-4 append an equality filter for country if provided
    if country:
        query += " AND country = %(country)s"
        args["country"] = country

    # TODO search-5 append an equality filter for state if provided
    if state:
        query += " AND state = %(state)s"
        args["state"] = state

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
        return redirect(url_for("organization.search"))

    try:
        result = DB.selectAll(query, args)
        if result.status:
            print(result.rows)
            rows = result.rows
    except Exception as e:
        flash(str(e), "danger")
    
    allowed_columns = [(column, column.replace("_", " ").title()) for column in allowed_columns]

    return render_template("list_organizations.html", rows=rows, allowed_columns=allowed_columns)

@organization.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        has_error = False

        name = request.form.get("name")
        address = request.form.get("address")
        city = request.form.get("city")
        state = request.form.get("state")
        country = request.form.get("country")
        website = request.form.get("website")
        zipcode = request.form.get("zipcode")
        description = request.form.get("description")

        if not name:
            flash("Name is required.", "danger")
            has_error = True

        if not address:
            flash("Address is required.", "danger")
            has_error = True

        if not city:
            flash("City is required.", "danger")
            has_error = True

        if not state:
            flash("State is required.", "danger")
            has_error = True
        elif state not in [s.alpha_2 for s in pycountry.subdivisions.get(country, [] if country else pycountry.subdivisions.get('US', []))]:
            flash("Invalid state.", "danger")
            has_error = True

        if not country:
            flash("Country is required.", "danger")
            has_error = True
        elif country not in [c.alpha_2 for c in pycountry.countries]:
            flash("Invalid country.", "danger")
            has_error = True

        if not zipcode:
            flash("Zipcode is required.", "danger")
            has_error = True

        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Organizations (name, address, city, state, country, zip, website, description)
                VALUES (%(name)s, %(address)s, %(city)s, %(state)s, %(country)s, %(zip)s, %(website)s, %(description)s)
                """, {
                    "name": name,
                    "address": address,
                    "city": city,
                    "state": state,
                    "country": country,
                    "zip": zipcode,
                    "website": website,
                    "description": description
                })

                if result.status:
                    flash("Added Organization", "success")
            except Exception as e:
                flash(str(e), "danger")

    return render_template("manage_organization.html", org=request.form)

@organization.route("/edit", methods=["GET", "POST"])
def edit():
    id = request.args.get("id")

    if not id:
        flash("Organization ID is required.", "danger")
        return redirect(url_for("organization.search"))

    if request.method == "POST":
        has_error = False

        name = request.form.get("name")
        address = request.form.get("address")
        city = request.form.get("city")
        state = request.form.get("state")
        country = request.form.get("country")
        website = request.form.get("website")
        zipcode = request.form.get("zipcode")

        if not name:
            flash("Name is required.", "danger")
            has_error = True

        if not address:
            flash("Address is required.", "danger")
            has_error = True

        if not city:
            flash("City is required.", "danger")
            has_error = True

        if not state:
            flash("State is required.", "danger")
            has_error = True
        elif state not in [s.alpha_2 for s in pycountry.subdivisions.get(country, [] if country else pycountry.subdivisions.get('US', []))]:
            flash("Invalid state.", "danger")
            has_error = True

        if not country:
            flash("Country is required.", "danger")
            has_error = True
        elif country not in [c.alpha_2 for c in pycountry.countries]:
            flash("Invalid country.", "danger")
            has_error = True

        if not zipcode:
            flash("Zipcode is required.", "danger")
            has_error = True

        if not has_error:
            try:
                # TODO: Add logic to delete all donations related to this organization first due to foreign key constraints
                DB.delete("DELETE FROM IS601_MP3_Donations WHERE organization_id=%(id)s", {"id": id})

                # Then, update the organization
                result = DB.update("""
                UPDATE IS601_MP3_Organizations
                SET name=%(name)s, address=%(address)s, city=%(city)s, state=%(state)s,
                    country=%(country)s, zip=%(zip)s, website=%(website)s
                WHERE id=%(id)s
                """, {
                    "id": id,
                    "name": name,
                    "address": address,
                    "city": city,
                    "state": state,
                    "country": country,
                    "zip": zipcode,
                    "website": website
                })

                if result.status:
                    flash("Updated record", "success")
            except Exception as e:
                flash(str(e), "danger")

    row = {}
    try:
        result = DB.selectOne("SELECT * FROM IS601_MP3_Organizations WHERE id=%(id)s", {"id": id})

        if result.status:
            row = result.row
    except ValueError as ve:
    # Handle the specific ValueError here
        flash(str(ve), "danger")
    except Exception as e:
        flash(str(e), "danger")

    return render_template("manage_organization.html", org=row)

@organization.route("/delete", methods=["GET"])
def delete():
    id = request.args.get("id")

    if not id:
        flash("Organization ID is required.", "danger")
        return redirect(url_for("organization.search"))

    try:
        # TODO: Add logic to delete all donations related to this organization first due to foreign key constraints
        DB.delete("DELETE FROM IS601_MP3_Donations WHERE organization_id=%(id)s", {"id": id})

        # Then, delete the organization
        result = DB.delete("DELETE FROM IS601_MP3_Organizations WHERE id=%(id)s", {"id": id})

        if result.status:
            flash("Organization deleted successfully", "success")
    except Exception as e:
        flash(str(e), "danger")

    return redirect(url_for("organization.search"))
