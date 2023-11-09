from config import app, db #need app context in order to seed database - why?
from models.models import *


with app.app_context():
    Genre.query.delete()
    db.session.commit()
    print("deleting genres")
    
    
    
    
    
    
    print('Seeding complete!')