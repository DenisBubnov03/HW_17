from flask import request
from flask_restx import Namespace, Resource
from app.setup_db import db
from app.models import Genre, GenreSchema


genre_ns = Namespace('/genre')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        genre = Genre.query.all()
        return genre_schema.dump(genre), 200

    def post(self):
        req_json = request.json
        new_genre = Genre(**req_json)
        with db.session.begin():
            db.session.add(new_genre)
        return "", 201


@genre_ns.route('/<int:pk>/')
class GenreView(Resource):
    def get(self, pk):
        try:
            note = Genre.query.get(pk)
            return genre_schema.dump(note), 200
        except Exception as e:
            return str(e), 404

    def post(self):
        req_json = request.json
        new_genre = Genre(**req_json)
        with db.session.begin():
            db.session.add(new_genre)
        return "", 201

    def put(self, pk):
        nots = Genre.query.get(pk)
        req_json = request.json
        nots.author = req_json.get("Genre")
        db.session.add(nots)
        db.session.commit()
        return "", 204

    def delete(self, pk):
        user = Genre.query.get(pk)
        db.session.delete(user)
        db.session.commit()
        return "", 204