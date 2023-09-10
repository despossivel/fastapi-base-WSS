from flask import Flask, request, jsonify
from src.utils.data_manipulation import calculate_average
from src.jwt_auth import generate_token, verify_token
from src.config.database import create_database
from src.models.tasks import create_task, select_tasks
from werkzeug.security import check_password_hash, generate_password_hash
from dotenv import load_dotenv
import os

load_dotenv()

users = {
   'user': generate_password_hash(os.getenv('PASSWORD'))
}

def controller_add_task():
    data = request.get_json()
    title = data.get('title')
    
    if title: 
        create_task(title)
        return jsonify({'message': 'Task added successfully!'}), 201
    else:
        return jsonify({'error': 'Title is required!'}), 400
 
def controller_list_tasks():
    tasks_ = select_tasks()
    return jsonify({'tasks': tasks_})

 
def controller_authenticate():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and check_password_hash(users[username], password):
        token = generate_token(username)
        return jsonify({'token': token}), 200
    else:
        return jsonify({'error': 'Authentication failed'}), 401

 