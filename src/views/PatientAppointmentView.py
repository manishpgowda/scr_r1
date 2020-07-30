from flask import request, json, Response, Blueprint, jsonify
from ..models.PatientAppointmentModel  import PatientAppointmentModel, PatientAppointmentSchema
from ..shared.CommonUtil import CommonUtil
#from ..shared.Authentication import Auth

patient_appointment_api = Blueprint('patient_appointment_api', __name__)
patient_appointment_schema = PatientAppointmentSchema()
common = CommonUtil()

@patient_appointment_api.route('/', methods=['GET'])
def get_all():
    try:
        appointments = PatientAppointmentModel.get_all_appointments()
        if not appointments:
            return common.custom_response({'error': 'appointment not found'}, 404)
        ser_appointments = patient_appointment_schema.dump(appointments, many=True)#.data
        return common.custom_response(ser_appointments, 200)
        # return common.custom_response(msg_in_json, 200)
    except:
        #raise
        return common.code_error_response()

@patient_appointment_api.route('/<int:appointment_id>', methods=['GET'])
def get_one_patient(appointment_id):
    try:
        appointment = PatientAppointmentModel.get_patient_appointment_by_appointment_id(appointment_id)
        if not appointment:
            return common.custom_response({'error': 'appointment not found'}, 404)
        ser_pat = patient_appointment_schema.dump(appointment)
        return common.custom_response(ser_pat, 200)
    except:
        #raise
        return common.code_error_response()



@patient_appointment_api.route('/person_no', methods=['GET'])
def get_patient_appointment_by_person_no(): #clinic_id,provider_id,user_type
    req_data = request.get_json()
    _person_no = req_data['person_no']
    # # check if user already exist in the db
    appointment_in_db = PatientAppointmentModel.get_appointment_by_person_no(_person_no)
    if not appointment_in_db:
        message = {'error': 'appointment does not exist, please check the person number'}
        return common.custom_response(message, 400)

    ser_data = patient_appointment_schema.dump(appointment_in_db)
    # token = Auth.generate_token(ser_data.get('id'))
    return common.custom_response(ser_data, 201)

@patient_appointment_api.route('/person_id', methods=['GET'])
def get_patient_appointment_by_person_id(): #clinic_id,provider_id,user_type
    req_data = request.get_json()
    _person_id = req_data['person_id']
    # # check if user already exist in the db
    appointment_in_db = PatientAppointmentModel.get_appointment_by_person_id(_person_id)
    if not appointment_in_db:
        message = {'error': 'appointment does not exist, please check the person id'}
        return common.custom_response(message, 400)

    ser_data = patient_appointment_schema.dump(appointment_in_db)
    # token = Auth.generate_token(ser_data.get('id'))
    return common.custom_response(ser_data, 201)

@patient_appointment_api.route('/consult/manage_op/past_visit/<int:person_id>', methods=['GET'])
def get_patient_past_visit_by_person_id_in_consult_Dr_web_app(person_id):
    try:
        past_visit_list = PatientAppointmentModel.load_patient_past_visit_by_person_id_in_consult_Dr_web_app(person_id)
        final_out = common.convert_result_to_dict(past_visit_list)
        app_in_json = jsonify(final_out)
        return common.custom_json_response(app_in_json, 200)
    except:
        return common.code_error_response()

@patient_appointment_api.route('/booking/my_appointments/<int:provider_id> <int:clinic_id>', methods=['GET'])
def get_my_appointments_by_provider_id_in_booking_of_Dr_web_app(provider_id, clinic_id):
    try:
        appointment_list = PatientAppointmentModel.load_my_appointments_by_provider_id_in_booking_of_Dr_web_app(provider_id, clinic_id)
        final_out = common.convert_result_to_dict(appointment_list)
        app_in_json = jsonify(final_out)
        return common.custom_json_response(app_in_json, 200)
    except:
        return common.code_error_response()

@patient_appointment_api.route('/booking/cancel_appointment/<int:person_no>', methods=['GET'])
def get_cancel_appointment_in_booking_by_patient_no(person_no):
    try:
        cancel_appointment_list = PatientAppointmentModel.load_cancel_appointment_in_booking_by_patient_no(person_no)
        final_out = common.convert_result_to_dict(cancel_appointment_list)
        app_in_json = jsonify(final_out)
        return common.custom_json_response(app_in_json, 200)
    except:
        return common.code_error_response()