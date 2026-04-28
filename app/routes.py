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
        match = Match(
            agent=form.agent.data,
            kills=form.kills.data,
            deaths=form.deaths.data,
            assists=form.assists.data,
            result=form.result.data,
            map=form.map.data,
            my_team_score=form.my_team_score.data,
            enemy_team_score=form.enemy_team_score.data,
            rank_before=form.rank_before.data,
            rank_after=form.rank_after.data,
            rr_change=form.rr_change.data
        )
        db.session.add(match)
        db.session.commit()
        flash('Match logged successfully!')
        return redirect(url_for('index'))
    return render_template('add_match.html', title='Add Match', form=form)

@app.route('/delete_match/<int:id>', methods=['POST'])
def delete_match(id):
    match = db.first_or_404(sa.select(Match).where(Match.id == id))
    db.session.delete(match)
    db.session.commit()
    flash('Match Deleted')
    return redirect(url_for('index'))