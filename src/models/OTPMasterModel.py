from marshmallow import fields, Schema
import datetime
from . import db

class OTPMasterModel(db.Model):
	"""
	PatientMasterModel Model
	"""
	# table name
	__tablename__ = 'otp_master'
	__table_args__ = {"schema": "scs"}

	otp_id = db.Column(db.Integer, primary_key=True)
	otp_phone = db.Column(db.String(20), nullable=False)
	otp_user_type = db.Column(db.String(10), nullable=False)
	otp_user_id = db.Column(db.String(50), nullable=True)
	otp = db.Column(db.String(10), nullable=False)
	otp_gen_time = db.Column(db.DateTime,nullable=False)
	is_otp_valid = db.Column(db.Boolean, nullable=False)
	created_by = db.Column(db.String(50), nullable=True)
	create_time = db.Column(db.DateTime, nullable=False)

	def __init__(self, data):
		self.otp_id = data.get('otp_id')
		self.otp_phone = data.get('otp_phone')
		self.otp_user_type = data.get('otp_user_type')
		self.otp_user_id = data.get('otp_user_id')
		self.otp = data.get('otp')
		self.otp_gen_time = data.get('otp_gen_time')
		self.is_otp_valid = data.get('is_otp_valid')
		self.created_by = data.get('created_by')
		self.create_time = data.get('create_time')

	def save(self):
		db.session.add(self)
		db.session.commit()

	def update(self, data):
		for key, item in data.items():
			setattr(self, key, item)
		db.session.commit()

	def validate_otp(self, data):
		self.is_otp_valid = True
		db.session.commit()

class OTPMasterSchema(Schema):
	otp_id = fields.Integer(required=False)
	otp_phone = fields.Str(required=True)
	otp_user_type = fields.Str(required=False,missing=None)
	otp_user_id = fields.Str(required=False,Missing=None)
	otp = fields.Str(required=False,missing=None)
	otp_gen_time = fields.DateTime(required=False, missing=None)
	is_otp_valid = fields.Bool(required=False, missing=False)
	created_by = fields.Str(required=False, missing=None)
	create_time = fields.DateTime(required=False, missing=datetime.datetime.now())
