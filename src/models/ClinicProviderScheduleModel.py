from marshmallow import fields, Schema
import datetime
from . import db


#clinic_provider_schedule
class ClinicProviderScheduleModel(db.Model):
    """
    ClinicProviderScheduleModel Model
    """
    # table name
    __tablename__ = 'clinic_provider_schedule'
    __table_args__ = {"schema": "scs"}

    schedule_id = db.Column(db.Integer, primary_key=True)
    clinic_id = db.Column(db.Integer, nullable=True)
    provider_id = db.Column(db.Integer, nullable=True)
    slot_start = db.Column(db.DateTime, nullable=False)
    slot_end = db.Column(db.DateTime, nullable=False)
    schedule_key = db.Column(db.String(20), nullable=False)
    consultation_fee = db.Column(db.Integer, nullable=True)
    schedule_effective_from = db.Column(db.DateTime, nullable=False)
    monday_on = db.Column(db.Boolean, nullable=False)
    tuesday_on = db.Column(db.Boolean, nullable=False)
    wednesday_on = db.Column(db.Boolean, nullable=False)
    thursday_on = db.Column(db.Boolean, nullable=False)
    friday_on = db.Column(db.Boolean, nullable=False)
    saturday_on = db.Column(db.Boolean, nullable=False)
    sunday_on = db.Column(db.Boolean, nullable=False)
    schedule_tag = db.Column(db.String(50), nullable=True)
    schedule_type = db.Column(db.String(5), nullable=True)
    avg_time_per_patient = db.Column(db.Integer, nullable=True)
    is_active = db.Column(db.Boolean, nullable=False)
    delete_ind = db.Column(db.Boolean, nullable=False)
    max_slots = db.Column(db.Integer, nullable=True)
    is_time_bound = db.Column(db.Boolean, nullable=False)
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
        self.schedule_id = data.get('schedule_id')
        self.clinic_id = data.get('clinic_id')
        self.provider_id = data.get('provider_id')
        self.slot_start = datetime.datetime.now()
        self.slot_end  = datetime.datetime.now()
        self.schedule_key = data.get('schedule_key')
        self.consultation_fee = data.get('consultation_fee')
        self.schedule_effective_from = datetime.datetime.now()
        self.monday_on = data.get('monday_on')
        self.tuesday_on = data.get('tuesday_on')
        self.wednesday_on = data.get('wednesday_on')
        self.thursday_on = data.get('thursday_on')
        self.friday_on = data.get('friday_on')
        self.saturday_on = data.get('saturday_on')
        self.sunday_on = data.get('sunday_on')
        self.schedule_tag = data.get('schedule_tag')
        self.schedule_type = data.get('schedule_type')
        self.avg_time_per_patient = data.get('avg_time_per_patient')
        self.is_active = data.get('is_active')
        self.delete_ind = data.get('delete_ind')
        self.max_slots = data.get('max_slots')
        self.is_time_bound = data.get('is_time_bound')
        self.create_time = datetime.datetime.now()
        self.created_by = data.get('created_by')
        self.modify_by = data.get('modify_by')
        self.modify_time = datetime.datetime.now()

class ClinicProviderScheduleSchema(Schema):
    schedule_id = fields.Integer(required=False)
    clinic_id = fields.Integer(required=False)
    provider_id = fields.Integer(required=False)
    slot_start = fields.DateTime(required=False, missing=datetime.datetime.now())
    slot_end = fields.DateTime(required=False, missing=datetime.datetime.now())
    schedule_key = fields.Str(required=False, missing=None)
    consultation_fee = fields.Integer(required=False)
    schedule_effective_from = fields.DateTime(required=False, missing=datetime.datetime.now())
    monday_on = fields.Bool(required=False, missing=True)
    tuesday_on = fields.Bool(required=False, missing=True)
    wednesday_on = fields.Bool(required=False, missing=True)
    thursday_on = fields.Bool(required=False, missing=True)
    friday_on = fields.Bool(required=False, missing=True)
    saturday_on = fields.Bool(required=False, missing=True)
    sunday_on = fields.Bool(required=False, missing=True)
    schedule_tag = fields.Str(required=False, missing=None)
    schedule_type = fields.Str(required=False, missing=None)
    avg_time_per_patient = fields.Integer(required=False)
    is_active = fields.Bool(required=False, missing=False)
    delete_ind = fields.Bool(required=False, missing=False)
    max_slots = fields.Integer(required=False)
    is_time_bound = fields.Bool(required=False, missing=False)
    create_time = fields.DateTime(required=False, missing=datetime.datetime.now())
    created_by = fields.Str(required=False, missing=None)
    modify_by = fields.Str(required=False, missing=None)
    modify_time = fields.DateTime(required=False, missing=datetime.datetime.now())