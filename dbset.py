#Flask 
from audioop import reverse
import json
import re
from wsgiref.util import request_uri
from flask import Flask, jsonify,redirect,session,url_for,render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false
import search
import psycopg2
from flask import request
import server

app = Flask(__name__)
db = SQLAlchemy(app)

app.debug = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ancdqlfdldvafg:f0dfff7b4625b9503ce0cd700a547ad7c87ad211f7ff163b3f6c93509757c423@ec2-44-193-188-118.compute-1.amazonaws.com:5432/d5bt1b4mojmt9s'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# model for the SQL
class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(200), unique=True)
    gender = db.Column(db.String(200))
    problem = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, user, gender, rating, problem, comments):
        self.user = user
        self.gender = gender
        self.rating = rating
        self.problem = problem
        self.comments = comments