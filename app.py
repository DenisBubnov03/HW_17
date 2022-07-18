# app.py

from flask import Flask, request
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields
from app.api.genre import genre_ns
from app.api.director import director_ns
from app.api.movie import movie_ns

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

api = Api(app)
api.add_namespace(director_ns)
api.add_namespace(genre_ns)
api.add_namespace(movie_ns)

if __name__ == '__main__':
    app.run(debug=True)
