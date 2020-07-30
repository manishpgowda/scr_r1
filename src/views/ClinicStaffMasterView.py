from flask import request, json, Response, Blueprint, jsonify
from ..models.ClinicStaffMasterModel import ClinicStaffMasterModel, ClinicStaffMasterSchema
from ..shared.CommonUtil import CommonUtil
#from ..shared.Authentication import Auth

clinic_staff_api = Blueprint('clinic_staff_api', __name__)
clinic_staff_schema = ClinicStaffMasterSchema()
common = CommonUtil()


# add clinic staff
@clinic_staff_api.route('/add', methods=['POST'])
def add():
    try:
        req_data = request.get_json()
        data = clinic_staff_schema.load(req_data)
        # # check if user already exist in the db
        clinic_staff_in_db = ClinicStaffMasterModel.get_staff_by_phone(data.get('phone_no'),data.get('clinic_id'))
        if clinic_staff_in_db:
            message = {'info': 'Clinic Staff already exists, please check the phone number or enter a new one'}
            return common.info_request_response(message)
        clinic_staff = ClinicStaffMasterModel(data)
        clinic_staff.user_name = clinic_staff.email_id
        clinic_staff.save()
        ser_data = clinic_staff_schema.dump(clinic_staff)
        return common.custom_response({'info': 'Clinic staff added successfully'}, 200)
    except:
        #raise
        return common.code_error_response()


# Update clinic staff
@clinic_staff_api.route('/update', methods=['PUT'])
def update():
    try:
        req_data = request.get_json()
        data = clinic_staff_schema.load(req_data, partial=True)
        clinic_staff = ClinicStaffMasterModel.get_clinic_staff_by_id(data.get('staff_id'))
        if not clinic_staff:
            message = {'info': 'Clinic staff does not exist, please check the details'}
            return common.info_request_response(message)
        clinic_staff.update(data)
        ser_staff = clinic_staff_schema.dump(clinic_staff)
        return common.custom_response(ser_staff, 201)
    except:
        #raise
        return common.code_error_response()



# Delete Clinic Staff
@clinic_staff_api.route('/delete', methods=['PUT'])
def delete():
    try:
        req_data = request.get_json()
        data = clinic_staff_schema.load(req_data, partial=True)
        clinic_staff = ClinicStaffMasterModel.get_clinic_staff_by_id(data.get('staff_id'))
        if not clinic_staff:
            message = {'info': 'Clinic staff does not exist, please check the details'}
            return common.info_request_response(message)
        clinic_staff.delete(data)
        ser_staff = clinic_staff_schema.dump(clinic_staff)
        return common.custom_response(ser_staff, 200)
    except:
        return common.code_error_response()


# Get list of clinic staff
@clinic_staff_api.route('/', methods=['GET'])
def get_all():
    try:
        clinic_staffs = ClinicStaffMasterModel.get_all_clinic_staff()
        ser_staff = clinic_staff_schema.dump(clinic_staffs, many=True)#.data
        return common.custom_response(ser_staff, 200)
    except:
        return common.code_error_response()


# get detail of one clinic staff
@clinic_staff_api.route('/<int:staff_id>', methods=['GET'])
def get_one_clinic_staff(staff_id):
    try:
        clinic_staff = ClinicStaffMasterModel.get_clinic_staff_by_id(staff_id)
        if not clinic_staff:
            return common.info_request_response({'info': 'clinic staff not found'})
        ser_staff = clinic_staff_schema.dump(clinic_staff)#.data
        return common.custom_response(ser_staff, 200)
    except:
        return common.code_error_response()



@clinic_staff_api.route('/list_by_clinic', methods=['GET'])
def get_clinic_staff_list():
    try:
        req_data = request.get_json()
        arg_list = None
        if not req_data:
            message = {'error': 'clinic_id args missing in the request'}
            return common.bad_request_response(message, 400)
        else:
            arg_list = req_data#json.loads(req_data)
        if 'clinic_id' in arg_list:
            _clinic_id = req_data['clinic_id']
        else:
            _clinic_id = 0

        if _clinic_id == 0:
            message = {'error': 'clinic_id args missing in the request call'}
            return common.bad_request_response(message, 400)
        print(_clinic_id)
        clinic_staffs = ClinicStaffMasterModel.get_clinic_staff_list(_clinic_id)
        ser_staff = clinic_staff_schema.dump(clinic_staffs,many=True)  # .data
        return common.custom_response(ser_staff, 200)
    except:
        raise
    #return common.custom_json_response(pat_lst, 200)
        return common.code_error_response()


@clinic_staff_api.route('/clinic_admin', methods=['GET'])
def get_clinic_admin_by_clinic(): #clinic_id,provider_id,user_type
    try:
        req_data = request.get_json()
        arg_list = req_data
        if not req_data:
            message = {'error': 'clinic_id args missing in the request'}
            return common.bad_request_response(message, 400)
        if 'clinic_id' in arg_list:
            _clinic_id = req_data['clinic_id']
        else:
            _clinic_id = 0

        if _clinic_id ==0:
            message = {'error': 'clinic_id args missing in the request call'}
            return common.bad_request_response(message, 400)
        # # check if user already exist in the db
        clinic_admin = ClinicStaffMasterModel.get_clinic_admin(_clinic_id)
        if not clinic_admin:
            message = {'error': 'clinic does not exist, please check the details'}
            return common.info_request_response(message)

        ser_data = clinic_staff_schema.dump(clinic_admin)
        # token = Auth.generate_token(ser_data.get('id'))
        return common.custom_response(ser_data, 200)
    except:
        return common.code_error_response()


# front desk list in web admin clinic page on click manage
@clinic_staff_api.route('/Web_admin/clinics_staff/<int:clinic_id>', methods=['GET'])
def get_list_of_front_desk_in_clinic_by_clinic_id(clinic_id):
    try:
        Staff_list = ClinicStaffMasterModel.load_list_of_front_desk_staff_by_clinic_id_in_admin(clinic_id)
        if not Staff_list:
            message = {'error': 'clinic_staff does not exist, please check the details'}
            return common.info_request_response(message)
        final_out = common.convert_result_to_dict(Staff_list)
        app_in_json = jsonify(final_out)
        return common.custom_json_response(app_in_json, 200)
    except:
        #raise
        return common.code_error_response()










