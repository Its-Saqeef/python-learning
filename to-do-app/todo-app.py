import csv
from pathlib import Path

TAKS_FILE = Path(__file__).with_name('tasks.csv')

def load_tasks():
    try:
        with open(TAKS_FILE, 'r') as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        return []


def save_tasks(task_list):
    with open(TAKS_FILE, 'w', newline='') as file:
        fieldnames = ['id', 'task', 'completed']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(task_list)

def add_task(task_list, task):
    """Add a new task to the task list."""
    id = len(task_list) + 1
    new_task = {'id': id, 'task': task, 'completed': 'False'}
    task_list.append(new_task)
    save_tasks(task_list)
    print(f'Task "{task}" added to the list.')

def mark_task_completed(task_list, task_id):
    """Mark a task as completed based on its ID."""
    for task in task_list:
        if str(task['id']) == task_id:
            task['completed'] = 'True'
            save_tasks(task_list)
            print(f'Task "{task["task"]}" marked as completed.')
            return
    print(f'No task found with ID {task_id}.')

def main():
    task_list = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as completed")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            if not task_list:
                print("No tasks found.")
            else:
                for task in task_list:
                    status = "Completed" if task['completed'] == 'True' else "Pending"
                    print(f"{task['id']}. {task['task']} - {status}")
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(task_list, task)
        elif choice == '3':
            for task in task_list:
                if(task['completed'] == "False"):
                    print(f'{task["id"]}. Task "{task["task"]}" is still pending.')
            task_id = input("Enter the task ID to mark as completed: ")
            mark_task_completed(task_list, task_id)
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()