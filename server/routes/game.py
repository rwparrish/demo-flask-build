from config import api, db
from flask import request
from flask_restful import Resource
from models.models import Game
from sqlalchemy.exc import IntegrityError


class GameResource(Resource):
    
    def get(self):
        games = [game.to_dict() for game in Game.query.all()]
        return games, 200
    
    def post(self):
        game = Game(**request.get_json())
        try:
            db.session.add(game)
            db.session.commit()
            return game.to_dict(), 201
        except IntegrityError:
            return {"error": "Title has already been taken"}, 422
    
    
api.add_resource(GameResource, "/api/games") #use /api here to separate backend routes from frontend routes because they will be on one domain
    