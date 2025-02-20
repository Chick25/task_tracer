
import json
import os

if os.path.exists('task.json'):
    with open('task.json') as file:
        task_list = json.load(file)
else:
    task_list = {}

def save_task():
    with open('task.json', 'w') as file:
        json.dump(task_list, file, indent=4)
    
def add_task():
    task = input('Enter the task name: ')
    if task in task_list:
        print('Task already exists')
        return
    task_list[task] = 'Not Started'
    #json_string = json.dumps(task_list, indent=4)
    save_task()
    print('Task added successfully')

def update_task():
    task_old = input('Enter the old task name: ')
    if task_old not in task_list:
        print('Task not found')
        return
    
    task_new = input('Enter the new task name: ')
    task_list[task_new] = task_list.pop(task_old)
    save_task()
    print('Task updated successfully')

def del_task():
    task = input('Enter the task name: ')
    if task not in task_list:
        print('Task not found')
        return
    del task_list[task]
    save_task() 
    print('Task deleted successfully')

def status_task():
    task = input('Enter the task name: ')
    if task not in task_list:
        print('Task not found')
        return
    status = input('Input status of the task is: ').lower()
    task_list[task] = status
    save_task()
    print('Task status updated successfully')

print('1. Add task')
print('2. Update task')
print('3. Delete task')
print('4. Status task')
print('5. View all tasks')
print('6. View all done tasks')
print('7. View all not done tasks')
print('8. View all in progress tasks')
print('9. Exit')

while True:

    option = int(input('Enter the option: '))
    if option == 1:
        add_task()
    elif option == 2:
        update_task()
    elif option == 3:
        del_task()
    elif option == 4:
        status_task()
    elif option == 5:
        print(task_list)
    elif option == 6:
        st = {key: value for key, value in task_list.items() if value == 'done'}
        print(st)
        if st == {}:
            print('No task is done')
    elif option == 7:
        st = {key: value for key, value in task_list.items() if value == 'not done'}
        print(st)
        if st == {}:
            print('No task is not done')
    elif option == 8:
        st = {key: value for key, value in task_list.items() if value == 'in progress'}
        print(st)
        if st == {}:
            print('No task is in progress')
    else:
        print('Invalid option')
    if option == 9:
        break