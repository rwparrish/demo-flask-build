from flask import request 
from flask_restful import Resource
from config import api, db
from models.models import Designer


class DesignerResource(Resource):
    def get(self):
        designers = [designer.to_dict() for designer in Designer.query.all()]
        return designers, 200
    
    def post(self):
        designer = Designer(**request.get_json())
        db.session.add(designer) #add designer to the session / transaction
        db.session.commit() #add to the database
        return designer.to_dict(), 201
    
api.add_resource(DesignerResource, "/api/designers") #use /api here to separate backend routes from frontend routes because they will be on one domain