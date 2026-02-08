from config import ma 
from marshmallow import ValidationError ,validates_schema


class UserSchema(ma.Schema):
    email = ma.Email(required=True)
    password = ma.String(required=True, load_only=True)
    confirm_password = ma.String(required=True, load_only=True)
    
    @validates_schema
    def validate_data(self, data, **kwargs):
        if data["password"] != data["confirm_password"]:
            raise ValidationError("Passwords do not match", "confirm_password")
    
        data.pop("confirm_password")
        
        return data
