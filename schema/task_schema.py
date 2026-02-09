from config import ma 
from marshmallow import ValidationError ,validates_schema


class TaskSchema(ma.Schema):
    heading = ma.String(required=True)
    description = ma.String(required=True)
    status = ma.String(dump_only=True)
    is_complete = ma.Boolean(dump_only=True)

    @validates_schema
    def validate_data(self, data, **kwargs):
        if len(data["heading"] )< 2 :
            raise ValidationError("Heading is too short", "heading")
        
        if len(data["description"] ) <10 :
            raise ValidationError("description is too short", "description")
    
        
        return data
