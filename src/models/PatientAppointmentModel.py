from marshmallow import fields, Schema
import datetime

from ..shared.DBUtil import DBUtil
from . import db

#patient_appointment
class PatientAppointmentModel(db.Model):
    """
    PatientAppointmentModel Model
    """
    # table name
    __tablename__ = 'patient_appointment'
    __table_args__ = {"schema": "scs"}

    appointment_id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, nullable=True)
    person_no = db.Column(db.String(50), nullable=False)
    schedule_id = db.Column(db.Integer, nullable=True)
    clinic_id = db.Column(db.Integer, nullable=True)
    provider_id = db.Column(db.Integer, nullable=True)
    appointment_purpose = db.Column(db.String(200), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)
    slot_start = db.Column(db.DateTime, nullable=False)
    slot_end = db.Column(db.DateTime, nullable=False)
    slot_duration = db.Column(db.Integer, nullable=True)
    slot_tag = db.Column(db.String(50), nullable=False)
    is_priority = db.Column(db.Boolean, nullable=False)
    booking_time = db.Column(db.DateTime, nullable=False)
    booked_by = db.Column(db.String(50), nullable=False)
    booked_via = db.Column(db.String(50), nullable=False)
    booking_agent = db.Column(db.String(50), nullable=False)
    delete_ind = db.Column(db.Boolean, nullable=False)
    online_checkin_status = db.Column(db.Boolean, nullable=False)
    online_checkin_time = db.Column(db.DateTime, nullable=False)
    payment_status = db.Column(db.Boolean, nullable=False)
    clinic_checkin_status = db.Column(db.Boolean, nullable=False)
    clinic_checkin_time = db.Column(db.DateTime, nullable=False)
    clinic_checkin_by = db.Column(db.String(50), nullable=False)
    provider_consultation_status = db.Column(db.String(10), nullable=False)
    created_by = db.Column(db.String(50), nullable=False)
    created_time = db.Column(db.DateTime, nullable=False)
    modify_by = db.Column(db.String(50), nullable=False)
    modify_time = db.Column(db.DateTime, nullable=False)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.appointment_id = data.get('appointment_id')
        self.person_id = data.get('person_id')
        self.person_no = data.get('person_no')
        self.schedule_id = data.get('schedule_id')
        self.clinic_id = data.get('clinic_id')
        self.provider_id = data.get('provider_id')
        self.appointment_purpose = data.get('appointment_purpose')
        self.appointment_date = datetime.datetime.now()
        self.slot_start = datetime.datetime.now()
        self.slot_end = datetime.datetime.now()
        self.slot_duration = data.get('slot_duration')
        self.slot_tag = data.get('slot_tag')
        self.is_priority = data.get('is_priority')
        self.booking_time = datetime.datetime.now()
        self.booked_by = data.get('booked_by')
        self.booked_via = data.get('booked_via')
        self.booking_agent = data.get('booking_agent')
        self.delete_ind = data.get('delete_ind')
        self.online_checkin_status = data.get('online_checkin_status')
        self.online_checkin_time = datetime.datetime.now()
        self.payment_status = data.get('payment_status')
        self.clinic_checkin_status = data.get('clinic_checkin_status')
        self.clinic_checkin_time = datetime.datetime.now()
        self.clinic_checkin_by = data.get('clinic_checkin_by')
        self.provider_consultation_status = data.get('provider_consultation_status')
        self.created_by = data.get('created_by')
        self.created_time = datetime.datetime.now()
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
    def get_all_appointments():
        return PatientAppointmentModel.query.all()

    @staticmethod
    def get_patient_appointment_by_appointment_id(appointment_id):
        return PatientAppointmentModel.query.get(appointment_id)

    @staticmethod
    def get_appointment_by_person_no(_person_no):
        return PatientAppointmentModel.query.filter_by(person_no=_person_no).first()

    @staticmethod
    def get_appointment_by_person_id(_person_id):
        return PatientAppointmentModel.query.filter_by(person_id=_person_id).first()

    @staticmethod
    def load_patient_past_visit_by_person_id_in_consult_Dr_web_app(_person_id):
        dbobj = DBUtil()
        fun_call = "SELECT * FROM scs.get_patient_past_visit_by_person_id_in_consult_Dr_web_app({0})".format(_person_id)
        return dbobj.execute_custom_function(fun_call)

    @staticmethod
    def load_my_appointments_by_provider_id_in_booking_of_Dr_web_app(_provider_id,_clinic_id,_date_):
        dbobj = DBUtil()
        fun_call = "SELECT * FROM scs.get_my_appointments_by_provider_id_in_booking_of_Dr_web_app({0},{1},'{2}')".format(_provider_id,_clinic_id,_date_)
        return dbobj.execute_custom_function(fun_call)

    @staticmethod
    def load_cancel_appointment_in_booking_by_patient_no(_person_no):
        dbobj = DBUtil()
        fun_call = "SELECT * FROM scs.get_cancel_appointment_in_booking_by_patient_no('{0}')".format(_person_no)
        return dbobj.execute_custom_function(fun_call)

    def __repr(self):
        return '<appointment_id {}>'.format(self.appointment_id)

class PatientAppointmentSchema(Schema):
    appointment_id = fields.Integer(required=False)
    person_id = fields.Integer(required=False)
    person_no = fields.Str(required=True)
    schedule_id = fields.Integer(required=False)
    clinic_id = fields.Integer(required=False)
    provider_id = fields.Integer(required=False)
    appointment_purpose = fields.Str(required=False, missing=None)
    appointment_date = fields.DateTime(required=False, missing=datetime.datetime.now())
    slot_start = fields.DateTime(required=False, missing=datetime.datetime.now())
    slot_end = fields.DateTime(required=False, missing=datetime.datetime.now())
    slot_duration = fields.Integer(required=False)
    slot_tag = fields.Str(required=False, missing=None)
    is_priority = fields.Bool(required=False, missing=False)
    booking_time = fields.DateTime(required=False, missing=datetime.datetime.now())
    booked_by = fields.Str(required=False, missing=None)
    booked_via = fields.Str(required=False, missing=None)
    booking_agent = fields.Str(required=False, missing=None)
    delete_ind = fields.Bool(required=False, missing=False)
    online_checkin_status = fields.Bool(required=False, missing=False)
    online_checkin_time = fields.DateTime(required=False, missing=datetime.datetime.now())
    payment_status = fields.Bool(required=False, missing=False)
    clinic_checkin_status = fields.Bool(required=False, missing=False)
    clinic_checkin_time = fields.DateTime(required=False, missing=datetime.datetime.now())
    clinic_checkin_by = fields.Str(required=False, missing=None)
    provider_consultation_status = fields.Str(required=False, missing=None)
    created_by = fields.Str(required=False, missing=None)
    created_time = fields.DateTime(required=False, missing=datetime.datetime.now())
    modify_by = fields.Str(required=False, missing=None)
    modify_time = fields.DateTime(required=False, missing=datetime.datetime.now())


