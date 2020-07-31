from flask import request, json, Response, Blueprint, jsonify
from ..models.MedicalStoreModel import MedicalStoreModel, MedicalStoreSchema
from ..shared.CommonUtil import CommonUtil
#from ..shared.Authentication import Auth

medical_store_api = Blueprint('medical_store_api', __name__)
medical_schema = MedicalStoreSchema()
common = CommonUtil()

@medical_store_api.route('/web_app/add', methods=['POST'])
def add():
    try:
        req_data = request.get_json()
        data = medical_schema.load(req_data)
        # # check if user already exist in the db
        medical_in_db = MedicalStoreModel.get_medical_by_phone(data.get('phone_no'))
        if medical_in_db:
            message = {'info': 'Medical Store already exist, please check the phone number or enter a new one'}
            return common.info_request_response(message)
        medical = MedicalStoreModel(data)
        medical.save()
        return common.custom_response({'info':'Medical store added successfully'}, 201)
    except:
        return common.code_error_response()

@medical_store_api.route('/web_app/update', methods=['PUT'])
def update():
    try:
        req_data = request.get_json()
        data = medical_schema.load(req_data, partial=True)
        medical = MedicalStoreModel.get_medical_by_id(data.get('medical_store_id'))
        if not medical:
            message = {'info': 'Medical store does not exist, please check the details'}
            return common.info_request_response(message)
        medical.update(data)
        ser_pat = medical_schema.dump(medical)
        return common.custom_response(ser_pat, 201)
    except:
        return common.code_error_response()

@medical_store_api.route('/web_app/delete', methods=['PUT'])
def delete():
    try:
        req_data = request.get_json()
        data = medical_schema.load(req_data, partial=True)
        medical = MedicalStoreModel.get_medical_by_id(data.get('medical_store_id'))
        if not medical:
            message = {'info': 'Medical store does not exist, please check the details'}
            return common.info_request_response(message)
        medical.delete(data)
        ser_pat = medical_schema.dump(medical)
        return common.custom_response(ser_pat, 201)
    except:
        return common.code_error_response()

@medical_store_api.route('/web_app/', methods=['GET'])
def get_all_medicals():
    try:
        medicals = MedicalStoreModel.get_all_medicals()
        ser_pats = medical_schema.dump(medicals, many=True)  # .data
        return common.custom_response(ser_pats, 200)
    except:
        raise
        return common.code_error_response()

@medical_store_api.route('/web_app/<int:medical_store_id>', methods=['GET'])
def get_medical_by_id(medical_store_id):
    try:
        medical = MedicalStoreModel.get_medical_by_id(medical_store_id)
        if not medical:
            return common.info_request_response({'info': 'Medical Store not found'})
        ser_pat = medical_schema.dump(medical)  # .data
        return common.custom_response(ser_pat, 200)
    except:
        return common.code_error_response()

@medical_store_api.route('/web_app/medical_by_phone', methods=['GET'])
def get_medical_by_phone():
    try:
        req_data = request.get_json()
        _phone_no = req_data['phone_no']
        # # check if user already exist in the db
        medical_in_db = MedicalStoreModel.get_medical_by_phone(_phone_no)
        if not medical_in_db:
            message = {'info': 'Medical store does not exist, please check the phone number'}
            return common.info_request_response(message)
    except:
        return common.code_error_response()


# @medical_store_api.route('admin/medical_store_page_list', methods=['GET'])
# def get_list_for_medical_page_in_admin():
#     try:
#         list = MedicalStoreModel.load_list_for_medical_page_in_admin()
#         final_out = common.convert_result_to_dict(list)
#         app_in_json = jsonify(final_out)
#         return common.custom_json_response(app_in_json, 200)
#     except:
#         return common.code_error_response()


#not connected medical store
@medical_store_api.route('/web_app/Web_admin/med_store_list', methods=['GET'])
def get_all_medical_stores():
    try:
        req_data = request.get_json()
        arg_list = None
        if not req_data:
            message = {'error': ''}
            return common.bad_request_response(message)
        else:
            arg_list = req_data#json.loads(req_data)

        if 'location_lat' in arg_list:
            _location_lat = req_data['location_lat']
        else:
            _location_lat = 0

        if 'location_lon' in arg_list:
            _location_lon = req_data['location_lon']
        else:
            _location_lon = 0

        if 'date_pref' in arg_list:
            _date_pref = req_data['date_pref']
        else:
            _date_pref = ''

        if 'medical_store_name' in arg_list:
            _medical_store_name = req_data['medical_store_name']
        else:
            _medical_store_name = ''

        if 'page_no' in arg_list:
            _page_no = req_data['page_no']
        else:
            _page_no = 0

        med_stores = MedicalStoreModel.load_medical_stores_list(_location_lat , _location_lon, _date_pref, _medical_store_name, _page_no)
        if not med_stores:
            message = {'error': 'med_stores does not exist '}
            return common.info_request_response(message, 404)
        final_out = common.convert_result_to_dict(med_stores)
        med_store_in_json = jsonify(final_out)
        return common.custom_json_response(med_store_in_json, 200)
    except:
        #raise
        return common.code_error_response()


@medical_store_api.route('/web_app/Web_admin/medical_store_page/<int:medical_store_id>', methods=['GET'])
def get_detail_contact_person_in_medical_store_by_medical_id_in_admin(medical_store_id):
    try:
        contact_person_detail = MedicalStoreModel.load_detail_contact_person_in_medical_store_by_medical_id_in_admin(medical_store_id)
        final_out = common.convert_result_to_dict(contact_person_detail)
        app_in_json = jsonify(final_out)
        return common.custom_json_response(app_in_json, 200)
    except:
        return common.code_error_response()


