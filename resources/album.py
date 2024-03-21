import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import AlbumModel
from schemas import AlbumSchema, AlbumUpdateSchema


blp = Blueprint("albuns", __name__, description="Operation on albuns")

# get one album
@blp.route("/album/<string:album_id>")
class Album(MethodView):
    @blp.response(200, AlbumSchema)
    def get(self, album_id):
        album = AlbumModel.query.get_or_404(album_id)
        return album

    def delete(self, album_id): 
        album = AlbumModel.query.get_or_404(album_id)
        db.session.delete(album)
        db.session.commit()
        return {"message": "Album deleted."}
    
    # Shoud keep original information if not informed new
    @blp.arguments(AlbumUpdateSchema)
    @blp.response(200, AlbumSchema)
    def put(self, album_data, album_name):
        album = AlbumModel.query.get(album_name)
        if album:
            album.foto = album_data["foto"]
            album.name = album_data["nome"]
            album.creator = album_data["creator"]
            album.release_date = album_data["release_date"]
            album.description = album_data["description"]
            album.rate = album_data["rate"]
        else:
            album = AlbumModel(**album_data)
        
        db.session.add(album)
        db.session.commit()
        return album


# lists all albuns     
@blp.route("/albuns")
class AlbunsList(MethodView):
    @blp.response(200, AlbumSchema(many=True))
    def get(self):
        return AlbumModel.query.all()
    
    @blp.arguments(AlbumSchema)
    @blp.response(201, AlbumSchema)
    def post(self, album_data):
        album = AlbumModel(**album_data)
        try:
            db.session.add(album)
            db.session.commit()
        except IntegrityError:
            abort(400, message="This album already exists.")
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the album.")
        return album