# Initialize an empty list to store tasks
task_list = []

# Function to add a new task to the list
def add_task(priority, due_date):
    task = (priority, due_date)
    task_list.append(task)

# Function to display all tasks
def display_tasks():
    # Sort tasks by priority (ascending order)
    sorted_tasks = sorted(task_list, key=lambda x: x[0])
    
    # Display sorted tasks
    if not sorted_tasks:
        print("No tasks available.")
    else:
        print("Tasks (sorted by priority):")
        for task in sorted_tasks:
            print(f"Priority: {task[0]}, Due Date: {task[1]}")

# Example usage:
add_task(5, "2024-09-10")
add_task(2, "2024-09-12")
add_task(3, "2024-09-15")

display_tasks()