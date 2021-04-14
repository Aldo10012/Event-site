"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref
from datetime import datetime

class Guest(db.Model):
    """
    Guest() creates a model for a guest.
    guests can be created with a name, email, and phone.
    has relationship with Event()
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(80), nullable=False)

    events_attending = db.relationship('Event', secondary='table', back_populates='guests')


# STRETCH CHALLENGE: Add a field `event_type` as an Enum column that denotes the
# type of event (Party, Study, Networking, etc)

class Event(db.Model):
    """
    Event() creates a model for events
    events have titles, descriptions, time/date, 
    and has relationship with guest
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date_and_time = db.Column(db.DateTime(100), nullable=False)

    guests = db.relationship('Guest', secondary='table', back_populates="events_attending")

guest_event_table = db.Table( "table",
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
)
