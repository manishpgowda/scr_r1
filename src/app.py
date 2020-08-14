from flask import Flask
from .config import app_config
from .models import db, bcrypt
from .views.PatientMasterView import patient_api as patient_blueprint
from .views.ProviderMasterView import provider_api as provider_blueprint
from .views.ClinicMasterView import clinic_api as clinic_blueprint
from .views.ClinicOpMasterView import clinic_op_api as clinic_op_blueprint
from .views.ClinicStaffMasterView import clinic_staff_api as clinic_staff_blueprint
from .views.DegreeMasterView import degree_api as degree_blueprint
from .views.SpecialityMasterView import spec_api as spec_blueprint
from .views.ProviderTypeMasterView import providerType_api as providerType_blueprint
from .views.CityMasterView import city_api as cityapi_blueprint
from .views.ProviderPatientConsultationView import provider_consultation_api as provider_patient_consult_blueprint
from .views.MedicalStoreView import medical_store_api as medical_store_blureprint
from .views.PatientAppointmentView import patient_appointment_api as patient_appoitnment_blueprint
from .views.ProviderMedicalConnectView import provider_medical_connect_api as provider_medical_connect_blueprint
from .views.ClinicProviderMappingView import clinic_provider_mapping_api as clinic_provider_mapping_api_blueprint


def create_app(env_name):

    #app initiliazation
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])
    bcrypt.init_app(app)  # add this line
    db.init_app(app)  # add this line


    app.register_blueprint(patient_blueprint, url_prefix='/api/v1/Patients')  # add this line
    app.register_blueprint(degree_blueprint, url_prefix='/api/v1/Degree')  # add this
    app.register_blueprint(spec_blueprint, url_prefix='/api/v1/Speciality')  # add this
    app.register_blueprint(providerType_blueprint, url_prefix='/api/v1/Stream')  # add this
    app.register_blueprint(cityapi_blueprint, url_prefix='/api/v1/City')  # add this
    app.register_blueprint(provider_blueprint, url_prefix='/api/v1/Providers')  # add this line
    app.register_blueprint(patient_appoitnment_blueprint, url_prefix='/api/v1/Patient_appointment')  # add this line
    app.register_blueprint(clinic_blueprint, url_prefix='/api/v1/Clinics')  # add this line
    app.register_blueprint(clinic_staff_blueprint, url_prefix='/api/v1/Clinic_staff')  # add this
    app.register_blueprint(provider_patient_consult_blueprint, url_prefix='/api/v1/Provider_Patient_Consult')  # add this
    app.register_blueprint(clinic_op_blueprint, url_prefix='/api/v1/Clinic_op')  # add this line
    app.register_blueprint(medical_store_blureprint, url_prefix='/api/v1/Medical_store')  # add this line
    app.register_blueprint(provider_medical_connect_blueprint, url_prefix='/api/v1/Provider_Medical_Connect')
    app.register_blueprint(clinic_provider_mapping_api_blueprint, url_prefix='/api/v1/Clinic_Provider_Mapping')

    @app.route('/', methods=['GET'])
    def index():
        """
        example endpoint
        """
        return 'Congratulations! Your first endpoint is working'

    return app