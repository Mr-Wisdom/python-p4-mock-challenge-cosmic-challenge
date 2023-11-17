#!/usr/bin/env python3

from models import db, Scientist, Mission, Planet
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask import Flask, make_response, jsonify, request
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

api = APi(app)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)


class Scientists(Resource):
    def get(self):
        scientists = [scientist.to_dict() for scientist in Scientist.query.all()]
        response = make_response(scientists, 200)
        return response
    def post(self):
        params = request.json
        new_scientist = Scientist(name = params['name'], field_of_study = params ['field_of_study'])
        db.session.add(new_scientist)
        db.session.commit()
        response = make_response(new_scientist.to_dict(),201)
        return response

api.add_resource(Scientists, '/scientists')
class ScientistsById(Resource):
    def get(self, id):
        if not scientists:
            return make_response({"error" : "Scientist not found"}, 404)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
