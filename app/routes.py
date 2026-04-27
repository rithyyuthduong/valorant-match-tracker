from app import app, db
from flask import render_template, url_for, redirect, flash
import sqlalchemy as sa
from app.models import Match
from app.forms import MatchForm

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    matches = db.session.scalars(sa.select(Match)).all()
    return render_template('index.html', title='Match History', matches=matches)
        
@app.route('/add_match', methods=['GET', 'POST'])
def add_match():
    form = MatchForm()
    if form.validate_on_submit():
        match = db.session.scalar(sa.select(Match)).all()
        db.session.add(match)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', title='Add Match', form=form)