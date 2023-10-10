from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    #rv437 and 10/09/23 List a summary view of all tasks 
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line

def add_task(name: str, description: str, due: str):
    #rv437 and 10/09/23 here we are adding tasks to the tracker app
    missing_fields = []
    if not name:
        missing_fields.append('name')
    if not description:
        missing_fields.append('description')
    if not due:
        missing_fields.append('due')

    if missing_fields:
        print(f"Error: The following required fields are missing: {', '.join(missing_fields)}")
        return
    
    task = TASK_TEMPLATE.copy()
    task['name'] = name
    task['description'] = description
    task['due'] = str_to_datetime(due)
    task['lastActivity'] = datetime.now()
    tasks.append(task)
    print("Task added successfully.")
    save()

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    #rv437 and 10/06/23 here we can select a task and update any field according to our reqiurements.
    if 0 <= index < len(tasks):
        task = tasks[index]
       

        name = input(f"What's the name of this task?   ({task['name']}) \n").strip()
        description = input(f"What's a brief descriptions of this task?  ({task['description']}) \n").strip()
        due = input(f"When is this task due (format: m/d/y H:M:S)  ({task['due']}) \n").strip()

        update_task(index, name=name if name else None, description=description if description else None, due=due if due else None)
    else:
        print("Invalid task index.")

def update_task(index: int, name: str = None, description: str = None, due: str = None):
    #rv437 and 10/08/23 Here we are updating the existing task 
    global tasks  # Assuming tasks is a global variable that holds task information
    if index < 0 or index >= len(tasks):
        return "Invalid index. Task not updated."
    task = tasks[index]
    updated = False
    if name is not None:
        task['name'] = name
        updated = True

    if description is not None:
        task['description'] = description
        updated = True

    if due is not None:
        task['due'] = due
        updated = True

    if updated:
        task['lastActivity'] = datetime.now()
        save()  # Assuming there's a save() function to save the changes
        print("Task updated successfully.")
    else:
        print("No updates provided. Task not updated.")


def mark_done(index):
    #rv437 and 10/09/23 this helps to mark a task as done
    if 0 <= index < len(tasks):
        task = tasks[index]
        if not task.get('done'):
            task['done'] = datetime.now()
            print("Task marked as done.")
        else:
            print("Task is already completed.")
        save()
    else:
        print("Invalid task index.")

def view_task(index):
    #rv437 and 10/09/23 Here we can use this function to view specific task 
    if 0 <= index < len(tasks):
        task = tasks[index]
        done_status = task.get('done', False)
        due_date = task.get('due', 'Not specified')
        print(f"""
            [{'x' if done_status else ' '}] Task: {task['name']}
            Description: {task['description']}
            Last Activity: {task['lastActivity']}
            Due: {due_date}
            Completed: {task['done'] if task.get('done') else '-'}
            """.replace('  ', ' '))
    else:
        print("Invalid task index.")

        
def delete_task(index):
    #rv437 and 10/09/23 here we use this to delete a task 
    if 0 <= index < len(tasks):
        del tasks[index]
        print("Task deleted successfully.")
        save()
    else:
        print("Invalid task index.")
        
def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    # generate a list of tasks where the task is not done
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    _tasks = [] # <-- this is a placeholder to populate based on the above requirements
    list_tasks(_tasks)

def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    # generate a list of tasks where the due date is older than "now" and that are not complete (i.e., not done)
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    _tasks = [] # <-- this is a placeholder to populate based on the above requirements
    list_tasks(_tasks)

def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # get the days, hours, minutes, seconds between the due date and now
    # display the remaining time via print in a clear format showing X days, X hours, X minutes, X seconds (time components must be clearly separated)
    # example: 1 day, 0 hours, 0 minutes, 0 seconds remaining
    # if the due date is in the past print out how many days, hours, minutes, seconds the task is overdue (clearly note that it's overdue, values should be positive)
    # example: 0 days, 2 hours, 5 minutes, 10 seconds overdue (note there's no negative values)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    task = {}# <-- this is a placeholder to populate based on the above requirements
    # do your print logic here

# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()