from flask_restful import Resource
from config import api
from models.models import Designer


class DesignerResource(Resource):
    def get(self):
        designers = [designer.to_dict() for designer in Designer.query.all()]
        return designers, 200
    
api.add_resource(DesignerResource, "/api/designers") #use /api here to separate backend routes from frontend routes because they will be on one domain