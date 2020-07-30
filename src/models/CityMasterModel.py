# src/models/PatientMasterModel.py
from marshmallow import fields, Schema
import datetime
from . import db


class CityMasterModel(db.Model):

    __tablename__ = 'city_master'
    __table_args__ = {"schema": "scs"}

    city_id = db.Column(db.Integer, primary_key=True)
    city= db.Column(db.String(100), nullable=False)

    # class constructor
    def __init__(self, data):

        self.city_id = data.get('city_id')
        self.city = data.get('city')

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all_cities():
        return CityMasterModel.query.all()

class CityMasterSchema(Schema):
    city_id = fields.Integer(required=False)
    city = fields.Str(required=True)