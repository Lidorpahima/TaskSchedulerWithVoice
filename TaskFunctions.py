import json
from datetime import datetime
from fuzzywuzzy import fuzz,process
from playsound import playsound
count = 0 # Task Number

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ADD TASK~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def add_task(task):
    tasks = load_tasks()
    if tasks:
        count = tasks[-1]['Task Number -'] + 1
    else:
        count = 1
    task_details = {
        'Task Number -': count ,
        'Task - ': task,
        'Time - ': str(datetime.now())

    }
    tasks.append(task_details)
    save_tasks(tasks)
    print(f"Task added: {task}")
    playsound('reminder_sound.wav')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~LOAD TASKS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: tasks.json is empty or corrupted.")
        return []

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DISPLAY TASKS MORE FRIENDLY~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def display_tasks():
    tasks = load_tasks()
    if tasks:
        print("Your tasks:")
        for task in tasks:
            print(f"Task Number: {task['Task Number -']}, Task: {task['Task - ']}, Time: {task['Time - ']}")
    else:
        print("No tasks found.")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~SAVE TASKS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~REMOVE TASK~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def remove_task(task_name):
    tasks = load_tasks()
    task_names = [task['Task - '] for task in tasks]
    best_match = process.extractOne(task_name, task_names, scorer=fuzz.ratio)
    if best_match and best_match[1] >= 30:
        task_index = task_names.index(best_match[0])
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Task removed: {removed_task['Task - ']}")
        playsound('reminder_sound.wav')
    else:
        print("Task not found. Please try again.")

