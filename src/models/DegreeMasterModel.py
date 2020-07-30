from marshmallow import fields, Schema
import datetime
from . import db
from ..shared.CommonUtil import CommonUtil
from ..shared.DBUtil import DBUtil

class DegreeMasterModel(db.Model):
    __tablename__ = 'degree_master'
    __table_args__ = {"schema": "scs"}

    degree_id = db.Column(db.Integer, primary_key=True)
    degree_name = db.Column(db.String(10), unique=True, nullable=False)

    def __init__(self, data):
        self.degree_id = data.get('degree_id')
        self.degree_name = data.get('degree_name')

    @staticmethod
    def get_all_degrees():
        return DegreeMasterModel.query.all()

class DegreeMasterSchema(Schema):
    degree_id = fields.Integer(required=False)
    degree_name = fields.Str(required=True)