from flask import render_template, request
from app import app
from models.event_planner import *
from models.event_class import Event

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events', methods=['POST'])
def add_event():
    event_date = request.form["date"]
    event_name = request.form["event_name"]
    event_guests = request.form["guests"]
    event_location = request.form["venue"]
    event_desc = request.form["description"]
    new_event = Event(event_date,event_name,event_guests,event_location,event_desc)
    add_new_event(new_event)
    return render_template('index.html', title='Home', events=events)
