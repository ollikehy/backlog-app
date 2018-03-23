from application import db

class VideoGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(144), nullable=False)
    releaseYear = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(50), nullable=False)

    def __init__(self, name, year, genre):
        self.name = name
        self.releaseYear = year
        self.genre = genre