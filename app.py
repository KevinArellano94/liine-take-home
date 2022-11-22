#!/bin/python
from flask import Flask, render_template, jsonify
from restaurants import restaurants
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html', name='index', hours='10:00')

@app.route("/restaurants/", methods=["GET"])
def get_restaurants():
  return jsonify(restaurants = restaurants)

@app.route("/restaurants/<int:id>/", methods=["GET"])
def get_restaurants_per_id(id):
  for restaurant in restaurants:
    if restaurant.get('id') == id:
      return jsonify(restaurant)

@app.route("/restaurants/date/<string:date_time>/", methods=["GET"])
def get_restaurants_days_date_time(date_time):
  result = []

  new_date_time = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
  new_date_time = new_date_time.isoformat()

  date = new_date_time.split('T')[0]
  time = new_date_time.split('T')[1]
  
  weekday = datetime.strptime(date, '%Y-%m-%d').weekday()
  
  for restaurant in restaurants:
    name = restaurant.get('name')
    day_hours = restaurant.get('day_hours')
    opens = restaurant.get('opens')
    closes = restaurant.get('closes')

    for daily_hours in day_hours:
      opens = daily_hours['opens']
      closes = daily_hours['closes']

      if ( weekday == daily_hours['day'] ):
        if ( opens <= time ) and ( closes >= time ):
          result.append(
            {
              "name": name,
              "hours": opens + "-" + closes
            }
          )

        if ( opens > closes ):
          if ( opens <= time ) or ( closes >= time ):
            result.append(
              {
                "name": name,
                "hours": opens + "-" + closes
              }
            )
  return jsonify(result)

app.run( host="0.0.0.0", port=8080, debug=True )