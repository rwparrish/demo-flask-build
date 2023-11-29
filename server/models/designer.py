from config import db
from sqlalchemy_serializer import SerializerMixin


class Designer(db.Model, SerializerMixin):
    
    __tablename__ = "designers"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    # One-to-many relationship - designer can have multiple games
    games = db.relationship("Game", back_populates="designer")
    # Many-to-many relationship - designer can have multiple genres through games
    genres = db.relationship("Genre", secondary="games", viewonly=True, back_populates="designers") # a designer can have many genres and a genre can have many designers (THROUGH games) - use secondary to connect the two tables    
    
    def __repr__(self):
        return f"<Designer id={self.id} name={self.name}>"
    
    # serialize rules to exclude games and genres from the JSON response and help prevent recursion issues
    serialize_rules=(
        "-games.designer",
        "-games.genre",
        "-genres.designers",
        "-genres.games"
    )