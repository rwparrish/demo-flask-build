from config import db
from sqlalchemy_serializer import SerializerMixin


class Genre(db.Model, SerializerMixin):
    
    __tablename__ = "genres"
    
    id = db.Column(db.Integer, primary_key=True) #create a column called id with the type integer and set it as the primary key
    name = db.Column(db.String(30), nullable=False, unique=True) #create a column called name with the type string and set it as not nullable
    
    # One-to-many relationship - genre can have multiple games
    games = db.relationship("Game", back_populates="genre") #relationship is used to connect tables - use back_populates here instead of backref because backref will auto create a method on the other table
    # Many-to-many relationship - genre can have multiple designers through games 
    designers = db.relationship("Designer", secondary="games", viewonly=True, back_populates="genres") # a designer can have many genres and a genre can have many designers (THROUGH games) - use secondary to connect the two tables
    
    def __repr__(self):
        return f"<Genre id={self.id} name={self.name}>"
    