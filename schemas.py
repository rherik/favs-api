from marshmallow import Schema, fields

class AlbumSchema(Schema):
    id = fields.Int(dump_only=True)
    foto = fields.Str(required=True)
    name = fields.Str(required=True)
    kind = fields.Str(required=True)
    creator = fields.Str(required=True)
    release_date = fields.Date(required=True)
    description = fields.Str(required=True)
    rate = fields.Int(required=True)

class AlbumUpdateSchema(Schema):
    foto = fields.Str(required=False)
    name = fields.Str(required=False)
    kind = fields.Str(required=False)
    creator = fields.Str(required=False)
    release_date = fields.Date(required=False)
    description = fields.Str(required=False)
    rate = fields.Int(required=False)

