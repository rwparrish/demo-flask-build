from config import db

class Game(db.Model):
    
    __tabename__ = "games"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    players = db.Column(db.Integer, nullable=False)
    time = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"<Game id={self.id} title={self.title} players={self.players} time={self.time}>"
