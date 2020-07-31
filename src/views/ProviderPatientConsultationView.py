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