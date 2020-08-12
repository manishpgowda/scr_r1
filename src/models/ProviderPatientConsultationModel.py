# src/models/PatientMasterModel.py
from marshmallow import fields, Schema
import datetime

from ..shared.DBUtil import DBUtil
from . import db


class ProviderPatientConsultationModel(db.Model):
    """
    ProviderPatientConsultationModel Model
    """
    # table name
    __tablename__ = 'provider_patient_consultation'
    __table_args__ = {"schema": "scs"}

    consultation_id = db.Column(db.Integer, primary_key=True)
    clinic_id = db.Column(db.Integer, nullable=True)
    provider_id = db.Column(db.Integer, nullable=True)
    consultation_type = db.Column(db.String(50), nullable=False)
    op_id = db.Column(db.Integer, nullable=False)
    appointment_id = db.Column(db.Integer, nullable=True)
    person_id = db.Column(db.Integer, nullable=True)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    consultation_summary = db.Column(db.String(1000), nullable=False)
    case_sheet_no = db.Column(db.String(10), nullable=False)
    case_sheet_id = db.Column(db.String(10), nullable=False)
    case_sheet_upload_time = db.Column(db.DateTime, nullable=False)


    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.consultation_id = data.get('consultation_id')
        self.clinic_id = data.get('clinic_id')
        self.provider_id = data.get('provider_id')
        self.consultation_type = data.get('consultation_type')
        self.op_id = data.get('op_id')
        self.appointment_id = data.get('appointment_id')
        self.person_id = data.get('person_id')
        self.start_time = datetime.datetime.now()
        self.end_time = datetime.datetime.now()
        self.consultation_summary = data.get('consultation_summary')
        self.case_sheet_no = data.get('case_sheet_no')
        self.case_sheet_id = data.get('case_sheet_id')
        self.case_sheet_upload_time = datetime.datetime.now()


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
    def get_all_provider_patient_consultation():
        return ProviderPatientConsultationModel.query.all()

    @staticmethod
    def load_appointment_list_of_patients_by_provider_id_by_date(_provider_id, date):
        dbobj = DBUtil()
        fun_call = "SELECT * FROM scs.get_appointments_by_provider_id({0}, 'date')".format(_provider_id, date)
        return dbobj.execute_custom_function(fun_call)

    @staticmethod
    def load_provider_list_in_book_new_patients():
        dbobj = DBUtil()
        fun_call = "SELECT * FROM scs.get_provider_list_in_book_new_appointment()".format()
        return dbobj.execute_custom_function(fun_call)

    @staticmethod
    def load_recent_consultation(_clinic_id, _provider_id):
        dbobj = DBUtil()
        fun_call = "SELECT * FROM scs.get_recent_consultation_by_clinic_id_and_provider_id({0},{1})".format(_clinic_id, _provider_id)
        return dbobj.execute_custom_function(fun_call)

    @staticmethod
    def load_appointment_report_by_date_range(_clinic_id, _provider_id, _date_from, _date_to):
        dbobj = DBUtil()
        fun_call = "SELECT * FROM scs.get_appointment_report_by_date_range({0},{1},'{2}','{3}')".format(_clinic_id, _provider_id, _date_from, _date_to)
        return dbobj.execute_custom_function(fun_call)


    @staticmethod
    def __repr(self):
        return '<speciality_id {}>'.format(self.speciality_id)

class ProviderConsultationSchema(Schema):
    consultation_id = fields.Integer(required=False)
    clinic_id = fields.Integer(required=False)
    provider_id = fields.Integer(required=False)
    consultation_type = fields.Str(required=False,missing=None)
    op_id = fields.Integer(required=False)
    appointment_id = fields.Integer(required=False)
    person_id = fields.Integer(required=False)
    start_time = fields.DateTime(required=False,missing=datetime.datetime.now())
    end_time = fields.DateTime(required=False,missing=datetime.datetime.now())
    consultation_summary = fields.Str(required=False,missing=None)
    case_sheet_no = fields.Str(required=False,missing=None)
    case_sheet_id = fields.Str(required=False,missing=None)
    case_sheet_upload_time = fields.DateTime(required=False,missing=datetime.datetime.now())