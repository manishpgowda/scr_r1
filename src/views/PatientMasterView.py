from flask import request, json, Response, Blueprint, jsonify
from ..models.PatientMasterModel import PatientMasterModel, PatientMasterSchema
from ..shared.CommonUtil import CommonUtil
#from ..shared.Authentication import Auth

patient_api = Blueprint('patient_api', __name__)
patient_schema = PatientMasterSchema()
common = CommonUtil()

@patient_api.route('/web_app/add', methods=['POST'])
def add():
    try:
        req_data = request.get_json()
        data = patient_schema.load(req_data)
        # # check if user already exist in the db
        patient_in_db = PatientMasterModel.get_patient_by_phone(data.get('phone_no'))
        if patient_in_db:
            message = {'info': 'Patient already exist, please check the phone number or enter a new one'}
            return common.info_request_response(message)
        _clinic_id = data.get('primary_clinic_id')
        if not _clinic_id:
            _clinic_id = 0
        next_upn = PatientMasterModel.get_next_patient_upn(_clinic_id)
        patient = PatientMasterModel(data)
        patient.person_no = next_upn
        patient.save()
        ser_data = patient_schema.dump(patient)
        token = ser_data.get('person_no')
        return common.custom_response({'person_no': token}, 201)
    except:
        #raise
        return common.code_error_response()

@patient_api.route('/web_app/update', methods=['PUT'])
def update():
    try:
        req_data = request.get_json()
        data = patient_schema.load(req_data, partial=True)
        patient = PatientMasterModel.get_patient_by_id(data.get('person_id'))
        if not patient:
            return common.info_request_response({'info': 'patient not found'})
        patient.update(data)
        ser_pat = patient_schema.dump(patient)
        return common.custom_response(ser_pat, 201)
    except:
        return common.code_error_response()

@patient_api.route('/web_app/delete', methods=['PUT'])
def delete():
    try:
        req_data = request.get_json()
        data = patient_schema.load(req_data, partial=True)
        patient = PatientMasterModel.get_patient_by_id(data.get('person_id'))
        if not patient:
            return common.info_request_response({'info': 'patient not found'})
        patient.delete(data)
        ser_pat = patient_schema.dump(patient)
        return common.custom_response(ser_pat, 201)
    except:
        return common.code_error_response()

@patient_api.route('/web_app/', methods=['GET'])
def get_all():
    try:
        patients = PatientMasterModel.get_all_patients()
        if not patients:
            return common.info_request_response({'info': 'patients not found'})
        ser_pats = patient_schema.dump(patients, many=True)#.data
        return common.custom_response(ser_pats, 200)
    except:
        return common.code_error_response()

@patient_api.route('/web_app/<int:person_id>', methods=['GET'])
def get_one_patient(person_id):
    try:
        patient = PatientMasterModel.get_patient_by_id(person_id)
        if not patient:
            return common.info_request_response({'info': 'patient not found'})
        ser_pat = patient_schema.dump(patient)#.data
        return common.custom_response(ser_pat, 200)
    except:
        return common.code_error_response()

@patient_api.route('/web_app/patient_list', methods=['GET'])
def get_patient_list():
    try:
        req_data = request.get_json()
        arg_list = None
        if not req_data:
            message = {'error': 'clinic_id | provider_id args missing in the request'}
            return common.bad_request_response(message)
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

        if 'age_from' in arg_list:
            _age_from = req_data['age_from']
        else:
            _age_from = 0

        if 'age_to' in arg_list:
            _age_to = req_data['age_to']
        else:
            _age_to = 0

        if 'user_type' in arg_list:
            _user_type = req_data['user_type']
        else:
            _user_type = 'SYS'

        if _clinic_id ==0 and _provider_id ==0:
            message = {'error': 'clinic_id | provider_id args missing in the request call'}
            return common.bad_request_response(message)
        #print(_clinic_id)
        pat_lst = PatientMasterModel.get_patient_list(_clinic_id,_provider_id,_user_type,_age_from,_age_to)
        final_out= common.convert_result_to_dict(pat_lst)
        pat_in_json = jsonify(final_out)
        return common.custom_json_response(pat_in_json, 200)
    except:
        return common.code_error_response()

@patient_api.route('/web_app/patient_dir', methods=['GET'])
def get_patient_directory():
    try:
        req_data = request.get_json()
        arg_list = None
        if not req_data:
            message = {'error': 'clinic_id | provider_id args missing in the request'}
            return common.bad_request_response(message)
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

        if 'age_from' in arg_list:
            _age_from = req_data['age_from']
        else:
            _age_from = 0

        if 'age_to' in arg_list:
            _age_to = req_data['age_to']
        else:
            _age_to = 0

        if 'user_type' in arg_list:
            _user_type = req_data['user_type']
        else:
            _user_type = 'SYS'

        if _clinic_id ==0 and _provider_id ==0:
            message = {'error': 'clinic_id | provider_id args missing in the request call'}
            return common.bad_request_response(message)
        #print(_clinic_id)
        pat_lst = PatientMasterModel.get_patient_directory(_clinic_id,_provider_id,_user_type,_age_from,_age_to)
        final_out= common.convert_result_to_dict(pat_lst)
        pat_in_json = jsonify(final_out)
        return common.custom_json_response(pat_in_json,200)
    except:
        return common.code_error_response()

@patient_api.route('/web_app/patient_by_upn', methods=['GET'])
def get_patient_by_upn(clinic_id,provider_id,user_type):
    ser_pat = None
    return common.custom_response(ser_pat, 200)

@patient_api.route('/web_app/patient_by_phone', methods=['GET'])
def get_patient_by_phone(): #clinic_id,provider_id,user_type
    try:
        req_data = request.get_json()
        _phone_no = req_data['phone_no']
        # # check if user already exist in the db
        patient_in_db = PatientMasterModel.get_patient_by_phone(_phone_no)
        if not patient_in_db:
            message = {'info': 'Patient does not exist, please check the phone number'}
            return common.info_request_response(message)
        ser_data = patient_schema.dump(patient_in_db)
        return common.custom_response(ser_data, 201)
    except:
        return common.code_error_response()






