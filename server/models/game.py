from config import db
from sqlalchemy_serializer import SerializerMixin


class Game(db.Model, SerializerMixin):
    
    __tablename__ = "games"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    players = db.Column(db.Integer, nullable=False)
    time = db.Column(db.Integer, nullable=False)
    designer_id = db.Column(db.Integer, db.ForeignKey("designers.id"), nullable=False) #table name.id is used for foreign keys
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"), nullable=False)
    
    # One-to-many relationship with Designer
    designer = db.relationship("Designer", back_populates="games") 
    # One-to-many relationship with Genre
    genre = db.relationship("Genre", back_populates="games") #relationship is used to connect tables - use back_populates here instead of backref because backref will auto create a method on the other table    
    
    def __repr__(self):
        return f"<Game id={self.id} title={self.title} players={self.players} time={self.time}>"

    serialize_rules=(
            "-designer.genres",
            "-designer.games",
            "-genre.designers",
            "-genre.games",
    )