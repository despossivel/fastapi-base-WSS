from flask import Flask, request, jsonify
from data_manipulation import calculate_average
from jwt_auth import generate_token, verify_token
from database import create_database, create_task, select_tasks
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
 
users = {
    'user1': generate_password_hash('password1'),
    'user2': generate_password_hash('password2')
}

@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.get_json()
    title = data.get('title')
    
    if title:
        task_id = len(tasks) + 1   
        tasks[task_id] = {'title': title, 'completed': False}
        create_task(title)
 
        return jsonify({'message': 'Task added successfully!', 'task_id': task_id}), 201
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
    app.run(debug=True)
