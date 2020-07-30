# src/models/PatientMasterModel.py
from marshmallow import fields, Schema
import datetime
from . import db


class ProviderTypeMasterModel(db.Model):
    """
    ProviderTypeMasterModel Model
    """
    # table name
    __tablename__ = 'provider_type_master'
    __table_args__ = {"schema": "scs"}

    provider_type_id = db.Column(db.Integer, primary_key=True)
    provider_type = db.Column(db.String(100), nullable=True)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.provider_type_id = data.get('provider_type_id')
        self.provider_type = data.get('provider_type')

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all_provider_type():
        return ProviderTypeMasterModel.query.all()

class ProviderTypeMasterSchema(Schema):
    provider_type_id = fields.Integer(required=False)
    provider_type = fields.Str(required=True)