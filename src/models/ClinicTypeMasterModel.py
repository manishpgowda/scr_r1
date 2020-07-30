from marshmallow import fields, Schema
import datetime
from . import db

#clinic_type_master
class ClinicTypeMasterModel(db.Model):
    """
    ClinicTypeMasterModel Model
    """
    # table name
    __tablename__ = 'clinic_type_master'
    __table_args__ = {"schema": "scs"}

    clinic_type_id = db.Column(db.Integer, primary_key=True)
    clinic_type = db.Column(db.String(200), nullable=True)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        # self.name = data.get('name')
        # self.email = data.get('email')
        # self.password = data.get('password')
        # self.created_at = datetime.datetime.utcnow()
        # self.modified_at = datetime.datetime.utcnow()
        self.clinic_type_id = data.get('clinic_type_id')
        self.clinic_type = data.get('clinic_type')

class ClinicTypeMasterSchema(Schema):
    clinic_type_id = fields.Integer(required=False)
    clinic_type = fields.Str(required=False, missing=None)