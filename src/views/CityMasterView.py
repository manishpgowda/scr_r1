from flask import request, json, Response, Blueprint, jsonify
from ..models.CityMasterModel import CityMasterModel, CityMasterSchema
from ..shared.CommonUtil import CommonUtil

city_api = Blueprint('city_api', __name__)
city_schema = CityMasterSchema()
common = CommonUtil()

@city_api.route('/', methods=['GET'])
def get_all():
    try:
        cities = CityMasterModel.get_all_cities()
        if not cities:
            return common.info_request_response({'info': 'city not found'})
        ser_pats = city_schema.dump(cities, many=True)#.data
        return common.custom_response(ser_pats, 200)
    except:
        raise
        return common.code_error_response()
