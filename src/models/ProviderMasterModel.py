from marshmallow import fields, Schema
import datetime
from . import db
from ..shared.CommonUtil import CommonUtil
from ..shared.DBUtil import DBUtil


#provider_master
class ProviderMasterModel(db.Model):
    """
    ProviderMasterModel Model
    """
    # table name
    __tablename__ = 'provider_master'
    __table_args__ = {"schema": "scs"}

    provider_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    phone_no = db.Column(db.String(20), unique=True, nullable=False)
    email_id = db.Column(db.String(80), unique=True, nullable=False)
    sex = db.Column(db.String(5), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    city = db.Column(db.String(500), nullable=False)
    region = db.Column(db.String(100), nullable=False)
    reg_no = db.Column(db.String(100), nullable=False)
    consult_startdate = db.Column(db.Date, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    degree_title = db.Column(db.String(500), nullable=False)
    provider_type = db.Column(db.String(50), nullable=False)
    speciality = db.Column(db.String(100), nullable=False)
    is_email_verified = db.Column(db.Boolean, nullable=False)
    is_terms_accepted = db.Column(db.Boolean, nullable=False)
    delete_ind = db.Column(db.Boolean, nullable=False)
    image_id = db.Column(db.String(200), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.String(50), nullable=False)
    modify_by = db.Column(db.String(50), nullable=False)
    modify_time = db.Column(db.DateTime, nullable=False)
    primary_clinic_id = db.Column(db.Integer, nullable=True)
    user_name = db.Column(db.String(50), nullable=False)
    user_password = db.Column(db.String(50), nullable=False)
    base_degree = db.Column(db.String(50), nullable=True)

    # class constructor
    def __init__(self, data):

        self.provider_id  = data.get('provider_id')
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')
        self.phone_no = data.get('phone_no')
        self.email_id = data.get('email_id')
        self.sex = data.get('sex')
        self.date_of_birth = data.get('date_of_birth')
        self.city = data.get('city')
        self.region = data.get('region')
        self.reg_no = data.get('reg_no')
        self.consult_startdate = datetime.datetime.now()
        self.is_active = data.get('is_active')
        self.degree_title  = data.get('degree_title')
        self.provider_type = data.get('provider_type')
        self.speciality = data.get('speciality')
        self.is_email_verified = data.get('is_email_verified')
        self.is_terms_accepted = data.get('is_terms_accepted')
        self.delete_ind = data.get('delete_ind')
        self.image_id = data.get('image_id')
        self.create_time = datetime.datetime.now()
        self.created_by = data.get('created_by')
        self.modify_by = data.get('modify_by')
        self.modify_time = datetime.datetime.now()
        self.primary_clinic_id = data.get('primary_clinic_id')
        self.user_name = data.get('user_name')
        self.user_password = data.get('user_password')
        self.base_degree = data.get('base_degree')


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
    def get_all_providers():
        return ProviderMasterModel.query.filter_by(delete_ind=False).all()

    @staticmethod
    def get_provider_by_id(_provider_id):
        return ProviderMasterModel.query.filter_by(provider_id =_provider_id,delete_ind=False).first()

    @staticmethod
    def get_provider_by_phone(_phone_no):
        return ProviderMasterModel.query.filter_by(phone_no=_phone_no,delete_ind=False).first()

    @staticmethod
    def get_provider_by_email(_email_id):
        return ProviderMasterModel.query.filter_by(email_id=_email_id, delete_ind=False).first()

    @staticmethod
    def get_provider_by_reg_no(_reg_no):
        return ProviderMasterModel.query.filter_by(reg_no=_reg_no, delete_ind=False).first()

    @staticmethod
    def get_provider_by_speciality(_speciality_name):
        return ProviderMasterModel.query.filter_by(speciality=_speciality_name,delete_ind=False,).all()
        #return ProviderMasterModel.query.filter(ProviderMasterModel.speciality == _speciality_name).all()

    @staticmethod
    def get_providers_list_by_spec(_person_id, _spec_id, _sort_id, _location_lat, _location_lon, _date, _provider_name,
                                   _page_no):
        dbobj = DBUtil()
        fun_call = "SELECT * FROM scs.get_providers_by_spec({0},{1},{2},'{3}','{4}','{5}','{6}',{7})".format(_person_id,
        _spec_id, _sort_id, _location_lat,_location_lon,_date, _provider_name, _page_no)
        return dbobj.execute_custom_function(fun_call)

    @staticmethod
    def get_provider_list(_clinic_id, _user_type):
        dbobj = DBUtil()
        fun_call = "SELECT * FROM scs.get_provider_list({0},'{1}')" \
            .format(_clinic_id, _user_type)
        return dbobj.execute_custom_function(fun_call)

    @staticmethod
    def load_provider_list_in_book_new_appointment(_clinic_id):
        dbobj = DBUtil()
        fun_call = "SELECT * FROM scs.get_provider_list_in_book_new_appointment({0})".format(_clinic_id)
        return dbobj.execute_custom_function(fun_call)

    @staticmethod
    def load_bookmarked_patients_by_provider_id(_provider_id):
        dbobj = DBUtil()
        fun_call = "SELECT * FROM scs.get_bookmarked_patient_details({0})".format(_provider_id)
        return dbobj.execute_custom_function(fun_call)

    @staticmethod
    def load_follow_up_patients_by_provider_id(_provider_id):
        dbobj = DBUtil()
        fun_call = "SELECT * FROM scs.get_follow_up_patient_details({0})".format(_provider_id)
        return dbobj.execute_custom_function(fun_call)

    @staticmethod
    def load_provider_list_in_web_admin_provider_section():
        dbobj = DBUtil()
        fun_call = "SELECT * FROM scs.get_provider_list_in_web_admin_provider_section()".format()
        return dbobj.execute_custom_function(fun_call)

    def __repr(self):
        return '<provider_id {}>'.format(self.provider_id)


class ProviderMasterSchema(Schema):
    provider_id = fields.Integer(required=False)
    first_name = fields.Str(required=False, missing=None)
    last_name = fields.Str(required=False, Missing=None)
    phone_no = fields.Str(required=True)
    email_id = fields.Email(required=False, missing=None)
    sex = fields.Str(required=False, missing=None)
    date_of_birth = fields.Date(required=False, missing=None)
    city = fields.Str(required=False, missing=None)
    region = fields.Str(required=False, missing=None)
    reg_no = fields.Str(required=False, missing=None)
    consult_startdate = fields.Date(required=False, missing=datetime.datetime.today())
    is_active = fields.Bool(required=False, missing=True)
    degree_title = fields.Str(required=False, missing=None)
    provider_type = fields.Str(required=False, missing=None)
    speciality = fields.Str(required=False, missing=None)
    is_email_verified = fields.Bool(required=False, missing=True)
    is_terms_accepted = fields.Bool(required=False, missing=True)
    delete_ind = fields.Bool(required=False, missing=True)
    image_id = fields.Str(required=False, missing=None)
    create_time = fields.DateTime(required=False,missing=datetime.datetime.now())
    created_by = fields.Str(required=False, missing=None)
    modify_by = fields.Str(required=False, missing=None)
    modify_time = fields.DateTime(required=False,missing=datetime.datetime.now())
    primary_clinic_id = fields.Integer(required=False)
    user_name = fields.Str(required=False, missing=None)
    user_password = fields.Str(required=False, missing=None)
    base_degree = fields.Str(required=False, missing=None)

    class Meta:
        dateformat = ("%d/%m/%Y")
        datetimeformat = ('%d/%m/%Y %H:%M:%S')