# src/models/PatientMasterModel.py
from marshmallow import fields, Schema
import datetime
from . import db
from ..shared.CommonUtil import CommonUtil
from ..shared.DBUtil import DBUtil

class PatientMasterModel(db.Model):
    """
    PatientMasterModel Model
    """
    # table name
    __tablename__ = 'patient_master'
    __table_args__ = {"schema": "scs"}

    person_id = db.Column(db.Integer, primary_key=True)
    person_no = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    phone_no = db.Column(db.String(20),unique=True, nullable=False)
    email_id = db.Column(db.String(100), unique=True, nullable=False)
    sex = db.Column(db.String(5), nullable=False)
    date_of_birth = db.Column(db.DateTime,nullable=False)
    em_contact_no = db.Column(db.String(20),unique=True, nullable=False)
    em_contact_name = db.Column(db.String(100), nullable=False)
    em_contact_rel = db.Column(db.String(100), nullable=False)
    family_name = db.Column(db.String(100), nullable=False)
    image_id = db.Column(db.String(100), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    is_terms_accepted = db.Column(db.Boolean, nullable=False)
    is_email_verified = db.Column(db.Boolean, nullable=False)
    created_by = db.Column(db.String(50), nullable=True)
    create_time = db.Column(db.DateTime, nullable=False )
    modify_by = db.Column(db.String(50), nullable=True)
    modify_time = db.Column(db.DateTime, nullable=False)
    mob_app_otp = db.Column(db.String(10), nullable=True)
    mob_app_otp_time = db.Column(db.DateTime,nullable=True)
    is_mob_app_otp_valid = db.Column(db.Boolean, nullable=False)
    primary_clinic_id = db.Column(db.Integer,nullable=True)
    delete_ind = db.Column(db.Boolean, nullable=False)
    blood_group = db.Column(db.String(10), nullable=False)

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
        self.person_id = data.get('person_id')
        self.person_no = data.get('person_no')
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')
        self.phone_no = data.get('phone_no')
        self.email_id = data.get('email_id')
        self.sex = data.get('sex')
        self.date_of_birth = data.get('date_of_birth')
        self.em_contact_no = data.get('em_contact_no')
        self.em_contact_name = data.get('em_contact_name')
        self.em_contact_rel = data.get('em_contact_rel')
        self.family_name = data.get('family_name')
        self.image_id = data.get('image_id')
        self.is_active = data.get('is_active')
        self.is_terms_accepted = data.get('is_terms_accepted')
        self.is_email_verified = data.get('is_email_verified')
        self.created_by = data.get('created_by')
        self.create_time = datetime.datetime.now()
        self.modify_by = data.get('modify_by')
        self.modify_time = datetime.datetime.now()
        self.mob_app_otp = data.get('mob_app_otp')
        self.mob_app_otp_time = data.get('mob_app_otp_time')
        self.is_mob_app_otp_valid = data.get('is_mob_app_otp_valid')
        self.primary_clinic_id = data.get('primary_clinic_id')
        self.delete_ind = data.get('delete_ind')
        self.blood_group = data.get('blood_group')

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
    def get_all_patients():
        return PatientMasterModel.query.filter_by(delete_ind=False).all()

    @staticmethod
    def get_patient_by_id(_person_id):
        return PatientMasterModel.query.filter_by(person_id=_person_id,delete_ind=False).first()

    @staticmethod
    def get_patient_by_phone(_phone_no):
        return PatientMasterModel.query.filter_by(phone_no=_phone_no,delete_ind=False).first()

    @staticmethod
    def get_patient_list(_clinic_id,_provider_id,_user_type,_age_from, _age_to):
        dbobj = DBUtil()
        fun_call = "SELECT * FROM scs.get_patient_list({0},{1},'{2}',{3},{4})"\
            .format(_clinic_id,_provider_id,_user_type,_age_from,_age_to)
        return dbobj.execute_custom_function(fun_call)

    @staticmethod
    def get_patient_directory(_clinic_id, _provider_id,_user_type, _age_from, _age_to):
        dbobj = DBUtil()
        fun_call = "SELECT * FROM scs.get_patient_directory({0},{1},'{2}',{3},{4})" \
            .format(_clinic_id, _provider_id, _user_type, _age_from, _age_to)
        return dbobj.execute_custom_function(fun_call)

    @staticmethod
    def get_next_patient_upn(_clinic_id):
        dbobj = DBUtil()
        fun_call = "SELECT * FROM scs.get_next_patient_number({0})"\
            .format(_clinic_id)
        temp_res = dbobj.execute_custom_function(fun_call)
        return temp_res[0][0]

    def __repr(self):
        return '<person_id {}>'.format(self.person_id)


class PatientMasterSchema(Schema):
    person_id = fields.Integer(required=False)
    person_no = fields.Str(required=True)
    first_name = fields.Str(required=False,missing=None)
    last_name = fields.Str(required=False,Missing=None)
    phone_no = fields.Str(required=True)
    email_id = fields.Email(required=False,missing=None)
    sex = fields.Str(required=False,missing=None)
    date_of_birth = fields.Date(required=False,missing=None)
    em_contact_no = fields.Str(required=False,missing=None)
    em_contact_name = fields.Str(required=False,missing=None)
    em_contact_rel = fields.Str(required=False,missing=None)
    family_name = fields.Str(required=False,missing=None)
    image_id = fields.Str(required=False,missing=None)
    is_active = fields.Bool(required=False,missing=True)
    is_terms_accepted = fields.Bool(required=False,missing=False)
    is_email_verified = fields.Bool(required=False,missing=False)
    created_by = fields.Str(required=False,missing=None)
    create_time = fields.DateTime(required=False,missing=datetime.datetime.now())
    modify_by = fields.Str(required=False,missing=None)
    modify_time = fields.DateTime(required=False,missing=datetime.datetime.now())
    mob_app_otp = fields.Str(required=False,missing=None)
    mob_app_otp_time = fields.DateTime(required=False, missing=None)
    is_mob_app_otp_valid = fields.Bool(required=False, missing=False)
    primary_clinic_id = fields.Int(required=False, missing=None)
    delete_ind = fields.Bool(required=False, missing=False)
    blood_group = fields.Str(required=False, missing=None)

    class Meta:
        dateformat = ("%d/%m/%Y")
        datetimeformat = ('%d/%m/%Y %H:%M:%S')