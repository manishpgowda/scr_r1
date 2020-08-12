from flask import request, json, Blueprint, Response, jsonify
from ..shared.CommonUtil import CommonUtil
from ..models.ProviderPatientConsultationModel import ProviderPatientConsultationModel, ProviderConsultationSchema

provider_consultation_api = Blueprint('provider_consultation_api', __name__)
provider_consultaion_schema = ProviderConsultationSchema()
common = CommonUtil()

@provider_consultation_api.route('/web_app/', methods=['GET'])
def get_all():
    consults = ProviderPatientConsultationModel.get_all_provider_patient_consultation()
    print(consults)
    ser_consults = provider_consultaion_schema.dump(consults, many=True)#.data
    print(ser_consults)
    return common.custom_response(ser_consults, 200)

@provider_consultation_api.route('/web_app/appointment_list/<int:provider_id> <date>', methods=['GET'])
def get_appointment_list_of_patients_by_provider_id_by_date(_provider_id, date):
    try:
        appointment_details = ProviderPatientConsultationModel.load_appointment_list_of_patients_by_provider_id_by_date(_provider_id, date)
        final_out = common.convert_result_to_dict(appointment_details)
        app_in_json = jsonify(final_out)
        return common.custom_json_response(app_in_json, 200)
    except:
        return common.code_error_response()


@provider_consultation_api.route('/web_app/patient_booking/provider_list', methods=['GET'])
def get_provider_list_in_book_new_patients():
    try:
        provider_list = ProviderPatientConsultationModel.load_provider_list_in_book_new_patients()
        final_out = common.convert_result_to_dict(provider_list)
        app_in_json = jsonify(final_out)
        return common.custom_json_response(app_in_json, 200)
    except:
        return common.code_error_response()

@provider_consultation_api.route('/web_app/consult/recent_consultation/<int:clinic_id> <int:provider_id>', methods=['GET'])
def get_recent_consultation_by_clinic_id_and_provider_id(clinic_id, provider_id):
    try:
        recent_consultation_list = ProviderPatientConsultationModel.load_recent_consultation(clinic_id, provider_id)
        final_out = common.convert_result_to_dict(recent_consultation_list)
        app_in_json = jsonify(final_out)
        return common.custom_json_response(app_in_json, 200)
    except:
        return common.code_error_response()

# get appointment report by date range
@provider_consultation_api.route('/web_app/appointment_report_by_date_range', methods=['GET'])
def get_appointmnet_by_date_range():
    try:
        req_data = request.get_json()
        arg_list = None
        if not req_data:
            message = {'error': 'parameter args missing in the request'}
            return common.bad_request_response(message, 404)
        else:
            arg_list = req_data  # json.loads(req_data)

        if 'clinic_id' in arg_list:
            _clinic_id = req_data['clinic_id']
        else:
            _clinic_id = 0

        if 'provider_id' in arg_list:
            _provider_id = req_data['provider_id']
        else:
            _provider_id = ''

        if 'date_from' in arg_list:
            _date_from = req_data['date_from']
        else:
            _date_from = 0

        if 'date_to' in arg_list:
            _date_to = req_data['date_to']
        else:
            _date_to = 0

        appointment_report = ProviderPatientConsultationModel.load_appointment_report_by_date_range(_clinic_id, _provider_id, _date_from, _date_to)
        if not appointment_report:
            message = {'error': 'appointment_report does not exist '}
            return common.info_request_response(message, 404)
        final_out = common.convert_result_to_dict(appointment_report)
        appointment_report_in_json = jsonify(final_out)
        return common.custom_json_response(appointment_report_in_json, 200)
    except:
        #raise
        return common.code_error_response()