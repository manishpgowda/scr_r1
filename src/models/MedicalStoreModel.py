from marshmallow import fields, Schema
import datetime

from ..shared.DBUtil import DBUtil
from . import db

#clinicd_master
class MedicalStoreModel(db.Model):

    # table name
    __tablename__ = 'medical_store_master'
    __table_args__ = {"schema": "scs"}

    medical_store_id = db.Column(db.Integer, primary_key=True)
    medical_store_name = db.Column(db.String(100), nullable=False)
    phone_no = db.Column(db.String(20), unique=True, nullable=False)
    email_id = db.Column(db.String(100), unique=True, nullable=False)
    location_lat = db.Column(db.String(50), nullable=False)
    location_lon = db.Column(db.String(50), nullable=False)
    image_id = db.Column(db.String(100), nullable=False)
    medical_store_type = db.Column(db.String(50), nullable=False)
    region = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(500), nullable=False)
    contact_person = db.Column(db.String(100), nullable=False)
    contact_person_phone = db.Column(db.String(15), unique=True, nullable=False)
    user_name = db.Column(db.String(50), nullable=False)
    user_password = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    medical_store_validity_upto = db.Column(db.DateTime, nullable=True)
    delete_ind = db.Column(db.Boolean, nullable=False)
    created_by = db.Column(db.String(50), nullable=False)
    created_time = db.Column(db.DateTime, nullable=False)
    modified_by = db.Column(db.String(50), nullable=True)
    modified_time = db.Column(db.DateTime, nullable=False)
    opening_time = db.Column(db.DateTime, nullable=False)
    closing_time = db.Column(db.DateTime, nullable=False)

    # class constructor
    def __init__(self, data):
        self.medical_store_id = data.get('medical_store_id')
        self.medical_store_name = data.get('medical_store_name')
        self.phone_no = data.get('phone_no')
        self.email_id = data.get('email_id')
        self.location_lat = data.get('location_lat')
        self.location_lon = data.get('location_lon')
        self.image_id = data.get('image_id')
        self.medical_store_type = data.get('medical_store_type')
        self.region = data.get('region')
        self.city = data.get('city')
        self.contact_person = data.get('contact_person')
        self.contact_person_phone = data.get('contact_person_phone')
        self.user_name = data.get('user_name')
        self.user_password = data.get('user_password')
        self.is_active = data.get('is_active')
        self.medical_store_validity_upto = data.get('medical_store_validity_upto')
        self.delete_ind = data.get('delete_ind')
        self.created_by = data.get('created_by')
        self.created_time = datetime.datetime.now()
        self.modified_by = data.get('modified_by')
        self.modified_time = datetime.datetime.now()
        self.opening_time = datetime.datetime.now()
        self.closing_time = datetime.datetime.now()

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
    def get_all_medicals():
        return MedicalStoreModel.query.all()

    @staticmethod
    def get_medical_by_id(_medical_store_id):
        return MedicalStoreModel.query.filter_by(medical_store_id=_medical_store_id,delete_ind=False).first()

    @staticmethod
    def get_medical_by_phone(_phone_no):
        return MedicalStoreModel.query.filter_by(phone_no=_phone_no,delete_ind=False).first()

    # @staticmethod
    # def load_list_for_medical_page_in_admin():
    #     dbobj = DBUtil()
    #     fun_call = "SELECT * FROM scs.get_list_for_medical_store_page_in_admin_()".format()
    #     return dbobj.execute_custom_function(fun_call)

    @staticmethod
    def load_medical_stores_list(_location_lat, _location_lon, _date_pref, _medical_store_name, _page_no):
        dbobj = DBUtil()
        fun_call = "SELECT * FROM scs.get_not_connected_medical_stores('{0}','{1}','{2}','{3}',{4})".format(
            _location_lat, _location_lon, _date_pref, _medical_store_name, _page_no)
        return dbobj.execute_custom_function(fun_call)

    @staticmethod
    def load_detail_contact_person_in_medical_store_by_medical_id_in_admin(_medical_store_id):
        dbobj = DBUtil()
        fun_call = "SELECT * FROM scs.get_detail_contact_person_in_medical_store_by_medical_id_in_admin({0})".format(
            _medical_store_id)
        return dbobj.execute_custom_function(fun_call)


    def __repr(self):
        return '<medical_store_id {}>'.format(self.medical_store_id)

class MedicalStoreSchema(Schema):
    medical_store_id = fields.Integer(required=False)
    medical_store_name = fields.Str(required=False, missing=None)
    phone_no = fields.Str(required=True)
    email_id = fields.Email(required=False, missing=None)
    location_lat = fields.Str(required=False, missing=None)
    location_lon = fields.Str(required=False, missing=None)
    image_id = fields.Str(required=False, missing=None)
    medical_store_type = fields.Str(required=False, missing=None)
    region = fields.Str(required=False, missing=None)
    city = fields.Str(required=False, missing=None)
    contact_person = fields.Str(required=False, missing=None)
    contact_person_phone = fields.Str(required=False, missing=None)
    user_name = fields.Str(required=False, missing=None)
    user_password = fields.Str(required=False, missing=None)
    is_active = fields.Bool(required=False, missing=True)
    medical_store_validity_upto = db.Column(db.Time, nullable=False)
    delete_ind = fields.Bool(required=False, missing=True)
    created_by = fields.Str(required=False, missing=None)
    created_time = fields.DateTime(required=False, missing=datetime.datetime.now())
    modified_by = fields.Str(required=False, missing=None)
    modified_time = fields.DateTime(required=False, missing=datetime.datetime.now())
    opening_time = fields.Str(required=False, missing=None)
    closing_time = fields.Str(required=False, missing=None)