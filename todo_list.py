# a to-do list project 

tasks = []

while True:
    print("\n\033[1mHEYY DEAR, Welcome to customisable to-do list\033[0m\n")
    print("PRESS: 1 -- To add a task.")
    print("PRESS: 2 -- To view all tasks.")
    print("PRESS: 3 -- Mark a task as completed.")
    print("PRESS: 4 -- Delete a task.")
    print("PRESS: 5 -- Exit.\n")
 
    try:
        n = int(input("GOOD DAY. Please enter your option number: ")) 
    except ValueError:
        print("Invalid input entered please enter a number between 1 - 5")    
        continue  
    if n == 5:
        print("Exit successfull")
        break   
    elif n ==4:
        print("Option number 4 selected successfully. Please delete a task")
        if not tasks:
            print("There are no tasks to be deleted")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['tittle']}")
            try:
                delete_task = int(input("Please select the task number you want to delete: "))
                tasks.pop(delete_task - 1)
                print("Task has been deleted successfully")
            except (ValueError, IndexError):
                print("Invalid task number entered")     

    elif n ==3:
        print("Option number 3 selected successfully. Please mark a task as completed")
        if not tasks:
            print("No tasks to mark")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['tittle']}")   

            try:
                m = int(input("Please enter the task number you want to mark as completed: "))
                tasks[m - 1]["completed"] = True
                print("Task marked as complete successfully")
            except (ValueError, IndexError): 
                print("Invalid task number entered")   

    elif n ==2:
        print("Option number 2 selected successfully. Your tasks are listed down here") 
        if not tasks:
            print("No tasks are available")
        else:
            for index, task in enumerate(tasks, start=1):
                status = "✔" if task["completed"] else "✘"    
                print(f"{index}. {task['tittle']} : {status}")

    elif n ==1:
        print("Option number 1 selected successfully. Please enter a task to add")
        task_name = input("Please enter the task you want to add: ")
        task = {
            "tittle" : task_name,
            "completed" : False
        }
        tasks.append(task)
        print("Task has been added successfully")

    else:
        print("Invalid input please select a number between from 1 - 5")   
