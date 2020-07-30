from marshmallow import fields, Schema
import datetime
from . import db

#appointment_purpose
class AppointmentPurposeModel(db.Model):
    """
    AppointmentPurposeModel Model
    """
    # table name
    __tablename__ = 'appointment_purpose'
    __table_args__ = {"schema": "scs"}

    appointment_purpose_id = db.Column(db.Integer, primary_key=True)
    appointment_purpose = db.Column(db.String(200), nullable=False)
    min_consult_time = db.Column(db.Integer, nullable=True)

    # class constructor
    def __init__(self, data):

        self.appointment_purpose_id = data.get('appointment_purpose_id')
        self.appointment_purpose = data.get('appointment_purpose')
        self.min_consult_time = data.get('min_consult_time')

class AppointmentPurposeSchema(Schema):
    appointment_purpose_id = fields.Integer(required=False)
    appointment_purpose = fields.Str(required=False, missing=None)
    min_consult_time = fields.Integer(required=False, Missing=None)
