# src/models/SpecialityMasterModel.py
from marshmallow import fields, Schema
import datetime
from . import db


class SpecialityMasterModel(db.Model):

    __tablename__ = 'speciality_master'
    __table_args__ = {"schema": "scs"}

    speciality_id = db.Column(db.Integer, primary_key=True)
    speciality_name = db.Column(db.String(200), nullable=False)
    created_by = db.Column(db.String(50), nullable=True)
    created_time = db.Column(db.DateTime, nullable=False)
    image_id = db.Column(db.String(100), nullable=False)

    # class constructor
    def __init__(self, data):
        self.speciality_id = data.get('speciality_id')
        self.speciality_name = data.get('speciality_name')
        self.created_by = data.get('created_by')
        self.created_time = data.get('created_time')
        self.image_id = data.get('image_id')

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all_specialities():
        return SpecialityMasterModel.query.all()

    @staticmethod
    def get_speciality_by_id(speciality_id):
        return SpecialityMasterModel.query.get(speciality_id)

    def __repr(self):
        return '<speciality_id {}>'.format(self.speciality_id)

class SpecialityMasterSchema(Schema):
    speciality_id = fields.Integer(required=False)
    speciality_name = fields.Str(required=True)
    create_time = fields.DateTime(required=False, missing=datetime.datetime.now())
    created_by = fields.Str(required=False, missing=None)
    image_id = fields.Str(required=False, missing=None)