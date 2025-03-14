from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from .tratamento import retorna_arquivo

from db import db
from models import AlbumModel
from schemas import AlbumSchema, AlbumUpdateSchema


blp = Blueprint("albuns", __name__, description="Operation on albuns")

# get one album
@blp.route("/album/<string:album_id>")
class Album(MethodView):
    @blp.response(200, AlbumSchema)
    # return the album that corresponds to id
    def get(self, album_id):
        album = AlbumModel.query.get_or_404(album_id)
        return album

    # delete the album that corresponds do id
    def delete(self, album_id): 
        album = AlbumModel.query.get_or_404(album_id)
        db.session.delete(album)
        db.session.commit()
        return {"message": "Album deleted."}
    
    # Keep original information if not informed new
    @blp.arguments(AlbumUpdateSchema)
    @blp.response(200, AlbumSchema)
    def patch(self, album_data, album_id):
        # Checa se há um album com esse id no banco de dados
        album = AlbumModel.query.get(album_id)
        if album:
            # Laço for para atribuir o valor à chave certa
            for key, value in album_data.items():
                setattr(album, key, value)
            db.session.add(album)
            db.session.commit()
            return album
        else:
            abort(400, message="Album id not found.")

# lists all albuns     
@blp.route("/albuns")
class AlbunsList(MethodView):
    @blp.response(200, AlbumSchema(many=True))
    # return all albuns
    def get(self):
        return AlbumModel.query.all()
    
    @blp.arguments(AlbumSchema)
    @blp.response(201, AlbumSchema)
    # insert a new album to database
    def post(self, album_data):
        # chamar a função retorna_arquivo aqui e passar o retorno para a coluna a album.foto
        # Ou jogar a função tratamento para o frontend
        #album = AlbumModel(**album_data)
        #fotoTratada = retorna_arquivo(arq=album_data['foto'])
        album = AlbumModel()
        album.name = album_data['name']
        #album.foto = fotoTratada
        album.foto = album_data['foto']
        album.kind = album_data['kind']
        album.creator = album_data['creator']
        album.release_date = album_data['release_date']
        album.description = album_data['description']
        album.rate = album_data['rate']

        db_album_name = AlbumModel.query.filter_by(name=album_data['name']).first()
        if db_album_name:
            abort(400, message="An album with this name already exists.")
        else:
            try:
                db.session.add(album)
                db.session.commit()
            except IntegrityError as e:
                abort(400, message=f"{e} ~~~ This album already exists.")
            except SQLAlchemyError as e:
                abort(500, message=f"{e} ~~~ An error occurred while inserting the album.")
            return album