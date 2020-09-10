# # import json
# # import dateutil.parser
# # import babel
# from flask import Flask
# #, render_template, request, Response, flash, redirect, url_for, abort, jsonify
# from flask_moment import Moment
# from flask_sqlalchemy import SQLAlchemy
# # import logging
# # from logging import Formatter, FileHandler
# # from flask_wtf import Form
# # from forms import *
# from flask_migrate import Migrate
# # from sqlalchemy import func, and_
# # from config import db


# app = Flask(__name__)
# moment = Moment(app)
# app.config.from_object('config')
# db = SQLAlchemy(app)

# migrate = Migrate(app, db)

# #--------------------------------#
# # Models
# #--------------------------------#

# class Venue(db.Model):
#     __tablename__ = 'venues'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     city = db.Column(db.String(120))
#     state = db.Column(db.String(120))
#     address = db.Column(db.String(120))
#     phone = db.Column(db.String(120))
#     genres = db.Column(db.ARRAY(db.String))
#     image_link = db.Column(db.String(500))
#     website_link = db.Column(db.String(500))
#     facebook_link = db.Column(db.String(500))
#     seeking_talent = db.Column(db.Boolean)
#     seeking_description = db.Column(db.String)
#     shows = db.relationship('Show', backref='venue', lazy=True)

#     def get_venue(self, city, state):
#         return self.query.filter(self.city == city, self.state == state).all()

#     def __repr__ (self):
#         return f'<Venue id {self.id}, Venue name {self.name}, Venue city {self.city}, Venue state {self.state}, Venue genres {self.genres}, Venue shows {self.shows}>'


# class Artist(db.Model):
#     __tablename__ = 'artists'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     city = db.Column(db.String(120))
#     state = db.Column(db.String(120))
#     phone = db.Column(db.String(120))
#     genres = db.Column(db.ARRAY(db.String))
#     image_link = db.Column(db.String(500))
#     website_link = db.Column(db.String(500))
#     facebook_link = db.Column(db.String(500))
#     seeking_venue = db.Column(db.Boolean)
#     seeking_description = db.Column(db.String)
#     shows = db.relationship('Show', backref='artist', lazy=True)

#     def __repr__ (self):
#       return f'<Artist id {self.id}, Artist name {self.name}, Artist city {self.city}, Artist state {self.state}, Artist shows {self.shows}, Artist genres {self.genres}>'


# class Show(db.Model):
#   __tablename__ = 'shows'

#   id = db.Column(db.Integer, primary_key=True)
#   venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)
#   artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
#   start_time = db.Column(db.DateTime, nullable=False)

#   def __repr__ (self):
#     return f'<ShowID {self.id}, artist_id {self.artist_id}, venue_id {self.venue_id} start_time {self.start_time}>'
