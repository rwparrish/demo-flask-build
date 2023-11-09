from config import db


class Genre(db.Model):
    
    __tablename__ = "genres"
    
    id = db.Column(db.Integer, primary_key=True) #create a column called id with the type integer and set it as the primary key
    name = db.Column(db.String(120), nullable=False) #create a column called name with the type string and set it as not nullable
    
    def __repr__(self):
        return f"<Genre id={self.id} name={self.name}>"
    
    
    
    
    