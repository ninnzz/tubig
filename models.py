import datetime
from flask_sqlalchemy import SQLAlchemy

__all__ = ['User', 'Stats']

db = SQLAlchemy()


class User(db.Model):
    
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), default=None)
    mobile_number = db.Column(db.String(64), unique=True, nullable=False)
    token = db.Column(db.String(128), default=None)
    created_at = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, user_obj):
        self.id = user_obj['id']
        self.name = user_obj['name']
        self.mobile_number = user_obj['mobile_number']
        self.token = user_obj['token']
        self.created_at = datetime.datetime.utcnow()


class Stats(db.Model):
    
    __tablename__ = 'stats'

    id = db.Column(db.Integer, primary_key=True)
    water_level = db.Column(db.Integer, default=None)
    water_speed = db.Column(db.Integer, default=None)
    location = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, stats_obj):
        self.id = stats_obj['id']
        self.water_level = stats_obj['water_level']
        self.water_speed = stats_obj['water_speed']
        self.location = stats_obj['location']
        self.created_at = datetime.datetime.utcnow()
