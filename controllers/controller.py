from flask import render_template
from app import app
from models.event_planner import *
from models.event_class import Event

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)