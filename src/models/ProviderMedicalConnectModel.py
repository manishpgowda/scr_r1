from marshmallow import fields, Schema
import datetime

from ..shared.DBUtil import DBUtil
from . import db

#clinicd_master
class ProviderMedicalConnectModel(db.Model):

    # table name
    __tablename__ = 'provider_medical_store'
    __table_args__ = {"schema": "scs"}

    provider_id = db.Column(db.Integer, primary_key=True)
    medical_store_id = db.Column(db.Integer, nullable=False)
    connect_status = db.Column(db.Integer, nullable=False)
    request_date = db.Column(db.DateTime, nullable=False)
    status_change_date = db.Column(db.DateTime, nullable=False)
    is_default = db.Column(db.Boolean, nullable=False)
    created_by = db.Column(db.String(50), nullable=False)
    created_time = db.Column(db.DateTime, nullable=False)
    modified_by = db.Column(db.String(50), nullable=True)
    modified_time = db.Column(db.DateTime, nullable=False)


    # class constructor
    def __init__(self, data):
        self.provider_id = data.get('provider_id')
        self.medical_store_id = data.get('medical_store_id')
        self.connect_status = data.get('connect_status')
        self.request_date = data.get('request_date')
        self.status_change_date = data.get('status_change_date')
        self.is_default = data.get('is_default')
        self.created_by = data.get('created_by')
        self.created_time = datetime.datetime.now()
        self.modified_by = data.get('modified_by')
        self.modified_time = datetime.datetime.now()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modify_time = datetime.datetime.now()
        db.session.commit()

    def delete(self,data):
        self.delete_ind = True
        self.is_active = False
        db.session.commit()

    @staticmethod
    def load_provider_connected_to_medical_store(_medical_store_id):
        dbobj = DBUtil()
        fun_call = "SELECT * FROM scs.get_provider_connected_to_medical_store({0})".format(_medical_store_id)
        return dbobj.execute_custom_function(fun_call)


    def __repr(self):
        return '<medical_store_id {}>'.format(self.medical_store_id)

class ProviderMedicalConnectSchema(Schema):
    provider_id = fields.Integer(required=False)
    medical_store_id = fields.Integer(required=False)
    connect_status = fields.Integer(required=False)
    request_date = fields.DateTime(required=False, missing=datetime.datetime.now())
    status_change_date = fields.DateTime(required=False, missing=datetime.datetime.now())
    is_default = fields.Str(required=False, missing=None)
    created_by = fields.Str(required=False, missing=None)
    created_time = fields.DateTime(required=False, missing=datetime.datetime.now())
    modified_by = fields.Str(required=False, missing=None)
    modified_time = fields.DateTime(required=False, missing=datetime.datetime.now())
