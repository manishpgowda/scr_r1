# src/models/PatientMasterModel.py
from marshmallow import fields, Schema
import datetime
from . import db


#clinic_op_master
class ClinicOpMasterModel(db.Model):
    """
    ClinicOpMasterModel Model
    """
    # table name
    __tablename__ = 'clinic_op_master'
    __table_args__ = {"schema": "scs"}

    op_id = db.Column(db.Integer, primary_key=True)
    clinic_id = db.Column(db.Integer, nullable=True)
    provider_id = db.Column(db.Integer, nullable=True)
    schedule_id = db.Column(db.Integer, nullable=True)
    scheduled_start = db.Column(db.DateTime, nullable=False)
    scheduled_end  = db.Column(db.DateTime, nullable=False)
    actual_start  = db.Column(db.DateTime, nullable=False)
    actual_end = db.Column(db.DateTime, nullable=False)
    op_status = db.Column(db.String(10), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.String(50), nullable=False)
    modify_by = db.Column(db.String(50), nullable=False)
    modify_time = db.Column(db.DateTime, nullable=False)


    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.op_id = data.get('op_id')
        self.clinic_id = data.get('clinic_id')
        self.provider_id = data.get('provider_id')
        self.schedule_id = data.get('schedule_id')
        self.scheduled_start = datetime.datetime.now()
        self.scheduled_end = datetime.datetime.now()
        self.actual_start = datetime.datetime.now()
        self.actual_end = datetime.datetime.now()
        self.op_status = data.get('op_status')
        self.create_time = datetime.datetime.now()
        self.created_by = data.get('created_by')
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

    def delete(self, data):
        self.delete_ind = True
        self.is_active = False
        db.session.commit()

    @staticmethod
    def get_all_op_patients():
        return ClinicOpMasterModel.query.all()

    @staticmethod
    def get_op_patient_by_phone(_phone_no):
        return ClinicOpMasterModel.query.filter_by(phone_no=_phone_no).first()

    @staticmethod
    def get_op_patient_by_id(op_id):
        return ClinicOpMasterModel.query.get(op_id)

    @staticmethod
    def get_op_patient_list(_clinic_id,_provider_id,_age_from, _age_to):
        dbobj = DBUtil()
        fun_call = "SELECT * FROM scs.get_patient_list({0},{1},'{2}',{3},{4})"\
            .format(_clinic_id,_provider_id,'sys',_age_from,_age_to)
        return dbobj.execute_custom_function(fun_call)

    def __repr(self):
        return '<op_id {}>'.format(self.op_id)


class ClinicOpMasterSchema(Schema):
    op_id = fields.Integer(required=False)
    clinic_id = fields.Integer(required=False)
    provider_id = fields.Integer(required=False)
    schedule_id = fields.Integer(required=False)
    scheduled_start = fields.DateTime(required=False, missing=datetime.datetime.now())
    scheduled_end = fields.DateTime(required=False, missing=datetime.datetime.now())
    actual_start = fields.DateTime(required=False, missing=datetime.datetime.now())
    actual_end = fields.DateTime(required=False, missing=datetime.datetime.now())
    op_status = fields.Str(required=False, missing=None)
    create_time = fields.DateTime(required=False, missing=datetime.datetime.now())
    created_by = fields.Str(required=False, missing=None)
    modify_by = fields.Str(required=False, missing=None)
    modify_time = fields.DateTime(required=False, missing=datetime.datetime.now())