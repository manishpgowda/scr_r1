from marshmallow import fields, Schema
import datetime

from ..shared.DBUtil import DBUtil
from . import db

#clinicd_master
class ClinicMasterModel(db.Model):

    # table name
    __tablename__ = 'clinic_master'
    __table_args__ = {"schema": "scs"}

    clinic_id = db.Column(db.Integer, primary_key=True)
    clinic_name = db.Column(db.String(200), nullable=False)
    clinic_phone_no = db.Column(db.String(20), unique=True, nullable=False)
    email_id = db.Column(db.String(80), unique=True, nullable=False)
    location_lat = db.Column(db.String(50), nullable=False)
    location_lon = db.Column(db.String(50), nullable=False)
    image_id = db.Column(db.String(200), nullable=False)
    clinic_type = db.Column(db.String(20), nullable=False)
    region = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(500), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    clinic_validity_upto = db.Column(db.DateTime, nullable=False)
    delete_ind = db.Column(db.Boolean, nullable=False)
    created_by = db.Column(db.String(50), nullable=False)
    created_time = db.Column(db.DateTime, nullable=False)
    modified_by = db.Column(db.String(50), nullable=False)
    modified_time = db.Column(db.DateTime, nullable=False)
    reg_no = db.Column(db.String(100), nullable=False)
    opening_time = db.Column(db.Time, nullable=False)
    closing_time = db.Column(db.Time, nullable=False)
    monday_on = db.Column(db.Boolean, nullable=False)
    tuesday_on = db.Column(db.Boolean, nullable=False)
    wednesday_on = db.Column(db.Boolean, nullable=False)
    thursday_on = db.Column(db.Boolean, nullable=False)
    friday_on = db.Column(db.Boolean, nullable=False)
    saturday_on = db.Column(db.Boolean, nullable=False)
    sunday_on = db.Column(db.Boolean, nullable=False)
    clinic_tag = db.Column(db.String(10), nullable=False)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.clinic_id = data.get('clinic_id')
        self.clinic_name = data.get('clinic_name')
        self.clinic_phone_no = data.get('clinic_phone_no')
        self.email_id = data.get('email_id')
        self.location_lat = data.get('location_lat')
        self.location_lon = data.get('location_lon')
        self.image_id = data.get('image_id')
        self.clinic_type = data.get('clinic_type')
        self.region = data.get('region')
        self.city = data.get('city')
        self.is_active = data.get('is_active')
        self.clinic_validity_upto = data.get('clinic_validity_upto')
        self.delete_ind = data.get('delete_ind')
        self.created_by = data.get('created_by')
        self.created_time = datetime.datetime.now()
        self.modify_by = data.get('modify_by')
        self.modify_time = datetime.datetime.now()
        self.reg_no = data.get('reg_no')
        self.opening_time = data.get('opening_time')
        self.closing_time = data.get('closing_time')
        self.monday_on = data.get('monday_on')
        self.tuesday_on = data.get('tuesday_on')
        self.wednesday_on = data.get('wednesday_on')
        self.thursday_on = data.get('thursday_on')
        self.friday_on = data.get('friday_on')
        self.saturday_on = data.get('saturday_on')
        self.sunday_on = data.get('sunday_on')
        self.clinic_tag = data.get('clinic_tag')

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
    def get_all_clinics():
        return ClinicMasterModel.query.all()

    @staticmethod
    def get_clinic_by_id(_clinic_id):
        return ClinicMasterModel.query.filter_by(clinic_id=_clinic_id,delete_ind=False).first()

    @staticmethod
    def get_clinic_by_phone(_phone_no):
        return ClinicMasterModel.query.filter_by(clinic_phone_no=_phone_no,delete_ind=False).first()

    @staticmethod
    def get_clinic_list_and_search(_location_lat, _location_lon, _clinic_name, _page_no):
        dbobj = DBUtil()
        fun_call = "SELECT * FROM scs.get_list_of_clinics_search('{0}','{1}','{2}',{3})".format(_location_lat, _location_lon, _clinic_name, _page_no)
        return dbobj.execute_custom_function(fun_call)

    @staticmethod
    def load_list_for_clinics_page_in_admin():
        dbobj = DBUtil()
        fun_call = "SELECT * FROM scs.get_list_for_clinics_page_in_admin()".format()
        return dbobj.execute_custom_function(fun_call)

    @staticmethod
    def load_list_of_providers_clinics_page_in_admin_by_clinic_id_onclick_view_button(clinic_id):
        dbobj = DBUtil()
        fun_call = "SELECT * FROM get_list_of_providers_clinics_page_in_admin_by_clinic_id_onclic({0})".format(clinic_id)
        return dbobj.execute_custom_function(fun_call)

    def __repr(self):
        return '<clinic_id {}>'.format(self.clinic_id)

class ClinicMasterSchema(Schema):
    clinic_id = fields.Integer(required=False)
    clinic_name= fields.Str(required=False,missing=None)
    clinic_phone_no = fields.Str(required=False,missing=None)
    email_id = fields.Email(required=False,missing=None)
    location_lat = fields.Str(required=False,missing=None)
    location_lon = fields.Str(required=False,missing=None)
    image_id = fields.Str(required=False,missing=None)
    clinic_type = fields.Str(required=False,missing=None)
    region = fields.Str(required=False,missing=None)
    city = fields.Str(required=False,missing=None)
    is_active = fields.Bool(required=False,missing=True)
    clinic_validity_upto = fields.DateTime(required=False,missing=datetime.datetime.now())
    delete_ind = fields.Bool(required=False,missing=True)
    created_by = fields.Str(required=False,missing=None)
    created_time = fields.DateTime(required=False,missing=datetime.datetime.now())
    modified_by = fields.Str(required=False,missing=None)
    modified_time = fields.DateTime(required=False,missing=datetime.datetime.now())
    reg_no = fields.Str(required=False,missing=None)
    opening_time = db.Column(db.Time, nullable=False)
    closing_time = db.Column(db.Time, nullable=False)
    monday_on = fields.Bool(required=False,missing=True)
    tuesday_on = fields.Bool(required=False,missing=True)
    wednesday_on = fields.Bool(required=False,missing=True)
    thursday_on = fields.Bool(required=False,missing=True)
    friday_on = fields.Bool(required=False,missing=True)
    saturday_on = fields.Bool(required=False,missing=True)
    sunday_on = fields.Bool(required=False,missing=True)
    clinic_tag = fields.Str(required=False,missing=None)