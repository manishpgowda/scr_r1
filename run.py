# /run.py
import os

from src.app import create_app
env_name = 'development'  ##os.getenv('FLASK_ENV')
app = create_app(env_name)

if __name__ == '__main__':

    # run app
    # app.run()
    app.run(host='127.0.0.1', port=8000, debug=True)
    # app.run(host='0.0.0.0', port=8080)