from flask import request, json, Blueprint, Response, jsonify
from ..models.ProviderMasterModel import ProviderMasterModel, ProviderMasterSchema
from ..shared.CommonUtil import CommonUtil

provider_api = Blueprint('provider_api', __name__)
provider_schema = ProviderMasterSchema()
common = CommonUtil()


#add a provider
@provider_api.route('/web_app/add', methods=['POST'])
def add():
    try:
        req_data = request.get_json()
        data = provider_schema.load(req_data)
        # # check if user already exist in the db
        provider_in_db = ProviderMasterModel.get_provider_by_phone(data.get('phone_no'))
        if provider_in_db:
            message = {'error': 'Provider already exist, please check the phone number or enter a new one'}
            return common.info_request_response(message)
        provider = ProviderMasterModel(data)
        provider.save()
        return common.custom_response({'info':'provider added successfully'}, 201)
    except:
        return common.code_error_response()


#update a provider
@provider_api.route('/web_app/update', methods=['PUT'])
def update():
    try:
        req_data = request.get_json()
        data = provider_schema.load(req_data, partial=True)
        provider = ProviderMasterModel.get_provider_by_id(data.get('provider_id'))
        if not provider:
            message = {'error': 'Provider does not exist'}
            return common.info_request_response(message)
        provider.update(data)
        ser_pat = provider_schema.dump(provider)
        return common.custom_response(ser_pat, 201)
    except:
        return common.code_error_response()


#delete a provider
@provider_api.route('/web_app/delete', methods=['PUT'])
def delete():
    try:
        req_data = request.get_json()
        data = provider_schema.load(req_data, partial=True)
        provider = ProviderMasterModel.get_provider_by_id(data.get('provider_id'))
        provider.delete(data)
        ser_prov = provider_schema.dump(provider)
        return common.custom_response(ser_prov, 201)
    except:
        raise
        # return common.code_error_response()


#get all providers
@provider_api.route('/web_app/', methods=['GET'])
def get_all():
    try:
        providers = ProviderMasterModel.get_all_providers()
        if not providers:
            return common.info_request_response({'info': 'provider not found'})
        ser_provs = provider_schema.dump(providers, many=True)#.data
        return common.custom_response(ser_provs, 200)
    except:
        return common.code_error_response()


#get one provider
@provider_api.route('/web_app/<int:provider_id>', methods=['GET'])
def get_one_provider(provider_id):
    try:
        provider = ProviderMasterModel.get_provider_by_id(provider_id)
        if not provider:
            return common.info_request_response({'error': 'provider not found'})
        ser_prov = provider_schema.dump(provider)#.data
        return common.custom_response(ser_prov, 200)
    except:
        #raise
        return common.code_error_response()


#get provider by phone num
@provider_api.route('/web_app/provider_by_phone', methods=['GET'])
def get_provider_by_phone():
    try:
        req_data = request.get_json()
        _phone_no = req_data['phone_no']
        # # check if user already exist in the db
        provider_in_db = ProviderMasterModel.get_provider_by_phone(_phone_no)
        if not provider_in_db:
            message = {'error': 'provider does not exist, please check the phone number'}
            return common.info_request_response(message)
        ser_data = provider_schema.dump(provider_in_db)
        return common.custom_response(ser_data, 200)
    except:
        return common.code_error_response()

#get provider by speciality
@provider_api.route('/web_app/provider_by_speciality', methods=['GET'])
def get_provider_by_speciality():
    try:
        req_data = request.get_json()
        _speciality_name = req_data['speciality']
        print(_speciality_name)
        # # check if user already exist in the db
        providers = ProviderMasterModel.get_provider_by_speciality(_speciality_name)
        if not providers:
            message = {'error': 'providers does not exist for the speciality entered'}
            return common.info_request_response(message)
        ser_data = provider_schema.dump(providers,many=True)
        return common.custom_response(ser_data, 200)
    except:
        #raise
        return common.code_error_response()


