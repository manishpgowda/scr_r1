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