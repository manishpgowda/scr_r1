from flask import request, json, Response, Blueprint, jsonify
from ..models.ClinicProviderMappingModel  import ClinicProviderMappingModel, ClinicProviderMappingSchema
from ..shared.CommonUtil import CommonUtil
#from ..shared.Authentication import Auth

clinic_provider_mapping_api = Blueprint('clinic_provider_mapping', __name__)
clinic_provider_mapping_schema = ClinicProviderMappingSchema()
common = CommonUtil()

@clinic_provider_mapping_api.route('/web_app/', methods=['GET'])
def get_all():
    pro_clinc_data = ClinicProviderMappingModel.get_all_mappings()
    ser_data = clinic_provider_mapping_schema.dump(pro_clinc_data, many=True)#.data
    return common.custom_response(ser_data, 200)

@clinic_provider_mapping_api.route('/web_app/booking/book_new_appointment/', methods=['GET'])
def get_provider_list_in_book_new_appointment():
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

        if 'date_pref' in arg_list:
            _date_pref = req_data['date_pref']
        else:
            _date_pref = ''

        provider_List_in_book_new_appointment = ClinicProviderMappingModel.load_provider_list_in_book_new_appointmnet(_clinic_id, _date_pref)
        if not provider_List_in_book_new_appointment:
            message = {'error': 'No providers found for the person number'}
            return common.info_request_response(message, 404)
        final_out = common.convert_result_to_dict(provider_List_in_book_new_appointment)
        app_in_json = jsonify(final_out)
        return common.custom_json_response(app_in_json, 200)
    except:
        raise
        # return common.code_error_response()