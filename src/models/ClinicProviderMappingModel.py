from marshmallow import fields, Schema
import datetime
from . import db

#clinic_provider_mapping
class ClinicProviderMappingModel(db.Model):
    """
    ClinicProviderMapping Model
    """
    # table name
    __tablename__ = 'clinic_provider_mapping'
    __table_args__ = {"schema": "scs"}

    clinic_id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Boolean, nullable=False)
    delete_ind = db.Column(db.Boolean, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.String(50), nullable=False)
    modify_by = db.Column(db.String(50), nullable=False)
    modify_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, data):
        """
        Class constructor
        """
        # self.name = data.get('name')
        # self.email = data.get('email')
        # self.password = data.get('password')
        # self.created_at = datetime.datetime.utcnow()
        # self.modified_at = datetime.datetime.utcnow()
        self.clinic_id = data.get('clinic_id')
        self.provider_id = data.get('provider_id')
        self.is_active = data.get('is_active')
        self.delete_ind = data.get('delete_ind')
        self.create_time = datetime.datetime.now()
        self.created_by = data.get('created_by')
        self.modify_by = data.get('modify_by')
        self.modify_time = datetime.datetime.now()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modify_time = datetime.datetime.now()
        db.session.commit()

    def delete(self, data):
        self.delete_ind = True
        self.is_active = False
        db.session.commit()

    @staticmethod
    def get_all_mappings():
        return ClinicProviderMappingModel.query.all()

class ClinicProviderMappingSchema(Schema):
    clinic_id = fields.Integer(required=False, missing=True)
    provider_id = fields.Integer(required=False, missing=True)
    is_active = fields.Bool(required=False, missing=True)
    delete_ind = fields.Bool(required=False, missing=False)
    create_time = fields.DateTime(required=False, missing=datetime.datetime.now())
    created_by = fields.Str(required=False, missing=None)
    modify_by = fields.Str(required=False, missing=None)
    modify_time = fields.DateTime(required=False, missing=datetime.datetime.now())


