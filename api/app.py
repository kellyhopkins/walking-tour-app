from flask import Flask
from flask_restful import Api, reqparse
from flask_jwt import JWT

# from security import authenticate, identity

from resources.user import UserRegister
from resources.location import Location, LocationList
from resources.tour import Tour, TourList
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(UserRegister, '/users')
api.add_resource(LocationList, '/locations')
api.add_resource(Location, '/locations/<id>')
api.add_resource(TourList, '/tours')
api.add_resource(Tour, '/tours/<name>')
# api.add_resource(TourStop, '/tours/<name>')

# @app.route('/tours/<name>/add', methods=['POST'])
# def add_stop(tour)

# jwt = JWT(app, authenticate, identity)

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)