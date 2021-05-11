from application import db


class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    conference = db.Column(db.String(5), nullable=False)
    rank = db.Column(db.Integer, nullable=False)
    players = db.relationship('Players', backref='team')

class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pl_name = db.Column(db.String(50), nullable=False)
    pl_position = db.Column(db.String(50), nullable=False)
    teamid= db.Column(db.Integer,db.ForeignKey('teams.id'), nullable=False)
    
    


    #change scheme(table) 