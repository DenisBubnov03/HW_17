from flask import request
from flask_restx import Namespace, Resource
from app.setup_db import db
from app.models import Director, DirectorSchema

director_ns = Namespace('/director')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)



############## DIRECTOR ##############
@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        director = Director.query.all()
        return director_schema.dump(director), 200

    def post(self):
        req_json = request.json
        new_director = Director(**req_json)
        with db.session.begin():
            db.session.add(new_director)
        return "", 201


@director_ns.route('/<int:pk>/')
class DirectorView(Resource):
    def get(self, pk):
        try:
            note = Director.query.get(pk)
            return director_schema.dump(note), 200
        except Exception as e:
            return str(e), 404

    def post(self):
        req_json = request.json
        new_director = Director(**req_json)
        with db.session.begin():
            db.session.add(new_director)
        return "", 201

    def put(self, pk):
        nots = Director.query.get(pk)
        req_json = request.json
        nots.author = req_json.get("Director")
        db.session.add(nots)
        db.session.commit()
        return "", 204

    def delete(self, pk):
        user = Director.query.get(pk)
        db.session.delete(user)
        db.session.commit()
        return "", 204