from flask import request, json, Response, Blueprint
from ..models.OTPMasterModel import OTPMasterModel, OTPMasterSchema

otp_api = Blueprint('otp_api', __name__)
otp_schema = OTPMasterSchema()

@otp_api.route('/web_app/new', methods=['POST'])
def generate_otp():
    """
    Create otp function
    """
    req_data = request.get_json()
    data = otp_schema.load(req_data)

    otp_obj = OTPMasterModel(data)
    otp_obj.save()

    ser_data = otp_schema.dump(otp_obj)
   #token = Auth.generate_token(ser_data.get('id'))
    token = ser_data.get('person_no')
    #return custom_response({'person_no': token}, 201)