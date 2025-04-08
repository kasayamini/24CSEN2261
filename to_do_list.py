todo_list = []
while True:
    print("\nTo-Do List:")
    for idx, task in enumerate(todo_list, 1):
        print(f"{idx}. {task}")
    
    task = input("\nEnter a task to add (or type 'done' to finish): ")
    if task.lower() == 'done':
        break
    else:
        todo_list.append(task)



OUTPUT :
To-Do List:

Enter a task to add (or type 'done' to finish): journal

To-Do List:
1. journal

Enter a task to add (or type 'done' to finish): getting ready to college 

To-Do List:
1. journal
2. getting ready to college 

Enter a task to add (or type 'done' to finish): attending classes 

To-Do List:
1. journal
2. getting ready to college 
3. attending classes 

Enter a task to add (or type 'done' to finish): coming home 

To-Do List:
1. journal
2. getting ready to college 
3. attending classes 
4. coming home 

Enter a task to add (or type 'done' to finish): fresh up

To-Do List:
1. journal
2. getting ready to college 
3. attending classes 
4. coming home 
5. fresh up

Enter a task to add (or type 'done' to finish): do the given work 

To-Do List:
1. journal
2. getting ready to college 
3. attending classes 
4. coming home 
5. fresh up
6. do the given work 

Enter a task to add (or type 'done' to finish): done
