import json
from datetime import datetime

def add_task(task):
    tasks = load_tasks()
    task_details = {
        'Task': task,
        'Time': str(datetime.now())
    }
    tasks.append(task_details)
    save_tasks(tasks)
    print(f"Task added: {task}")

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)
        
def remove_task(task_index):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Task removed: {removed_task['task']}")
    else:
        print("Invalid task number")
