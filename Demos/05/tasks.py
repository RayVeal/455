import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'tasks.sqlite')
db = SQLAlchemy(app)

# Task Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, default=False)

# Endpoint 1: Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    task_list = [{"id": task.id, "title": task.title, "done": task.done} for task in tasks]
    return jsonify({"tasks": task_list})

# Endpoint 2: Get a specific task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get(task_id)
    if task:
        return jsonify({"task": {"id": task.id, "title": task.title, "done": task.done}})
    else:
        return jsonify({"error": "Task not found"}), 404

# Endpoint 3: Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    if "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    new_task = Task(title=data['title'], done=False)
    db.session.add(new_task)
    db.session.commit()

    return jsonify({"message": "Task created", "task": {"id": new_task.id, "title": new_task.title, "done": new_task.done}}), 201

# Endpoint 4: Remove a specific task by ID
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def remove_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"})

if __name__ == '__main__':
    #with app.app_context():
     #   db.create_all()
    app.run(debug=True)
