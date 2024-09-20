# Function to sort tasks by priority using Bubble Sort
tasks = []

def arrange_tasks_by_importance():
    total_tasks = len(tasks)
    for outer in range(total_tasks):
        for inner in range(0, total_tasks - outer - 1):
            if tasks[inner][0] < tasks[inner + 1][0]:  # Swap if the importance is less (highest first)
                tasks[inner], tasks[inner + 1] = tasks[inner + 1], tasks[inner]
    print("Tasks arranged by importance.")