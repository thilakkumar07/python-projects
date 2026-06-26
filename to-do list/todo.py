task_manager = {}

def create_task():
    task_no = int(input("Enter your Task Number: "))
    task = input("Enter Your Task: ")
    if task_no not in task_manager:
        task_manager[task_no] = task
        print(f"Your Task: '{task}' added Successfully.")
    else:  
        print("You number is already exist.")   
        

def delete_task():
    task_no = int(input("Enter your Task Number: "))
    
    if task_no in task_manager:
        del task_manager[task_no]
        print(f"You Task is Deleted Successfully.")
    else:
        print("Your task is not Available.")

def show_tasks():
    print("Your tasks")
    if len(task_manager) == 0:
        print("Your Task is Empty")
    for key, value in task_manager.items():
        print(f"{key}.{value}")
    
def edit_task():
    task_no = int(input("Enter your Task Number: "))
    new_task = input("Enter your new Task: ")
    if task_no in task_manager:
        task_manager[task_no] = new_task
        
    else:
        print("Your task is not Available.")
    
    
def todo_app():
    while True:
        user_request = int(input("\n 1.Create Task | 2.Delete Task | 3.Update Task | 4.Show Task | 5.Exit\n\nWhat work you do: "))
        if user_request == 1:
            create_task()
        elif user_request == 2:
            delete_task()
        elif user_request == 3:
            edit_task()
        elif user_request == 4:
            show_tasks()
        elif user_request == 5:
            break
        else:
            print("Invalid Request!")
            
try:
   todo_app()
except Exception as e:
    print(f"Something went wrong!\n{e}")
        
    