import datetime
from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
donations = Blueprint('donations', __name__, url_prefix='/donations')

@donations.route("/search", methods=["GET"])
def search():
    rows = []
    organization_name = ""
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve donation id as id, donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments, organization_name using a LEFT JOIN
    #rv437-30/11/23
    query = """
    SELECT d.id, d.donor_firstname, d.donor_lastname, d.donor_email, d.organization_id, 
           d.item_name, d.item_description, d.item_quantity, d.donation_date, d.comments, 
           o.name as organization_name
    FROM IS601_MP3_Donations d
    LEFT JOIN IS601_MP3_Organizations o ON d.organization_id = o.id
    WHERE 1=1
    """
    args = {}

    allowed_columns = ["donor_firstname", "donor_lastname", "donor_email", "organization_name", "item_name", "item_description","item_quantity", "donation_date", "comments"]
    # TODO search-2 get fn, ln, email, organization_id, column, order, limit from request args
    # TODO search-3 append like filter for donor_firstname if provided
    # TODO search-4 append like filter for donor_lastname if provided
    # TODO search-5 append like filter for donor_email if provided
    # TODO search-6 append like filter for item_name if provided
    # TODO search-7 append equality filter for organization_id if provided
    # TODO search-8 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    # TODO search-9 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # TODO search-10 provide a proper error message if limit isn't a number or if it's out of bounds
    #rv437-30/11/23
    fn = request.args.get("donor_firstname")
    ln = request.args.get("donor_lastname")
    email = request.args.get("donor_email")
    item_name = request.args.get("item_name")
    organization_id = request.args.get("organization_id")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit")

    if fn:
        query += " AND d.donor_firstname LIKE %(donor_firstname)s"
        args["donor_firstname"] = f"%{fn}%"

    if ln:
        query += " AND d.donor_lastname LIKE %(donor_lastname)s"
        args["donor_lastname"] = f"%{ln}%"

    if email:
        query += " AND d.donor_email LIKE %(donor_email)s"
        args["donor_email"] = f"%{email}%"
    #rv437-30/11/23

    if item_name:
        query += " AND d.item_name LIKE %(item_name)s"
        args["item_name"] = f"%{item_name}%"

    if organization_id:
        query += " AND d.organization_id = %(organization_id)s"
        args["organization_id"] = organization_id

    if column and column in allowed_columns and order in ["asc", "desc"]:
        query += f" ORDER BY {column} {order}"

    if limit:
        try:
            limit = int(limit)
            if 1 <= limit <= 100:
                query += " LIMIT %(limit)s"
                args["limit"] = limit
            else:
                flash("Limit must be between 1 and 100", "danger")
        except ValueError:
            flash("Invalid limit value", "danger")

    try:
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-11 make message user friendly
        #rv437-30/11/23
        flash("There was an error retrieving donation data", "danger")
         # TODO search-12 if request args has organization identifier set organization_name variable to the correct name
         #rv437-30/11/23

    return render_template("list_donations.html", organization_name=organization_name, rows=rows, allowed_columns=allowed_columns)

