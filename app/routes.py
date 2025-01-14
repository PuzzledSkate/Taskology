from flask import Blueprint, request, jsonify
from app.models import db, Task

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/todos', methods=['GET'])
def get_todos():
    tasks = Task.query.all()
    return jsonify([{
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'completed': task.completed
    } for task in tasks])

@api_blueprint.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    task = Task(title=data['title'], description=data.get('description', ''), completed=data.get('completed', False))
    db.session.add(task)
    db.session.commit()
    return jsonify({'message': 'Task created'}), 201

@api_blueprint.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    data = request.get_json()
    task = Task.query.get_or_404(id)
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.completed = data.get('completed', task.completed)
    db.session.commit()
    return jsonify({'message': 'Task updated'})

@api_blueprint.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted'})

@api_blueprint.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'OK'})

@api_blueprint.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Welcome to the To-Do API!',
        'endpoints': {
            '/todos': 'CRUD operations for tasks',
            '/health': 'Health check endpoint'
        }
    })

