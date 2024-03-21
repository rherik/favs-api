from marshmallow import Schema, fields

class AlbumSchema(Schema):
    id = fields.Str(dump_only=True)
    foto = fields.Str(required=True)
    name = fields.Str(required=True)
    kind = fields.Str(required=True)
    creator = fields.Str(required=True)
    release_date = fields.Str(required=True)
    description = fields.Str(required=True)
    rate = fields.Integer(required=True)

class AlbumUpdateSchema(Schema):
    foto = fields.Str()
    name = fields.Str()
    kind = fields.Str()
    creator = fields.Str()
    release_date = fields.Str()
    description = fields.Str()
    rate = fields.Integer()

