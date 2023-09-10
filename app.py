from flask import Flask, request, jsonify
from src.utils.data_manipulation import calculate_average
from src.jwt_auth import generate_token, verify_token
from src.config.database import create_database
from src.models.tasks import create_task, select_tasks
from werkzeug.security import check_password_hash, generate_password_hash
from src.controllers.tasks import controller_authenticate, controller_list_tasks, controller_add_task
from dotenv import load_dotenv
import os

load_dotenv()
 
app = Flask(__name__)
 
@app.route('/add_task', methods=['POST'])
def add_task():
    return controller_add_task()

@app.route('/list_tasks', methods=['GET'])
def list_tasks():
   return controller_list_tasks()

@app.route('/authenticate', methods=['POST'])
def authenticate():
   return controller_authenticate()

if __name__ == '__main__':
    create_database()
    app.run(host='0.0.0.0', port=os.getenv('PORT'), debug=os.getenv('DEBUG'))
