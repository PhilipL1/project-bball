from application.forms import TeamForm
from application import app, db
from application.models import Players, Teams
from application.forms import TeamForm, PlayerForm 
from flask import render_template, request, redirect, url_for


@app.route("/")
@app.route("/home")
def home():
    all_teams = Teams.query.all()
    all_players = Players.query.all()
    output=""
    return render_template("index.html", title="Home", all_teams = all_teams, all_players = all_players)

@app.route("/create", methods=["GET", "POST"]) #allow get & post request 
def create():
    form=TeamForm()
    if request.method == "POST": #(check to see if the method a post request.)post request: send  the filled/complete info to the route
        if form.validate_on_submit():#check if the form validates 
            new_team = Teams(
                name = form.form_name.data, 
                city = form.form_city.data,
                conference = form.form_conference.data,
                rank = form.form_rank.data
            ) #check if new team has been added with the data
            db.session.add(new_team) # add the new team to the route 
            db.session.commit() # commit to the data base itself
            return redirect(url_for("home"))  #redirect back to the home page
    return render_template("add.html", title = "Create a Team", form=form) # display ftml file 

@app.route("/update/<int:id>", methods=["GET","POST"]) #buton will get the id & post request 
def update(id):
    form= TeamForm()
    team= Teams.query.filter_by(id=id).first()

    if request.method == 'GET':
        form.form_name.data = team.name # put data in the input box 
        form.form_city.data = team.city
        form.form_conference.data = team.conference
        form.form_rank.data = team.rank

    elif request.method =="POST": # id the form has been posted 
        team.name = form.form_name.data # refere to model.py && send to the data base 
        team.city = form.form_city.data
        team.conference = form.form_conference.data
        team.rank = form.form_rank.data
        db.session.commit()
        return redirect(url_for("home")) 
    return render_template("update.html", form=form, title="Update Team", team=team)
   
@app.route("/delete/<int:id>")
def delete(id):
    team=Teams.query.filter_by(id=id).first()
    for player in team.players: 
        db.session.delete(player)
    db.session.delete(team)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/player/<int:id>",methods=["GET", "POST"])  
def player(id):
    form=PlayerForm()
    if request.method == "POST": 
        if form.validate_on_submit():
            new_player = Players(
                pl_name = form.form_name.data,   # filling in each column 
                pl_position = form.form_position.data,
                teamid = id 
            ) 
            db.session.add(new_player) # add the new team to the route 
            db.session.commit() # commit to the data base itself
            return redirect(url_for("home"))  #redirect back to the home page
    return render_template("add-Player.html", title = "Add Players to your Teams", form=form) # display ftml file