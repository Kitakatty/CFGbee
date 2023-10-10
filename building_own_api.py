from flask import Flask, jsonify, request
from flights_data import flights
from utils import search_flight, get_index
app = Flask(__name__)


# GETTING INFORMATION

@app.route('/')
def hello():
    return {'hello': 'Universe'}

# get /flights returns list of avail flights
# define a /flights endpoint
@app.route('/flights')
def get_flights():
    return jsonify(flights)


# get /flights/id returns information about a specific flight
# define a /flights/ endpoint which accepts an id for flight we want

@app.route('/flights/<int:id>')
def get_flight_by_id(id):
    flight = search_flight(id, flights)
    return jsonify(flight)

# post endpoint to add a new flight
@app.route('/flights', methods=['POST'])
def add_flight():
    flight: object = request.get_json()
    flights.append(flight)
    return flight
# put edit or update a flight
@app.route('/flights/<int:id>', methods=['PUT'])
def update_flight(id):
    flight_to_update = request.get_json()
    index = get_index(id, flights)
    flights[index] = flight_to_update
    return jsonify(flight[index])

# delete delete a flight
@app.route('/flights/<int:id>', methods=['DELETE'])
def delete_flight(id):
    index = get_index(id, flights)
    deleted = flights.pop(index)
    return jsonify(deleted), 200


if __name__ == '__main__':
    app.run(debug=True)
