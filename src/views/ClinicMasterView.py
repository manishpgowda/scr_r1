from flask import request, json, Response, Blueprint, jsonify
from ..models.ClinicMasterModel import ClinicMasterModel, ClinicMasterSchema
from ..shared.CommonUtil import CommonUtil
#from ..shared.Authentication import Auth

clinic_api = Blueprint('clinic_api', __name__)
clinic_schema = ClinicMasterSchema()
common = CommonUtil()


#add clinic
@clinic_api.route('/web_app/add', methods=['POST'])
def add():
    try:
        req_data = request.get_json()
        data = clinic_schema.load(req_data)
        # # check if user already exist in the db
        clinic_in_db = ClinicMasterModel.get_clinic_by_phone(data.get('clinic_phone_no'))
        if clinic_in_db:
            message = {'info': 'Clinic already exist, please check the phone number or enter a new one'}
            return common.info_request_response(message)
        clinic = ClinicMasterModel(data)
        clinic.save()
        return common.custom_response({'info':'clinic added successfully'}, 201)
    except:
        return common.code_error_response()


#update the clinic details
@clinic_api.route('/web_app/update', methods=['PUT'])
def update():
    try:
        req_data = request.get_json()
        data = clinic_schema.load(req_data, partial=True)
        clinic = ClinicMasterModel.get_clinic_by_id(data.get('clinic_id'))
        if not clinic:
            message = {'info': 'Clinic does not exist, please check the details'}
            return common.info_request_response(message)
        clinic.update(data)
        ser_pat = clinic_schema.dump(clinic)
        return common.custom_response(ser_pat, 201)
    except:
        return common.code_error_response()


#delete the clinic
@clinic_api.route('/web_app/delete', methods=['PUT'])
def delete():
    try:
        req_data = request.get_json()
        data = clinic_schema.load(req_data, partial=True)
        clinic = ClinicMasterModel.get_clinic_by_id(data.get('clinic_id'))
        if not clinic:
            message = {'info': 'Clinic does not exist, please check the details'}
            return common.info_request_response(message)
        clinic.delete(data)
        ser_pat = clinic_schema.dump(clinic)
        return common.custom_response(ser_pat, 201)
    except:
        return common.code_error_response()


#get all clinics
@clinic_api.route('/web_app/', methods=['GET'])
def get_all_clinics():
    try:
        clinics = ClinicMasterModel.get_all_clinics()
        ser_pats = clinic_schema.dump(clinics, many=True)  # .data
        return common.custom_response(ser_pats, 200)
    except:
        return common.code_error_response()


#get clinic by clinic id
@clinic_api.route('/web_app/<int:clinic_id>', methods=['GET'])
def get_clinic_by_id(clinic_id):
    try:
        clinic = ClinicMasterModel.get_clinic_by_id(clinic_id)
        if not clinic:
            return common.info_request_response({'info': 'clinic not found'})
        ser_pat = clinic_schema.dump(clinic)  # .data
        return common.custom_response(ser_pat, 200)
    except:
        return common.code_error_response()


#get clinic by phone number
@clinic_api.route('/web_app/clinic_by_phone', methods=['GET'])
def get_clinic_by_phone():
    try:
        req_data = request.get_json()
        _phone_no = req_data['phone_no']
        # # check if user already exist in the db
        clinic_in_db = ClinicMasterModel.get_clinic_by_phone(_phone_no)
        if not clinic_in_db:
            message = {'info': 'Clinic does not exist, please check the phone number'}
            return common.info_request_response(message)
    except:
        return common.code_error_response()


#get clinic list
@clinic_api.route('/web_app/clinic_list', methods=['GET'])
def get_clinic_lists():
    try:
        req_data = request.get_json()
        arg_list = None
        if not req_data:
            message = {'error': 'location args missing in the request'}
            return common.bad_request_response(message, 404)
        else:
            arg_list = req_data  # json.loads(req_data)

        if 'location_lat' in arg_list:
            _location_lat = req_data['location_lat']
        else:
            _location_lat = 0

        if 'location_lon' in arg_list:
            _location_lon = req_data['location_lon']
        else:
            _location_lon = 0

        if 'clinic_name' in arg_list:
            _clinic_name = req_data['clinic_name']
        else:
            _clinic_name = ''

        if 'page_no' in arg_list:
            _page_no = req_data['page_no']
        else:
            _page_no = 0

        clinics = ClinicMasterModel.get_clinic_list_and_search(_location_lat, _location_lon, _clinic_name, _page_no)
        if not clinics:
            message = {'error': 'clinics does not exist'}
            return common.custom_response(message)
        final_out = common.convert_result_to_dict(clinics)
        clinic_in_json = jsonify(final_out)
        # return common.custom_json_response(app_in_json, 200)
        return common.custom_json_response(clinic_in_json, 200)
    except:
        #raise
        return common.code_error_response()


# get clinic list in web_admin section Clinics page
@clinic_api.route('/web_app/web_admin/clinics_page_list', methods=['GET'])
def get_clinic_list_for_clinics_page_in_admin():
    try:
        list = ClinicMasterModel.load_list_for_clinics_page_in_admin()
        if list:
            final_out = common.convert_result_to_dict(list)
            app_in_json = jsonify(final_out)
            return common.custom_json_response(app_in_json, 200)
    except:
        # raise
        return common.code_error_response()

#get provider list in web_admin section clinc page onclick view button
@clinic_api.route('/web_app/web_admin/provider_list/<int:clinic_id>', methods=['GET'])
def get_list_of_provider_in_clinic_by_clinic_id(clinic_id):
    try:
        provider_list_by_clinic_id = ClinicMasterModel.load_list_of_providers_clinics_page_in_admin_by_clinic_id_onclick_view_button(clinic_id)
        # if not provider_list_by_clinic_id:
        #     message = {'error': 'provider does not exist in clinic'}
        #     return common.custom_response(message, 404)
        final_out = common.convert_result_to_dict(provider_list_by_clinic_id)
        app_in_json = jsonify(final_out)
        return common.custom_json_response(app_in_json, 200)
    except:
        raise
        # return common.code_error_response()

#providers in clinic with speciality in front desk home page
@clinic_api.route('/front_desk_home_page/web_app/providers_in_clinic', methods=['GET'])
def get_providers_in_clinic():
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

        if 'page_no' in arg_list:
            _page_no = req_data['page_no']
        else:
            _page_no = 0

        if _clinic_id == 0:
            message = {'error': 'clinic_id args missing in the request call'}
            return common.bad_request_response(message, 400)

        clinics = ClinicMasterModel.get_providers_by_speciality_in_cinic(_clinic_id, _date_pref, _page_no)
        if not clinics:
            message = {'error': 'clinics does not exist '}
            return common.info_request_response(message, 404)
        final_out = common.convert_result_to_dict(clinics)
        clinic_in_json = jsonify(final_out)
        # return common.custom_json_response(app_in_json, 200)
        return common.custom_json_response(clinic_in_json, 200)
    except:
        #raise
        return common.code_error_response()