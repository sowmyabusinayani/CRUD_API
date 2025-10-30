from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (in-memory)
tasks = [
    {"id": 1, "title": "Learn Flask", "done": False},
    {"id": 2, "title": "Study for ALBA test", "done": False}
]

# Home route


@app.route('/')
def home():
    return "Task Manager API is running!"

# READ - Get all tasks


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# READ - Get single task by ID


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    return jsonify(task) if task else ("Task not found", 404)

# CREATE - Add new task


@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = {
        "id": len(tasks) + 1,
        "title": data.get("title"),
        "done": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# UPDATE - Mark task as done


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    data = request.get_json()
    task["title"] = data.get("title", task["title"])
    task["done"] = data.get("done", task["done"])
    return jsonify(task)

# DELETE - Remove a task


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "Task deleted"})


if __name__ == '__main__':
    app.run(debug=True)
