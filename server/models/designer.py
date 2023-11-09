from config import db

class Designer(db.Model):
    
    __tablename__ = "designers"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    
    def __repr__(self):
        return f"<Designer id={self.id} name={self.name}>"