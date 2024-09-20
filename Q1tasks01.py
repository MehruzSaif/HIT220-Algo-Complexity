task_collection = []

def add_task():
    try:
        priority = int(input("Enter task priority (as a number): "))
        due_date = input("Enter task due date (in YYYY-MM-DD format): ")
        new_entry = (priority, due_date)
        task_collection.append(new_entry)
        print(f"Task {new_entry} added!")

    except ValueError:
        print("Invalid input. Please enter a valid priority number and due date in the correct format.")

def display_task_collection():
    if not task_collection:
        print("No task_collection available.")
    else:
        print("Here are the current task_collection:")
        for new_entry in task_collection:
            print(f"Priority: {new_entry[0]}, Due Date: {new_entry[1]}")

# Function to sort tasks by priority using Bubble Sort
def arrange_task_collection_by_importance():
    total_task_collection = len(task_collection)
    for outer in range(total_task_collection):
        for inner in range(0, total_task_collection - outer - 1):
            if task_collection[inner][0] < task_collection[inner + 1][0]:  # Swap if the importance is less (highest first)
                task_collection[inner], task_collection[inner + 1] = task_collection[inner + 1], task_collection[inner]
    print("Task_cotask_collection arranged by importance.")

# Function to find the task with the highest
def locate_top_priority_task():
    if task_collection:
        print(f"The top priority task is: Priority: {task_collection[0][0]}, Due Date: {task_collection[0][1]}")
    else:
        print("No tasks available.")

# function to remove a task by its priority
def eliminate_task_by_priority(task_priority):
    for task in task_collection:
        if task[0] == task_priority:
            task_collection.remove(task)
            print(f"Task with priority {task_priority} removed!")

while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Display task_collection")
    print("3. Exit")

    selection = input("Choose an option (1/2/3): ")

    if selection == '1':
        add_task()
    elif selection == '2':
        display_task_collection()
    elif selection == '3':
        print("Exiting the task management system.")
        break
    else:
        print("Invalid option. Please choose 1, 2, or 3.")