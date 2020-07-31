from flask import request, json, Response, Blueprint, jsonify
from ..models.ClinicOpMasterModel import ClinicOpMasterModel, ClinicOpMasterSchema
from ..shared.CommonUtil import CommonUtil

# from ..shared.Authentication import Auth


clinic_op_api = Blueprint('clinic_op_api', __name__)
clinic_op_schema = ClinicOpMasterSchema()
common = CommonUtil()


@clinic_op_api.route('/web_app/add', methods=['POST'])
def add():
    """
    Create User Function
    """
    req_data = request.get_json()
    data = clinic_op_schema.load(req_data)
    # # check if user already exist in the db
    op_patient_in_db = ClinicOpMasterModel.get_op_patient_by_phone(data.get('phone_no'))
    if op_patient_in_db:
        message = {'error': 'OP Patient already exist, please check the phone number or enter a new one'}
        return common.custom_response(message, 400)

    op_patient = ClinicOpMasterModel(data)
    op_patient.save()

   #  ser_data = clinic_op_schema.dump(op_patient)
   # #token = Auth.generate_token(ser_data.get('id'))
   #  token = ser_data.get('person_no')
   #  return common.custom_response({'person_no': token}, 201)


@clinic_op_api.route('/web_app/update', methods=['PUT'])
def update():
  """
  Update me
  """
  req_data = request.get_json()
  data = clinic_op_schema.load(req_data, partial=True)

  op_patient = ClinicOpMasterModel.get_op_patient_by_id(data.get('op_id'))
  op_patient.update(data)
  ser_op_pat = clinic_op_schema.dump(op_patient)
  return common.custom_response(ser_op_pat, 200)

@clinic_op_api.route('/web_app/delete', methods=['PUT'])
def delete():
  """
  Update me
  """
  req_data = request.get_json()
  data = clinic_op_schema.load(req_data, partial=True)
  op_patient = ClinicOpMasterModel.get_op_patient_by_id(data.get('op_id'))
  op_patient.delete(data)
  ser_op_pat = clinic_op_schema.dump(op_patient)
  return common.custom_response(ser_op_pat, 200)


@clinic_op_api.route('/web_app/', methods=['GET'])
def get_all():
    op_patients = ClinicOpMasterModel.get_all_op_patients()
    ser_op_pat = clinic_op_schema.dump(op_patients, many=True)#.data
    return custom_response(ser_op_pat, 200)

@clinic_op_api.route('/web_app/<int:op_id>', methods=['GET'])
def get_one_op_patient(op_id):
    op_patient = ClinicOpMasterModel.get_op_patient_by_id(op_id)
    if not op_patient:
        return custom_response({'error': ' OP patient not found'}, 404)
    ser_op_pat = clinic_op_schema.dump(op_patient)#.data
    return custom_response(ser_op_pat, 200)

@clinic_op_api.route('/web_app/op_patient_list', methods=['GET'])
def get_op_patient_list():

    req_data = request.get_json()
    arg_list = None
    if not req_data:
        message = {'error': 'clinic_id | provider_id args missing in the request'}
        return common.custom_response(message, 400)
    else:
        arg_list = req_data#json.loads(req_data)
    if 'clinic_id' in arg_list:
        _clinic_id = req_data['clinic_id']
    else:
        _clinic_id = 0

    if 'provider_id' in arg_list:
        _provider_id = req_data['provider_id']
    else:
        _provider_id = 0

    if _clinic_id ==0 and _provider_id ==0:
        message = {'error': 'clinic_id | provider_id args missing in the request call'}
        return common.custom_response(message, 400)
    print(_clinic_id)
    op_pat_lst = ClinicOpMasterModel.get_op_patient_list(_clinic_id,_provider_id,0,0)
    op_pat_in_json = jsonify({'result': [dict(row) for row in op_pat_lst]})
    #return common.custom_json_response(pat_lst, 200)
    return op_pat_in_json



def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )