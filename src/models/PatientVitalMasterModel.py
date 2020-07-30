# src/models/PatientMasterModel.py
from marshmallow import fields, Schema
import datetime
from . import db


class PatientVitalMasterModel(db.Model):
    """
    PatientVitalMasterModel Model
    """
    # table name
    __tablename__ = 'patient_vital_master'
    __table_args__ = {"schema": "scs"}

    vital_sign_id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.Integer, nullable=True)
    consultation_id = db.Column(db.Integer, nullable=True)
    clinic_id = db.Column(db.Integer, nullable=True)
    person_id = db.Column(db.Integer, nullable=True)
    vital_time = db.Column(db.DateTime, nullable=False)
    bp_sys = db.Column(db.Float, nullable=False)
    bp_diastolic = db.Column(db.Float, nullable=False)
    bmi = db.Column(db.Float, nullable=False)
    height_cm = db.Column(db.Float, nullable=False)
    weight_kg = db.Column(db.Float, nullable=False)
    pulse_rate = db.Column(db.Float, nullable=False)
    created_by = db.Column(db.String(50), nullable=False)
    created_time = db.Column(db.DateTime, nullable=False)
    delete_ind = db.Column(db.Boolean, nullable=False)


    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.vital_sign_id = data.get('vital_sign_id')
        self.appointment_id = data.get('appointment_id')
        self.consultation_id = data.get('consultation_id')
        self.clinic_id = data.get('clinic_id')
        self.person_id = data.get('person_id')
        self.vital_time = data.get('vital_time')
        self.bp_sys = data.get('bp_sys')
        self.bp_diastolic = data.get('bp_diastolic')
        self.bmi = data.get('bmi')
        self.height_cm = data.get('height_cm')
        self.weight_kg = data.get('weight_kg')
        self.pulse_rate = data.get('pulse_rate')
        self.created_by = data.get('created_by')
        self.created_time = data.get('created_time')
        self.delete_ind = data.get('delete_ind')

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
    def get_all_patients_vitals():
        return PatientVitalMasterModel.query.all()

    @staticmethod
    def get_patient_vitals_by_id(person_id):
        return PatientVitalMasterModel.query.get(person_id)

    def __repr(self):
        return '<person_id {}>'.format(self.person_id)


class PatientVitalMasterSchema(Schema):
    vital_sign_id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.Integer, nullable=True)
    consultation_id = db.Column(db.Integer, nullable=True)
    clinic_id = db.Column(db.Integer, nullable=True)
    person_id = db.Column(db.Integer, nullable=True)
    vital_time = db.Column(db.DateTime, nullable=False)
    bp_sys = db.Column(db.Float, nullable=False)
    bp_diastolic = db.Column(db.Float, nullable=False)
    bmi = db.Column(db.Float, nullable=False)
    height_cm = db.Column(db.Float, nullable=False)
    weight_kg = db.Column(db.Float, nullable=False)
    pulse_rate = db.Column(db.Float, nullable=False)
    created_by = db.Column(db.String(50), nullable=False)
    created_time = db.Column(db.DateTime, nullable=False)
    delete_ind = db.Column(db.Boolean, nullable=False)