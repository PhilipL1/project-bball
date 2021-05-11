from flask_wtf import FlaskForm #class that the forms clasess are going to inherit from so they need to be type form 
from wtforms import StringField, SubmitField
from wtforms.validators import Length 

class TeamForm(FlaskForm):
    form_name= StringField('Enter Team name: ', validators=[Length(min = 1)])
    form_city= StringField('Enter Team City: ', validators=[Length(min = 1)])
    form_conference= StringField('Enter Team Conference', validators=[Length(min = 1)])
    form_rank= StringField('Enter Team rank position: ', validators=[Length(min = 1)])
    submit=SubmitField('Add Team') # the botton
