from datetime import datetime

class Event():
    def __init__(self, date, event_name, guests, room_location, description):
        self.date = date
        self.eventname = event_name
        self.guests = guests
        self.roomlocation = room_location
        self.description = description
