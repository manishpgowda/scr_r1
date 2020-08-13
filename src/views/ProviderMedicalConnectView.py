from flask import request, json, Response, Blueprint, jsonify
from ..models.ProviderMedicalConnectModel import ProviderMedicalConnectModel, ProviderMedicalConnectSchema
from ..shared.CommonUtil import CommonUtil
#from ..shared.Authentication import Auth

provider_medical_connect_api = Blueprint('provider_medical_connect_api', __name__)
provider_medical_connect_schema = ProviderMedicalConnectSchema()
common = CommonUtil()


@provider_medical_connect_api.route('/web_app/pro_conect_to_medical_store', methods=['GET'])
def get_provider_connected_to_medical_store():
    try:
        req_data = request.get_json()
        arg_list = None
        if not req_data:
            message = {'error': 'parameter args missing in the request'}
            return common.bad_request_response(message, 404)
        else:
            arg_list = req_data  # json.loads(req_data)

        if 'medical_store_id' in arg_list:
            _medical_store_id = req_data['medical_store_id']
        else:
            _medical_store_id = 0

        if _medical_store_id == 0:
            message = {'error': 'clinic_id args missing in the request call'}
            return common.bad_request_response(message, 400)

        provider_connect_list = ProviderMedicalConnectModel.load_provider_connected_to_medical_store(_medical_store_id)
        if not provider_connect_list:
            message = {'error': 'clinics does not exist '}
            return common.info_request_response(message, 404)
        final_out = common.convert_result_to_dict(provider_connect_list)
        pro_list_in_json = jsonify(final_out)
        return common.custom_json_response(pro_list_in_json, 200)
    except:
        raise
        return common.code_error_response()