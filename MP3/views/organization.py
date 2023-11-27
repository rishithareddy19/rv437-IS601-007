from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
import pycountry

organization = Blueprint('organization', __name__, url_prefix='/organization')

@organization.route("/search", methods=["GET"])
def search():
    rows = []
    allowed_columns = ["name", "city", "country", "state", "modified", "created"]
    query = "SELECT id, name, address, city, country, state, zip, website, (SELECT COUNT(*) FROM IS601_MP3_Donations WHERE organization_id = IS601_MP3_Organizations.id) as donations FROM IS601_MP3_Organizations WHERE 1=1"
    args = {}

    limit = request.args.get("limit", 10)
    try:
        limit = int(limit)
        if limit < 1 or limit > 100:
            raise ValueError("Limit must be between 1 and 100.")
    except ValueError:
        flash("Invalid limit value.", "danger")
        return redirect(url_for("organization.search"))

    query += " LIMIT %(limit)s"
    args["limit"] = limit

    try:
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
    except Exception as e:
        flash(str(e), "danger")

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
        # Then, delete the organization
        result = DB.delete("DELETE FROM IS601_MP3_Organizations WHERE id=%(id)s", {"id": id})

        if result.status:
            flash("Organization deleted successfully", "success")
    except Exception as e:
        flash(str(e), "danger")

    return redirect(url_for("organization.search"))
