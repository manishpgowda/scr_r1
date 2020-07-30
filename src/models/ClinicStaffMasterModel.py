from marshmallow import fields, Schema
import datetime

from ..shared.DBUtil import DBUtil
from . import db

#clinic_staff_master
class ClinicStaffMasterModel(db.Model):
    """
    ClinicStaffMasterModel Model
    """
    # table name
    __tablename__ = 'clinic_staff_master'
    __table_args__ = {"schema": "scs"}

    staff_id = db.Column(db.Integer, primary_key=True)
    clinic_id = db.Column(db.Integer, nullable=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    phone_no = db.Column(db.String(20), unique=True, nullable=False)
    email_id = db.Column(db.String(100), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    staff_type = db.Column(db.String(50), nullable=True)
    is_email_verified = db.Column(db.Boolean, nullable=False)
    user_name = db.Column(db.String(50), nullable=False)
    user_password = db.Column(db.String(50), nullable=False)
    delete_ind = db.Column(db.Boolean, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.String(50), nullable=True)
    modify_by = db.Column(db.String(50), nullable=True)
    modify_time = db.Column(db.DateTime, nullable=False)

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
        self.staff_id = data.get('staff_id')
        self.clinic_id = data.get('clinic_id')
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')
        self.phone_no = data.get('phone_no')
        self.email_id = data.get('email_id')
        self.is_active = data.get('is_active')
        self.staff_type = data.get('staff_type')
        self.is_email_verified = data.get('is_email_verified')
        self.user_name = data.get('user_name')
        self.user_password = data.get('user_password')
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

    def delete(self,data):
        self.delete_ind = True
        self.is_active = False
        db.session.commit()

    @staticmethod
    def get_all_clinic_staff():
        return ClinicStaffMasterModel.query.all()

    @staticmethod
    def get_clinic_staff_list(_clinic_id):
        return ClinicStaffMasterModel.query.filter_by(clinic_id=_clinic_id, delete_ind=False).all()

    @staticmethod
    def get_clinic_staff_by_id(_staff_id):
        return ClinicStaffMasterModel.query.filter_by(staff_id=_staff_id,delete_ind=False).first()

    @staticmethod
    def get_clinic_admin(_clinic_id):
        return ClinicStaffMasterModel.query.filter_by(clinic_id=_clinic_id, delete_ind=False,staff_type='CA').first()

    @staticmethod
    def get_staff_by_phone(_phone_no,_clinic_id):
        return ClinicStaffMasterModel.query.filter_by(phone_no=_phone_no,delete_ind=False,clinic_id=_clinic_id).first()

    @staticmethod
    def load_list_of_front_desk_staff_by_clinic_id_in_admin(_clinic_id):
        dbobj = DBUtil()
        fun_call = "SELECT * FROM scs.get_list_of_front_desk_staff_by_clinic_id_in_admin({0})".format(_clinic_id)
        return dbobj.execute_custom_function(fun_call)

    def __repr(self):
        return '<clinic_id {}>'.format(self.clinic_id)

class ClinicStaffMasterSchema(Schema):
    staff_id = fields.Integer(required=False)
    clinic_id = fields.Integer(required=False)
    first_name = fields.Str(required=False, missing=None)
    last_name = fields.Str(required=False, Missing=None)
    phone_no = fields.Str(required=True)
    email_id = fields.Email(required=False, missing=None)
    is_active = fields.Bool(required=False, missing=True)
    staff_type = fields.Str(required=False, Missing=None)
    is_email_verified = fields.Bool(required=False, missing=False)
    user_name = fields.Str(required=False, Missing=None)
    user_password = fields.Str(required=False, Missing=None)
    delete_ind = fields.Bool(required=False, missing=False)
    create_time = fields.DateTime(required=False, missing=datetime.datetime.now())
    created_by = fields.Str(required=False, missing=None)
    modify_by = fields.Str(required=False, missing=None)
    modify_time = fields.DateTime(required=False, missing=datetime.datetime.now())