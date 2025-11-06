todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Added: {task}")

def edit_task(index, new_task):
    if 0 <= index < len(todo_list):
        print(f"Task '{todo_list[index]}' changed to '{new_task}'")
        todo_list[index] = new_task
    else:
        print("Invalid task number!")

def delete_task(index):
    if 0 <= index < len(todo_list):
        print(f"Deleted: {todo_list.pop(index)}")
    else:
        print("Invalid task number!")

def show_tasks():
    print("\nYour To-Do List:")
    for i, task in enumerate(todo_list):
        print(f"{i}. {task}")
    print()

add_task("Complete assignment")
add_task("Read Open source articles")
show_tasks()

edit_task(0, "Complete lab manual")
delete_task(1)
show_tasks()
