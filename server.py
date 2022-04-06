#Flask 
from audioop import reverse
import json
import re
from wsgiref.util import request_uri
from flask import Flask, jsonify,redirect,session,url_for,render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false
import search
from dbset import Feedback,app,db
import psycopg2
from flask import request

@app.route('/')
def takeornot():
    return render_template("takeornot.html")

@app.route('/decline')
def decline():
    return render_template('decline.html')

@app.route('/survey')
def survey():
    return render_template('survey.html')

@app.route('/Thanks',methods=['POST'])
def submit():
    if request.method =='POST':
        user = request.form['user']
        gender = request.form['gender']
        rating = request.form['rating']
        problem = request.form['problem']
        comments = request.form['comments']
        if user == '' or gender == ''or rating == '' or problem == '' or  comments=='':
            return render_template('survey.html',message='Required fields not Complete!')
        if db.session.query(Feedback).filter(Feedback.user == user).count() == 0:
            data = Feedback(user, gender, rating, problem, comments)
            db.session.add(data)
            db.session.commit()
            return render_template('main.html')
        return render_template('survey.html', message='Current use have already submitted!')



@app.route('/api/results')
def returningreverse():
    response=search.getallof()
    test = request.args.get("reverse")
    if (test):
        newlist = sorted(response,key=lambda k:k[0],reverse=True)
        # sorting = jsonify(newlist)
        return render_template('summary.html', title="results", jsonfile=json.dumps(newlist))
        # return render_template('summary.html',rows=sorting)
    # return jsonify(response)
    return render_template('summary.html', title="results", jsonfile=json.dumps(response))


if __name__ == "__main__":
    app.debug = True
    app.run()

