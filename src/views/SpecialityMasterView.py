from flask import request, json, Response, Blueprint, jsonify
from ..models.SpecialityMasterModel import SpecialityMasterModel, SpecialityMasterSchema
from ..shared.CommonUtil import CommonUtil

spec_api = Blueprint('spec_api', __name__)
spec_schema = SpecialityMasterSchema()
common = CommonUtil()

@spec_api.route('/', methods=['GET'])
def get_all():
    try:
        speciality = SpecialityMasterModel.get_all_specialities()
        if not speciality:
            return common.info_request_response({'info': 'speciality not found'})
        ser_pats = spec_schema.dump(speciality, many=True)#.data
        return common.custom_response(ser_pats, 200)
    except:
        raise
        return common.code_error_response()
