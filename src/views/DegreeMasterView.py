from flask import request, json, Response, Blueprint, jsonify
from ..models.DegreeMasterModel import DegreeMasterModel, DegreeMasterSchema
from ..shared.CommonUtil import CommonUtil

degree_api = Blueprint('degree_api', __name__)
degree_schema = DegreeMasterSchema()
common = CommonUtil()

@degree_api.route('/', methods=['GET'])
def get_all():
    try:
        degree = DegreeMasterModel.get_all_degrees()
        if not degree:
            return common.info_request_response({'info': 'degree not found'})
        ser_pats = degree_schema.dump(degree, many=True)#.data
        return common.custom_response(ser_pats, 200)
    except:
        return common.code_error_response()
