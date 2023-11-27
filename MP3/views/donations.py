import datetime
from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB

donations = Blueprint('donations', __name__, url_prefix='/donations')

@donations.route("/search", methods=["GET"])
def search():
    rows = []
    organization_name = ""
    
    query = """
    SELECT d.id, d.donor_firstname, d.donor_lastname, d.donor_email, d.organization_id, 
           d.item_name, d.item_description, d.item_quantity, d.donation_date, d.comments, 
           o.organization_name
    FROM donations d
    LEFT JOIN organizations o ON d.organization_id = o.id
    WHERE 1=1
    """
    args = {}

    allowed_columns = ["donor_firstname", "donor_lastname", "donor_email", "organization_name", "item_name", "item_quantity", "created", "modified"]

    # search-2 to search-10
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
        flash("There was an error retrieving donation data", "danger")

    return render_template("list_donations.html", organization_name=organization_name, rows=rows, allowed_columns=allowed_columns)

@donations.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # add-1 to add-10
        donor_firstname = request.form.get("donor_firstname")
        donor_lastname = request.form.get("donor_lastname")
        donor_email = request.form.get("donor_email")
        organization_id = request.form.get("organization_id")
        item_name = request.form.get("item_name")
        item_description = request.form.get("item_description")
        item_quantity = request.form.get("item_quantity")
        donation_date = request.form.get("donation_date")
        comments = request.form.get("comments")

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
                """, request.form)

                if result.status:
                    flash("Created Donation Record", "success")
            except Exception as e:
                flash("There was an error creating the donation record", "danger")

    return render_template("manage_donation.html", donation=request.form)

@donations.route("/edit", methods=["GET", "POST"])
def edit():
    row = {}

    id = request.args.get("id")

    if not id:
        flash("Donation ID is required", "danger")
        return redirect(url_for("donations.search"))

    if request.method == "POST":
        # edit-1 to edit-15
        donor_firstname = request.form.get("donor_firstname")
        donor_lastname = request.form.get("donor_lastname")
        donor_email = request.form.get("donor_email")
        organization_id = request.form.get("organization_id")
        item_name = request.form.get("item_name")
        item_description = request.form.get("item_description")
        item_quantity = request.form.get("item_quantity")
        donation_date = request.form.get("donation_date")
        comments = request.form.get("comments")

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
                # edit-12: fill in proper update query
                result = DB.update("""
                UPDATE donations SET
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
                flash("There was an error updating the donation record", "danger")

    try:
        # edit-14: fetch the updated data 
        result = DB.selectOne("""
        SELECT id, donor_firstname, donor_lastname, donor_email, organization_id, 
               item_name, item_description, item_quantity, donation_date, comments
        FROM donations
        WHERE id = %s
        """, id)

        if result.status:
            row = result.row
    except Exception as e:
        flash("There was an error fetching donation data", "danger")

    return render_template("manage_donation.html", donation=row)

@donations.route("/delete", methods=["GET"])
def delete():
    id = request.args.get("id")

    if not id:
        flash("Donation ID is required", "danger")
        return redirect(url_for("donations.search"))

    try:
        # delete-2: Delete donation by id
        result = DB.delete("""
        DELETE FROM donations
        WHERE id = %s
        """, id)

        if result.status:
            flash("Deleted record", "success")
    except Exception as e:
        flash("There was an error deleting the donation record", "danger")

    return redirect(url_for("donations.search"))
