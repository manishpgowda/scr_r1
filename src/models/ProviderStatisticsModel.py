# src/models/PatientMasterModel.py
from marshmallow import fields, Schema
import datetime
from . import db


class ProviderStatisticsModel(db.Model):
    """
    ProviderStatisticsModel Model
    """
    # table name
    __tablename__ = 'provider_statistics'
    __table_args__ = {"schema": "scs"}

    provider_id = db.Column(db.Integer, primary_key=True)
    total_patient_visits = db.Column(db.Integer, nullable=False)
    avg_consult_time = db.Column(db.Float, nullable=False)
    avg_rating = db.Column(db.Float, nullable=False)
    total_consult_time = db.Column(db.Float, nullable=False)
    last_updated_time = db.Column(db.DateTime, nullable=False)
    avg_waiting_time = db.Column(db.Float, nullable=False)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.provider_id = data.get('provider_id')
        self.total_patient_visits = data.get('total_patient_visits')
        self.avg_consult_time = data.get('avg_consult_time')
        self.avg_rating = data.get('avg_rating')
        self.total_consult_time = data.get('total_consult_time')
        self.last_updated_time = data.get('last_updated_time')
        self.avg_waiting_time = data.get('avg_waiting_time')

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
    def get_all_provider_statistics():
        return ProviderStatisticsModel.query.all()

    @staticmethod
    def get_provider_statistics_by_provider_id(provider_id):
        return ProviderStatisticsModel.query.get(provider_id)

    def __repr(self):
        return '<provider_id {}>'.format(self.provider_id)


class ProviderStatisticsSchema(Schema):
    provider_id = db.Column(db.Integer, primary_key=True)
    total_patient_visits = db.Column(db.Integer, nullable=False)
    avg_consult_time = db.Column(db.Float, nullable=False)
    avg_rating = db.Column(db.Float, nullable=False)
    total_consult_time = db.Column(db.Float, nullable=False)
    last_updated_time = db.Column(db.DateTime, nullable=False)
    avg_waiting_time = db.Column(db.Float, nullable=False)