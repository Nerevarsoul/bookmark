from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str()
    
    
user_schema = UserSchema(many=True)

