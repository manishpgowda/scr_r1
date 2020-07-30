import os

class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://qjbisntxylqejw:541680ab26610c302fd02853e2995a3ecd88e951acca0a6599b8fd697076e9d9@ec2-107-21-110-75.compute-1.amazonaws.com:5432/dh1g5k9tddipq'  # os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = 'hhgaghhgsdhdhdd'  # os.getenv('JWT_SECRET_KEY')

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://qjbisntxylqejw:541680ab26610c302fd02853e2995a3ecd88e951acca0a6599b8fd697076e9d9@ec2-107-21-110-75.compute-1.amazonaws.com:5432/dh1g5k9tddipq' #os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = 'hhgaghhgsdhdhdd'#os.getenv('JWT_SECRET_KEY')


app_config = {
    'development': Development,
    'production': Production,
    'env_name': 'development'
}

