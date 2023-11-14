from flask_restful import Resource
from config import api

class Designer(Resource):
    def get(self):
        return {"message": "This is the designers route!"}
    
api.add_resource(Designer, "/api/designers") #use /api here to separate backend routes from frontend routes because they will be on one domain