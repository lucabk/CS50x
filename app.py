import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import date
from helpers import apology, login_required


# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///dani.db")


#global input validation
goals_valid_list = ["strong","mass","leaness","stamina"]
gender_list = ["male", "other", "female"]

#Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


#root page
@app.route("/")
def index():
    return render_template("index.html", current_page="home")

#aboutme
@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html", current_page="aboutme")


#register
@app.route("/register", methods=["GET", "POST"])
def register():

    max_date = date.today().strftime("%Y-%m-%d")

    if request.method == "POST":

        #input validation
        name = request.form.get("name")
        surname = request.form.get("surname")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        gender = request.form.get("gender")
        birthdate = request.form.get("birthdate")
        workouts = int(request.form.get("training"))
        email = request.form.get("email")
        username = request.form.get("username")
        goals = request.form.getlist("goal")


        #valori mancanti
        if not name or not surname or not password or not confirmation or not gender or not birthdate or not workouts or not email or not username or not goals:
            return apology("Missing input field")


        #controllo se non esiste giò lo username
        if len(db.execute('SELECT username FROM users WHERE username = ?', username)) > 0:
            return apology("Username already exist")

        #password diverse
        if password != confirmation:
            return apology("Password doesn't match")

        #hash the psw
        psw = generate_password_hash(password)

        #workouts range
        if workouts < 0 or workouts > 7:
            return apology("workouts must be between 0 and 7")

        #goals validation
        for goal in goals:
            if goal not in goals_valid_list:
                return apology("Invalid goal, pls don't hack: it's my first website from scratch")
        #trasformo la lista di obiettivi un un'unica stringa da inserire nel db (con separatore la virgola)
        goals_string = ','.join(goals)

        #gender_validation
        if gender not in gender_list:
            return apology("Invalid gender, pls don't hack: it's my first website from scratch")

        #inserisco i valori nel db
        db.execute("""INSERT INTO users (name, surname, gender, birth, workouts, password, email, username, goals)
                    VALUES (?,?,?,?,?,?,?,?,?)""", name, surname, gender, birthdate, workouts, psw, email, username, goals_string)

        #reindirizzo alla homepage
        return redirect("/login")


    return render_template("register.html", current_page="register", max_date=max_date)



#login
@app.route("/login", methods=["GET","POST"])
def login():

    # Forget any user_id
    session.clear()

    # User reached route via POST
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["password"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to profile page
        return redirect("/profile")


    # User reached route via GET
    else:
        return render_template("login.html", current_page="login")


#logout
@app.route("/logout")
def logout():

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


#reviews
@app.route("/reviews", methods=["GET", "POST"])
@login_required
def reviews():

    if request.method == "POST":

        title = request.form.get("title")
        comment = request.form.get("comments")

        if not title or not comment:
            return apology("Insert both title and comments")

        user_id = db.execute("SELECT username_id FROM reviews WHERE username_id = ?", session["user_id"])
        if user_id:
            return apology("You have already submitted a review")

        #date
        data = date.today().strftime("%Y-%m-%d")

        db.execute("""INSERT INTO reviews (username_id, date, title, comment)
                   VALUES (?,?,?,?)""", session["user_id"], data, title, comment)

        return redirect("/reviews")


    else:
        #db query
        query = db.execute("""SELECT username, reviews.date, title, comment
                           FROM reviews join users on users.id = username_id""")

        return render_template("reviews.html", current_page="reviews", query=query)


#booknow
@app.route("/booknow", methods=["GET","POST"])
@login_required
def booknow():

    min_date = date.today().strftime("%Y-%m-%d")

    if request.method == "POST":
        data = request.form.get("date_training")
        orario = request.form.get("time_training")
        info = request.form.get("info")

        if not data or not orario or not info:
            return apology("Invalid input")

        #a quanto pare serve AJAX ma non so come si usa :(
        try:
            db.execute("""INSERT INTO booking (id_name, date, time, info)
                       VALUES (?,?,?,?)""", session["user_id"], data, orario, info)

            return redirect("/profile")

        except ValueError:
            return apology("The selected date and time is already booked. Please choose a different time. Go back.",422)


    else:
        return render_template("booknow.html",min_date=min_date)


#profile
@app.route("/profile")
@login_required
def profile():

    #users db
    personal_info = db.execute("""SELECT name, surname, gender, birth, workouts, email, username, goals
                               FROM users WHERE id = ?""", session["user_id"])

    #recensioni db
    review =  db.execute("""SELECT reviews.date, title, comment FROM reviews join users
                                 on users.id = username_id where users.id = ?""", session["user_id"])

    #prenotazioni db
    appointment = db.execute("SELECT date, time, info FROM booking WHERE id_name = ?", session["user_id"])
    print(appointment)
    return render_template("profile.html", personal_info=personal_info, review=review, appointment=appointment)
