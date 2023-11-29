from flask import request 
from flask_restful import Resource
from config import api, db
from models.models import Designer
from sqlalchemy.exc import IntegrityError


class DesignersResource(Resource):
    
    
    def get(self, id=None):
        if id == None:
            designers = [designer.to_dict() for designer in Designer.query.all()]
            return designers, 200
        else:
            designer = Designer.query.get(id)
            return designer.to_dict(), 200
        
    
    def post(self):
        designer = Designer(**request.get_json())
        try:
            db.session.add(designer) #add designer to the session / transaction
            db.session.commit() #add to the database
            return designer.to_dict(), 201
        except IntegrityError:
            return {"error": "Name has already been taken"}, 422 #flask sends over one error at time, formic will help with this on the frontend (errors that pertain to interacting with the database are handled backend)
    
api.add_resource(DesignersResource, "/api/designers", "/api/designers/<int:id>") #use /api here to separate backend routes from frontend routes because they will be on one domain

