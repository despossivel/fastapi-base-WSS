from flask import Flask, request, jsonify
from src.utils.data_manipulation import calculate_average
from src.jwt_auth import generate_token, verify_token
from src.config.database import create_database
from src.models.tasks import create_task, select_tasks
from werkzeug.security import check_password_hash, generate_password_hash
from dotenv import load_dotenv
import os

load_dotenv()
 
app = Flask(__name__)
 
users = {
   'user': generate_password_hash(os.getenv('PASSWORD'))
}

@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.get_json()
    title = data.get('title')
    
    if title: 
        create_task(title)
        return jsonify({'message': 'Task added successfully!'}), 201
    else:
        return jsonify({'error': 'Title is required!'}), 400

@app.route('/list_tasks', methods=['GET'])
def list_tasks():
    tasks_ = select_tasks()
    return jsonify({'tasks': tasks_})

@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and check_password_hash(users[username], password):
        token = generate_token(username)
        return jsonify({'token': token}), 200
    else:
        return jsonify({'error': 'Authentication failed'}), 401

if __name__ == '__main__':
    create_database()
    app.run(host='0.0.0.0', port=os.getenv('PORT'), debug=os.getenv('DEBUG'))
