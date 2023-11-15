from config import api, db
from flask import request
from flask_restful import Resource
from models.models import Genre

class GenreResource(Resource):
    
    def get(self):
        genres = [genre.to_dict() for genre in Genre.query.all()]
        return genres, 200
    
    def post(self):
        genre = Genre(**request.get_json())
        db.session.add(genre)
        db.session.commit()
        return genre.to_dict(), 201
    
api.add_resource(GenreResource, "/api/genres") #use /api here to separate backend routes from frontend routes because they will be on one domain