#get provider by speciality using function
@provider_api.route('/web_app/providers_by_spec', methods=['GET'])
def get_providers_by_speciality():
    try:
        req_data = request.get_json()
        arg_list = None
        if not req_data:
            message = {'error': 'person_id | spec_id args missing in the request'}
            return common.bad_request_response(message, 400)
        else:
            arg_list = req_data#json.loads(req_data)

        if 'person_id' in arg_list:
            _person_id = req_data['person_id']
        else:
            _person_id = 0

        if 'spec_id' in arg_list:
            _spec_id = req_data['spec_id']
        else:
            _spec_id = 0

        if 'sort_id' in arg_list:
            _sort_id = req_data['sort_id']
        else:
            _sort_id = 0

        if 'location_lat' in arg_list:
            _location_lat = req_data['location_lat']
        else:
            _location_lat = 0

        if 'location_lon' in arg_list:
            _location_lon = req_data['location_lon']
        else:
            _location_lon = 0

        if 'date' in arg_list:
            _date = req_data['date']
        else:
            _date = ''

        if 'provider_name' in arg_list:
            _provider_name = req_data['provider_name']
        else:
            _provider_name = ''

        if 'page_no' in arg_list:
            _page_no = req_data['page_no']
        else:
            _page_no = 0

        if _spec_id ==0 and _person_id ==0 :
            message = {'error': 'spec_id args missing in the request call'}
            return common.bad_request_response(message)
        #print(_clinic_id)
        prov_lst = ProviderMasterModel.get_providers_list_by_spec(_person_id, _spec_id, _sort_id, _location_lat, _location_lon, _date, _provider_name, _page_no )
        if not prov_lst:
            message = {'error': 'providers does not exist for the speciality'}
            return common.info_request_response(message, 400)
        final_out= common.convert_result_to_dict(prov_lst)
        prov_in_json = jsonify(final_out)
        # return common.custom_response(ser_data, 200)
        return common.custom_json_response(prov_in_json,200)
    except:
        #raise
        return common.code_error_response()

@provider_api.route('/web_app/provider_by_clinic', methods=['GET'])
def get_provider_by_clinic():
    try:
        req_data = request.get_json()
        arg_list = None
        if not req_data:
            message = {'error': 'clinic_id args missing in the request'}
            return common.bad_request_response(message, 400)
        else:
            arg_list = req_data  # json.loads(req_data)
        if 'clinic_id' in arg_list:
            _clinic_id = req_data['clinic_id']
        else:
            _clinic_id = 0

        if _clinic_id == 0:
            message = {'error': 'clinic_id args missing in the request call'}
            return common.bad_request_response(message, 400)
        providers = ProviderMasterModel.get_provider_list(_clinic_id,'sys')
        if not providers:
            message = {'error': 'providers does not exist for the speciality entered'}
            return common.info_request_response(message)
        final_out = common.convert_result_to_dict(providers)
        prov_in_json = jsonify(final_out)
        return common.custom_json_response(prov_in_json, 200)
    except:
        raise
        # return common.code_error_response()

@provider_api.route('/web_app/book_appointment/provider_list/<int:clinic_id>', methods=['GET'])
def get_provider_list_in_book_new_appointment(clinic_id):
    try:
        provider_list_BA = ProviderMasterModel.load_provider_list_in_book_new_appointment(clinic_id)
        final_out = common.convert_result_to_dict(provider_list_BA)
        app_in_json = jsonify(final_out)
        return common.custom_json_response(app_in_json, 200)
    except:
        raise
        # return common.code_error_response()


@provider_api.route('/web_app/bookmarked_patients/<int:provider_id>', methods=['GET'])
def get_bookmarked_patients_by_provider_id(provider_id):
    try:
        bookmarked_list = ProviderMasterModel.load_bookmarked_patients_by_provider_id(provider_id)
        final_out = common.convert_result_to_dict(bookmarked_list)
        app_in_json = jsonify(final_out)
        return common.custom_json_response(app_in_json, 200)
    except:
        raise
        # return common.code_error_response()


@provider_api.route('/web_app/follow_up_patients/<int:provider_id>', methods=['GET'])
def get_follow_up_patients_by_provider_id(provider_id):
    try:
        follow_up_list = ProviderMasterModel.load_follow_up_patients_by_provider_id(provider_id)
        final_out = common.convert_result_to_dict(follow_up_list)
        app_in_json = jsonify(final_out)
        return common.custom_json_response(app_in_json, 200)
    except:
        raise
        # return common.code_error_response()

# provider list in web admin in provider section
@provider_api.route('/web_app/Web_admin/provider_list', methods=['GET'])
def get_provider_list_web_admin_provider_page():
    try:
        provider_list_web_admin = ProviderMasterModel.load_provider_list_in_web_admin_provider_section()
        if provider_list_web_admin:
            final_out = common.convert_result_to_dict(provider_list_web_admin)
            app_in_json = jsonify(final_out)
            return common.custom_json_response(app_in_json, 200)
    except:
        raise
        # return common.code_error_response()