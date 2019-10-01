import os
from app import app
from flask import render_template, request, redirect

events = [
        {"event":"First Day of Classes", "date":"2019-08-21"},
        {"event":"Winter Break", "date":"2019-12-20"},
        {"event":"Finals Begin", "date":"2019-12-01"}]
from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'test'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:tsul0w85xQtsdZJa@cluster0-3rv5u.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/input')
def input():
    return render_template('input.html')



# INDEX

@app.route('/')
@app.route('/index')

def index():
    #connects the events to the mongo database
    collection = mongo.db.events
    #finding all of the events (stored as events)
    events = list(collection.find({}))
    print(events)
    return render_template('index.html', events = events)



# CONNECT TO DB, ADD DATA

@app.route('/add')

def add():
    # connect to the database
    collections = mongo.db.events
    # insert new data
    collections.insert({"eventname":"Obama_commencement","date":"10/22/63"})
    # return a message to the user
    return "you added sumting to da database"

@app.route('/results', methods = ["Get", "Post"])
def results():
    userdata = dict(request.form)
    print(userdata)
    event_name = userdata['event_name']
    print(event_name)
    event_date = userdata['event_date']
    print(event_date)
    event_time = userdata['event_time']
    collection = mongo.db.events #connecting to the Mongo database (the events collection within the databse)
    print("#"*500, collection)
    #find the events in the collection, store them as a list of dictionaries, and assign to X.
    x = list(collection.find({})) #
    print(x)
    collection.insert({"name": event_name, "date": event_date, "time": event_time})
    return redirect("/")

@app.route('/deleteall')
def deleteall():
    #connect to mongo
    collections = mongo.db.events
    collections.delete_many({})
    return "I deleted your database mwahahahahah"
