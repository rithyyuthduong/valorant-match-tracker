from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class MatchForm(FlaskForm):
    agent = StringField('Agent Name', validators=[DataRequired()])
    kills = IntegerField('Kills', validators=[DataRequired()])
    deaths = IntegerField('Deaths', validators=[DataRequired()])
    assists = IntegerField('Assists', validators=[DataRequired()])
    result = BooleanField('Result (Win?)')
    map = StringField('Map', validators=[DataRequired()])
    my_team_score = IntegerField('My Team', validators=[DataRequired()])
    enemy_team_score = IntegerField('Enemy Team', validators=[DataRequired()])
    rank_before = StringField('Rank Before', validators=[DataRequired()])
    rank_after = StringField('Rank After', validators=[DataRequired()])
    rr_change = IntegerField('RR Change', validators=[DataRequired(), NumberRange(min=-30, max=60)])
    submit = SubmitField('Log Match')