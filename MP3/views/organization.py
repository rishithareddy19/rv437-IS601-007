from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
import pycountry

organization = Blueprint('organization', __name__, url_prefix='/organization')

@organization.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, donation count as donations for the organization
    #rv437-30/11/23
    # don't do SELECT * and replace the below "..." portion
    allowed_columns = ["name", "address", "website","city", "country", "state", "zip"]
    query = "SELECT DISTINCT id, name, address, city, country, state, zip, website, (SELECT COUNT(*) FROM IS601_MP3_Donations  WHERE organization_id = IS601_MP3_Organizations.id) as donations FROM IS601_MP3_Organizations WHERE 1=1"
    args = {}
    # TODO search-2 get name, country, state, column, order, limit request args
    #rv437-30/11/23
    limit = 10 # TODO change this per the above requirements
    name = request.args.get("name")
    country = request.args.get("country")
    state = request.args.get("state")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", 10)
    # TODO search-3 append a LIKE filter for name if provided
    #rv437-30/11/23
    if name:
        query += " AND name LIKE %(name)s"
        args["name"] = f"%{name}%"

    # TODO search-4 append an equality filter for country if provided
    #rv437-30/11/23
    if country:
        query += " AND country = %(country)s"
        args["country"] = country

    # TODO search-5 append an equality filter for state if provided
    #rv437-30/11/23
    if state:
        query += " AND state = %(state)s"
        args["state"] = state

    # TODO search-6 append sorting if column and order are provided and within the allows columns and allowed order asc,desc
    #rv437-30/11/23
    if column in allowed_columns and order in ["asc", "desc"]:
        query += f" ORDER BY {column} {order}"

    # TODO search-7 append limit (default 10) or limit greater than or equal to 1 and less than or equal to 100
    #rv437-30/11/23
    try:
        limit = int(request.args.get("limit", 10))
        if 1 <= limit <= 100:
            query += " LIMIT %(limit)s"
            args["limit"] = limit
        else:
            raise ValueError("Limit must be between 1 and 100.")
    except ValueError:
     # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
     #rv437-30/11/23
        flash("Invalid limit value.", "danger")
        return redirect(url_for("organization.search"))

    try:
        result = DB.selectAll(query, args)
        if result.status:
            print(result.rows)
            rows = result.rows
    except Exception as e:
        # TODO search-9 make message user friendly
        #rv437-30/11/23
        flash(str(e), "danger")
    
    allowed_columns = [(column, column.replace("_", " ").title()) for column in allowed_columns]
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    
    # do this prior to passing to render_template, but not before otherwise it can break validation
    #rv437-30/11/23

    return render_template("list_organizations.html", rows=rows, allowed_columns=allowed_columns)

@organization.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        has_error = False
         # TODO add-1 retrieve form data for name, address, city, state, country, zip, website, description
        # TODO add-2 name is required (flash proper error message)
        # TODO add-3 address is required (flash proper error message)
        # TODO add-4 city is required (flash proper error message)
        # TODO add-5 state is required (flash proper error message)
        # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
        # hint see geography.py and pycountry documentation to solve this
        # TODO add-6 country is required (flash proper error message)
        # TODO add-6a country should be a valid country mentioned in pycountry
        # hint see geography.py and pycountry documentation to solve this
        # TODO add-7 website is not required
        # TODO add-8 zip is required (flash proper error message)
        # note: call zip variable zipcode as zip is a built in function it could lead to issues
        # TODO add-9 description is not required
        #rv437-30/11/23


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
        #rv437-30/11/23

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
                # TODO edit-10 fill in proper update query
                    # name, address, city, state, country, zip, website
                    #rv437-30/11/23
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
                # <-- TODO add-10 add query and add arguments
                #rv437-30/11/23

                if result.status:
                    flash("Added Organization", "success")
            except Exception as e:
                # TODO add-11 make message user friendly
                #rv437-30/11/23
                flash(str(e), "danger")

    return render_template("manage_organization.html", org=request.form)

@organization.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    #rv437-30/11/23
    id = request.args.get("id")

    if not id:# TODO update this for TODO edit-1
        #rv437-30/11/23
        flash("Organization ID is required.", "danger")
        return redirect(url_for("organization.search"))

    if request.method == "POST":
        has_error = False
        # TODO edit-2 retrieve form data for name, address, city, state, country, zip, website
            # TODO edit-3 name is required (flash proper error message)
            # TODO edit-4 address is required (flash proper error message)
            # TODO edit-5 city is required (flash proper error message)
            # TODO edit-6 state is required (flash proper error message)
            # TODO edit-6a state should be a valid state mentioned in pycountry for the selected state
            # hint see geography.py and pycountry documentation
            # TODO edit-7 country is required (flash proper error message)
            # TODO edit-7a country should be a valid country mentioned in pycountry
            # hint see geography.py and pycountry documentation
            # TODO edit-8 website is not required
            # TODO edit-9 zipcode is required (flash proper error message)
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            # populate data dict with mappings
            #rv437-30/11/23

        name = request.form.get("name")
        address = request.form.get("address")
        city = request.form.get("city")
        state = request.form.get("state")
        country = request.form.get("country")
        website = request.form.get("website")
        zipcode = request.form.get("zipcode")
        #rv437-30/11/23

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
        #rv437-30/11/23

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
                #rv437-30/11/23
                DB.delete("DELETE FROM IS601_MP3_Donations WHERE organization_id=%(id)s", {"id": id})
                # Then, update the organization
                #rv437-30/11/23
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
         # TODO edit-12 fetch the updated data
         #rv437-30/11/23
        result = DB.selectOne("SELECT * FROM IS601_MP3_Organizations WHERE id=%(id)s", {"id": id})
        if result.status:
            row = result.row
    except ValueError as ve:
    # Handle the specific ValueError here
    #rv437-30/11/23
        flash(str(ve), "danger")
    except Exception as e:
        # TODO edit-13 make this user-friendly
        #rv437-30/11/23
        flash(str(e), "danger")
    return render_template("manage_organization.html", org=row)

@organization.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 if id is missing, flash necessary message and redirect to search
    # TODO delete-2 delete organization by id (note: you'll likely need to trigger a delete of all donations related to this organization first due to foreign key constraints)
    # TODO delete-3 ensure a flash message shows for successful delete
    # TODO delete-4 pass all argument except id to this route
    # TODO delete-5 redirect to organization search
    #rv437-30/11/23
    id = request.args.get("id")

    if not id:
        flash("Organization ID is required.", "danger")
        return redirect(url_for("organization.search"))

    try:
        # TODO: Add logic to delete all donations related to this organization first due to foreign key constraints
        #rv437-30/11/23
        DB.delete("DELETE FROM IS601_MP3_Donations WHERE organization_id=%(id)s", {"id": id})

        # Then, delete the organization
        #rv437-30/11/23
        result = DB.delete("DELETE FROM IS601_MP3_Organizations WHERE id=%(id)s", {"id": id})

        if result.status:
            flash("Organization deleted successfully", "success")
    except Exception as e:
        flash(str(e), "danger")
        # return redirect(url_for("organization.search", **args))
        #rv437-30/11/23

    return redirect(url_for("organization.search"))
