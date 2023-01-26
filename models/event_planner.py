from models.event_class import *
import datetime

event_1 = Event(datetime.date(2022,1,25), "Barrowlands Gig", 500, "Ballroom", "Local band")
event_2 = Event(datetime.date(2022,2,28), "Starset", 600, "Garage", "Main hall")

events = [event_1,event_2]

def add_new_event(new_event):
    events.append(new_event)