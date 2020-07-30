# src/models/PatientMasterModel.py
from marshmallow import fields, Schema
import datetime
from . import db


class PatientProviderRatingModel(db.Model):
    """
    PatientProviderRatingModel Model
    """
    # table name
    __tablename__ = 'patient_master'
    __table_args__ = {"schema": "scs"}

    rating_id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.Integer,nullable=True)
    person_id = db.Column(db.Integer,nullable=True)
    clinic_id = db.Column(db.Integer,nullable=True)
    provider_id = db.Column(db.Integer,nullable=True)
    provider_interaction_rating = db.Column(db.Integer,nullable=True)
    provider_treatment_rating = db.Column(db.Integer,nullable=True)
    provider_punctuality_rating = db.Column(db.Integer,nullable=True)
    clinic_rating = db.Column(db.Integer,nullable=True)
    patient_comment = db.Column(db.String(2000), nullable=False)
    provider_comment = db.Column(db.String(2000), nullable=False)
    created_by = db.Column(db.String(50), nullable=False)
    created_time = db.Column(db.DateTime,nullable=False)


    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
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
    def get_all_patients_provider_rating():
        return PatientProviderRatingModel.query.all()

    @staticmethod
    def get_patient_provider_rating_by_id(person_id):
        return PatientProviderRatingModel.query.get(person_id)


    def __repr(self):
        return '<person_id {}>'.format(self.person_id)


class PatientProviderRatingSchema(Schema):
    rating_id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.Integer,nullable=True)
    person_id = db.Column(db.Integer,nullable=True)
    clinic_id = db.Column(db.Integer,nullable=True)
    provider_id = db.Column(db.Integer,nullable=True)
    provider_interaction_rating = db.Column(db.Integer,nullable=True)
    provider_treatment_rating = db.Column(db.Integer,nullable=True)
    provider_punctuality_rating = db.Column(db.Integer,nullable=True)
    clinic_rating = db.Column(db.Integer,nullable=True)
    patient_comment = db.Column(db.String(2000), nullable=False)
    provider_comment = db.Column(db.String(2000), nullable=False)
    created_by = db.Column(db.String(50), nullable=False)
    created_time = db.Column(db.DateTime,nullable=False)