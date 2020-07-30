from flask import request, json, Response, Blueprint
from random import randint
import re
from ..config import app_config, Development, Production


class CommonUtil():
    status_code = None
    otp_length = 4
    env_name = None

    def __init__(self):
        self.status_code = 404
        self.otp_length = 4

    def custom_response(self, res, status_code):
        """
        Custom Response Function
        """
        return Response(
            mimetype="application/json",
            response=json.dumps(res),
            status=status_code
        )

    def custom_json_response(self, res, status_code=200):
        return res

    def generate_otp(self):
        range_start = 10 ** (self.otp_length - 1)
        range_end = (10 ** self.otp_length) - 1
        otp = randint(range_start, range_end)
        return otp

    def is_valid_phone(self,phone_no):
        Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
        return Pattern.match(phone_no)

    def get_app_config(self):
        env_name = app_config['env_name']
        self.env_name = env_name
        if env_name == 'development':
            return Development()
        if env_name == 'production':
            return Production()

    def get_db_constring(self):
        config_obj = self.get_app_config()
        return config_obj.SQLALCHEMY_DATABASE_URI

    def convert_result_to_dict(self,result):
        res_obj = [dict(row) for row in result]
        return res_obj

    def code_error_response(self, error_code=555):
        message = {'error': 'An internal error occured'}
        return Response(
            mimetype="application/json",
            response=json.dumps(message),
            status=error_code
        )
    # use this when the api is requested with invalid synatx or arguments
    def bad_request_response(self,res, error_code=400):
        return Response(
            mimetype="application/json",
            response=json.dumps(res),
            status=error_code
        )
    # send this if you want to send an information response
    def info_request_response(self,res, error_code=556):
        return Response(
            mimetype="application/json",
            response=json.dumps(res),
            status=error_code
        )

