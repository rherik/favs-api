from db import db

class AlbumModel(db.Model):
    __tablename__ = "albuns"

    id = db.Column(db.Integer, primary_key=True)
    foto = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    kind = db.Column(db.String(15), nullable=False)
    creator = db.Column(db.String(80), nullable=False)
    release_date = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255))
    rate = db.Column(db.Float)