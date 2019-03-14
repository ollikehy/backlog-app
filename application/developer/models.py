from application import db

from sqlalchemy.sql import text

class Developer(db.Model):

    __tablename__ = "developer"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(144), nullable=False)
    country = db.Column(db.String(144), nullable=True)

    games = db.relationship("VideoGame", backref='account', lazy=True)

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def find_developer_by_name(developer):
        stmt = text("SELECT developer.id FROM developer WHERE developer.name = :developer").params(developer=developer)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0]})

        return response