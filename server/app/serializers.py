from marshmallow import Schema, fields # , ValidationError, pre_load


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str()


class PostSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    body = fields.Str()
    user = fields.Nested(UserSchema)
    created_at = fields.DateTime(dump_only=True)
    
    
user_schema = UserSchema()
post_schema = PosrSchema()
