from application import db
from application.auth.models import User
from application.developer.models import Developer

from sqlalchemy.sql import text

class VideoGame(db.Model):

    __tablename__ = "videogame"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(144), nullable=False)
    releaseyear = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    developer_id = db.Column(db.Integer, db.ForeignKey('developer.id'), nullable=False)
    
    def __init__(self, name, year, genre, developer):
        self.name = name
        self.releaseyear = year
        self.genre = genre
        self.developer_id = developer

class GameInstance(db.Model):

    __tablename__ = "gameinstance"

    id = db.Column(db.Integer, primary_key=True)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                            nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('videogame.id'),
                        nullable=False)

    completed = db.Column(db.Boolean, nullable=False)

    def __init__(self, account_id, game_id):
        self.account_id = account_id
        self.game_id = game_id
        self.completed = False

    def find_games_by_user(account_id):
        stmt = text("SELECT videogame.id, videogame.name, videogame.genre, videogame.releaseyear, "
                    "videogame.developer_id FROM videogame INNER JOIN "
                    "gameinstance ON videogame.id = gameinstance.game_id "
                    "INNER JOIN account ON account.id = gameinstance.account_id "
                    "WHERE gameinstance.account_id = :acc_id "
                    "AND gameinstance.game_id = videogame.id").params(acc_id=account_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0],"name":row[1],"genre":row[2],"releaseyear":row[3], "developer_id":row[4]})
        
        return response

    def delete_games_by_user(account_id, game_id):
        stmt = text("DELETE FROM gameinstance WHERE "
                    "gameinstance.account_id = :account_id AND "
                    "gameinstance.game_id = :game_id").params(account_id=account_id, game_id=game_id)
        res = db.engine.execute(stmt)