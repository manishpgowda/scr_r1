from flask import request, json, Response, Blueprint, jsonify
from ..models.ProviderTypeMasterModel import ProviderTypeMasterModel, ProviderTypeMasterSchema
from ..shared.CommonUtil import CommonUtil

providerType_api = Blueprint('providerType_api', __name__)
providerType_schema = ProviderTypeMasterSchema()
common = CommonUtil()

@providerType_api.route('/web_app/', methods=['GET'])
def get_all():
    try:
        streams = ProviderTypeMasterModel.get_all_provider_type()
        if not streams:
            return common.info_request_response({'info': 'degree not found'})
        ser_pats = providerType_schema.dump(streams, many=True)#.data
        return common.custom_response(ser_pats, 200)
    except:
        return common.code_error_response()
