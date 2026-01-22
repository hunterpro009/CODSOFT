def task():
    task_list = []
    print("welcome to your TO DO LIST")

    total_tasks = int(input("how many tasks do you want to add?"))
    for i in range(total_tasks):
        task_name = input(f"enter the name of task {i+1}:")
        task_list.append(task_name)
    print(f"your tasks are\n {task}")

    while True:
        operation = int(input("what do you want to do? 1. add task 2. remove task 3. view tasks 4. exit"))
        if operation == 1:
            new_task = input("enter the name of the task to add:")
            task_list.append(new_task)
            print(f"task '{new_task}' added.")
        elif operation == 2:
            remove_task = input("enter the name of the task to remove:")
            if remove_task in task_list:
                task_list.remove(remove_task)
                print(f"task '{remove_task}' removed.")
            else:
                print(f"task '{remove_task}' not found in the list.")
        elif operation == 3:
            print("your current tasks are:")
            for idx, task in enumerate(task_list, start=1):
                print(f"{idx}. {task}")
        elif operation == 4:
            print("exiting the TO DO LIST. Goodbye!")
            break
        else:
            print("invalid option, please try again.")