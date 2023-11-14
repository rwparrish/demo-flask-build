from config import db


class Designer(db.Model):
    
    __tablename__ = "designers"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    # One-to-many relationship - designer can have multiple games
    games = db.relationship("Game", back_populates="designer")
    # Many-to-many relationship - designer can have multiple genres through games
    genres = db.relationship("Genre", secondary="games", viewonly=True, back_populates="designers") # a designer can have many genres and a genre can have many designers (THROUGH games) - use secondary to connect the two tables    
    
    def __repr__(self):
        return f"<Designer id={self.id} name={self.name}>"