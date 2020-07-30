# src/models/PatientMasterModel.py
from marshmallow import fields, Schema
import datetime
from . import db


class ProviderBookmarkMasterModel(db.Model):
    """
    ProviderBookmarkMasterModel Model
    """
    # table name
    __tablename__ = 'provider_bookmark_master'
    __table_args__ = {"schema": "scs"}

    provider_id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer,nullable=True)
    bookmark_type = db.Column(db.String(5), nullable=False)
    bookmark_status = db.Column(db.Boolean, nullable=False)
    bookmark_date = db.Column(db.DateTime,nullable=False)
    bookmark_comments = db.Column(db.String(500), nullable=False)
    appointment_no = db.Column(db.Integer,nullable=False)
    consultation_id = db.Column(db.Integer,nullable=False)
    appointment_date = db.Column(db.DateTime,nullable=False)
    create_time = db.Column(db.DateTime,nullable=False)
    created_by = db.Column(db.String(50), nullable=False)
    modify_by = db.Column(db.String(50), nullable=False)
    modify_time = db.Column(db.DateTime,nullable=False)


    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.provider_id = data.get('provider_id')
        self.person_id = data.get('person_id')
        self.bookmark_type = data.get('bookmark_type')
        self.bookmark_status = data.get('bookmark_status')
        self.bookmark_date = data.get('bookmark_date')
        self.bookmark_comments = data.get('bookmark_comments')
        self.appointment_no = data.get('appointment_no')
        self.consultation_id = data.get('consultation_id')
        self.appointment_date = data.get('appointment_date')
        self.create_time = data.get('create_time')
        self.created_by = data.get('created_by')
        self.modify_by = data.get('modify_by')
        self.modify_time = data.get('modify_time')


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
    def get_all_provider_bookmark():
        return ProviderBookmarkMasterModel.query.all()

    @staticmethod
    def get_provider_bookmark_by_id(provider_id):
        return ProviderBookmarkMasterModel.query.get(provider_id)


    def __repr(self):
        return '<provider_id {}>'.format(self.provider_id)


class ProviderBookmarkMasterSchema(Schema):
    provider_id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer,nullable=True)
    bookmark_type = db.Column(db.String(5), nullable=False)
    bookmark_status = db.Column(db.Boolean, nullable=False)
    bookmark_date = db.Column(db.DateTime,nullable=False)
    bookmark_comments = db.Column(db.String(500), nullable=False)
    appointment_no = db.Column(db.Integer,nullable=False)
    consultation_id = db.Column(db.Integer,nullable=False)
    appointment_date = db.Column(db.DateTime,nullable=False)
    create_time = db.Column(db.DateTime,nullable=False)
    created_by = db.Column(db.String(50), nullable=False)
    modify_by = db.Column(db.String(50), nullable=False)
    modify_time = db.Column(db.DateTime,nullable=False)