@donations.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments
        # TODO add-2 donor_firstname is required (flash proper error message)
        # TODO add-3 donor_lastname is required (flash proper error message)
        # TODO add-4 donor_email is required (flash proper error message)
        # TODO add-4a email must be in proper format (flash proper message)
        # TODO add-5 organization_id is required (flash proper error message)
        # TODO add-6 item_name is required (flash proper error message)
        # TODO add-7 item_description is optional
        # TODO add-8 item_quantity is required and must be more than 0 (flash proper error message)
        # TODO add-9 donation_date is required and must be within the past 30 days
        # TODO add-10 comments are optional
        #rv437-30/11/23
        
        donor_firstname = request.form.get("donor_firstname")
        donor_lastname = request.form.get("donor_lastname")
        donor_email = request.form.get("donor_email")
        organization_id = request.form.get("organization_id")
        item_name = request.form.get("item_name")
        item_description = request.form.get("item_description")
        item_quantity = request.form.get("item_quantity")
        donation_date = request.form.get("donation_date")
        comments = request.form.get("comments")
        #rv437-30/11/23

        has_error = False

        if not donor_firstname:
            flash("Donor First Name is required", "danger")
            has_error = True

        if not donor_lastname:
            flash("Donor Last Name is required", "danger")
            has_error = True

        if not donor_email:
            flash("Donor Email is required", "danger")
            has_error = True
        elif "@" not in donor_email:
            flash("Invalid email format", "danger")
            has_error = True

        if not organization_id:
            flash("Organization ID is required", "danger")
            has_error = True
        #rv437-30/11/23

        if not item_name:
            flash("Item Name is required", "danger")
            has_error = True

        if not item_quantity or int(item_quantity) <= 0:
            flash("Item Quantity must be greater than 0", "danger")
            has_error = True

        if not donation_date:
            flash("Donation Date is required", "danger")
            has_error = True
        else:
            try:
                donation_date = datetime.datetime.strptime(donation_date, "%Y-%m-%d")
                thirty_days_ago = datetime.datetime.now() - datetime.timedelta(days=30)
                if donation_date < thirty_days_ago:
                    flash("Donation Date must be within the past 30 days", "danger")
                    has_error = True
            except ValueError:
                flash("Invalid date format for Donation Date", "danger")
                has_error = True

        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO donations (donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments)
                VALUES (%(donor_firstname)s, %(donor_lastname)s, %(donor_email)s, %(organization_id)s, %(item_name)s, %(item_description)s, %(item_quantity)s, %(donation_date)s, %(comments)s)
                """, request.form)# <-- TODO add-11 add query and add arguments
                #rv437-30/11/23

                if result.status:
                    flash("Created Donation Record", "success")
            except Exception as e:
                # TODO add-7 make message user friendly
                #rv437-30/11/23
                flash("There was an error creating the donation record", "danger")

    return render_template("manage_donation.html", donation=request.form)

@donations.route("/edit", methods=["GET", "POST"])
def edit():
    row = {}
     # TODO edit-1 request args id is required (flash proper error message)
     #rv437-30/11/23

    id = request.args.get("id")

    if not id:
        flash("Donation ID is required", "danger")
        return redirect(url_for("donations.search"))

    if request.method == "POST":
        
            # TODO add-2 retrieve form data for donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments
            # TODO add-3 donor_firstname is required (flash proper error message)
            # TODO add-4 donor_lastname is required (flash proper error message)
            # TODO add-5 donor_email is required (flash proper error message)
            # TODO add-5a email must be in proper format (flash proper message)
            # TODO add-6 organization_id is required (flash proper error message)
            # TODO add-7 item_name is required (flash proper error message)
            # TODO add-8 item_description is optional
            # TODO add-9 item_quantity is required and must be more than 0 (flash proper error message)
            # TODO add-10 donation_date is required and must be within the past 30 days
            # TODO add-11 comments are optional
            #rv437-30/11/23
        donor_firstname = request.form.get("donor_firstname")
        donor_lastname = request.form.get("donor_lastname")
        donor_email = request.form.get("donor_email")
        organization_id = request.form.get("organization_id")
        item_name = request.form.get("item_name")
        item_description = request.form.get("item_description")
        item_quantity = request.form.get("item_quantity")
        donation_date = request.form.get("donation_date")
        comments = request.form.get("comments")
        #rv437-30/11/23

        has_error = False

        if not donor_firstname:
            flash("Donor First Name is required", "danger")
            has_error = True

        if not donor_lastname:
            flash("Donor Last Name is required", "danger")
            has_error = True

        if not donor_email:
            flash("Donor Email is required", "danger")
            has_error = True
        elif "@" not in donor_email:
            flash("Invalid email format", "danger")
            has_error = True
        #rv437-30/11/23

        if not organization_id:
            flash("Organization ID is required", "danger")
            has_error = True

        if not item_name:
            flash("Item Name is required", "danger")
            has_error = True

        if not item_quantity or int(item_quantity) <= 0:
            flash("Item Quantity must be greater than 0", "danger")
            has_error = True

        if not donation_date:
            flash("Donation Date is required", "danger")
            has_error = True
        else:
            try:
                donation_date = datetime.datetime.strptime(donation_date, "%Y-%m-%d")
                thirty_days_ago = datetime.datetime.now() - datetime.timedelta(days=30)
                if donation_date < thirty_days_ago:
                    flash("Donation Date must be within the past 30 days", "danger")
                    has_error = True
            except ValueError:
                flash("Invalid date format for Donation Date", "danger")
                has_error = True

        if not has_error:
            try:
                # TODO edit-12 fill in proper update query
                #rv437-30/11/23
                result = DB.update("""
                UPDATE IS601_MP3_Donations SET
                donor_firstname = %(donor_firstname)s,
                donor_lastname = %(donor_lastname)s,
                donor_email = %(donor_email)s,
                organization_id = %(organization_id)s,
                item_name = %(item_name)s,
                item_description = %(item_description)s,
                item_quantity = %(item_quantity)s,
                donation_date = %(donation_date)s,
                comments = %(comments)s
                WHERE id = %(id)s
                """, request.form)

                if result.status:
                    flash("Updated record", "success")
            except Exception as e:
                # TODO edit-13 make this user-friendly
                #rv437-30/11/23
                flash("There was an error updating the donation record", "danger")

    try:
        # TODO edit-14 fetch the updated data 
        #rv437-30/11/23
        result = DB.selectOne("""
        SELECT id, donor_firstname, donor_lastname, donor_email, organization_id, 
               item_name, item_description, item_quantity, donation_date, comments
        FROM IS601_MP3_Donations
        WHERE id = %s
        """, id)

        if result.status:
            row = result.row
    except Exception as e:
        # TODO edit-15 make this user-friendly
        #rv437-30/11/23
        flash("There was an error fetching donation data", "danger")

    return render_template("manage_donation.html", donation=row)

@donations.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 if id is missing, flash necessary message and redirect to search
    # TODO delete-2 delete donation by id (fetch the id from the request)
    # TODO delete-3 ensure a flash message shows for successful delete
    # TODO delete-4 pass all argument except id to this route
    # TODO delete-5 redirect to donation search
    #rv437-30/11/23
    id = request.args.get("id")

    if not id:
        flash("Donation ID is required", "danger")
        return redirect(url_for("donations.search"))

    try:
        # delete-2: Delete donation by id
        #rv437-30/11/23
        result = DB.delete("""
        DELETE FROM IS601_MP3_Donations
        WHERE id = %s
        """, id)

        if result.status:
            flash("Deleted record successfully", "success")
    except Exception as e:
        flash("There was an error deleting the donation record", "danger")
        # return redirect(url_for("donations.search", **args))
        #rv437-30/11/23

    return redirect(url_for("donations.search"))
