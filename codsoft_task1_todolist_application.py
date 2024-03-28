#COMMAND LINE APPLICATION OF TO DO LIST

#Author : Jatoth Adithya Naik
#for    : Intenship (TASK-1)

# Discription :
# this command appplication is for tracking your tasks
# you can add,delete and view your tasks by choosing respective choices

# empty task list
tasks = []

# main function
def main():
    print("\n\n\t\t\tby @JATOTH ADITHYA NAIK")
    print("________________________________________")
    print("\n\t\t\t***TO DO LIST APP***\n") 
    while True :
        # options for user
        print("1.ADD")
        print("2.DELETE")
        print("3.VIEW")
        print("4.UPDATE")
        print("5.EXIT")
        # taking input from the user
        choice=int(input("Enter your choice : "))
        print("\n")
        
        # for adding the task
        if(choice == 1):
            # taking the task from the user
            item = input("Enter the task that you wanna add : ")
            # adding the task to the tasks list with add(item) function
            add(item)
            
        # for deleting the task
        elif(choice == 2):
            # checking the number of tasks in the list
            if(len(tasks)>0):
                print("YOUR TO DO TASKS : ")
                for i in range(len(tasks)):
                    print(f"{i+1}."+tasks[i])
                print("NOTE THAT INDEXING STARTS FROM '1' ONLY")
                index = int(input("Enter the index of the Task that you wanna delete :"))
                # deleting the task by using delete(index) function
                delete(index)
            else:
                print("No Tasks to remove\n")
                
        # for viewing the tasks
        elif(choice == 3):
            # viewing the tasks by using show() function
            show()
            
        # for updating the task
        elif(choice == 4):
            print("YOUR TO DO TASKS : ")
            for i in range(len(tasks)):
                print(f"{i+1}."+tasks[i])
            print("NOTE THAT INDEXING STARTS FROM '1' ONLY")
            index = int(input("Enter the index of the Task that you wanna update :")) 
            # updating the task by using update(index) function
            update(index)
            
        # for exiting from the app
        elif(choice == 5):
            print("Saving & Exiting ......\n")
            break;
        
        # for default case
        else:
            print("Enter valid input , please try again..\n")



# defining the functions I have used above

# add() method
# takes the task from the user and adds it to the list
def add(new_item):
    tasks.append(new_item)
    print("Added Task Successfully!!\n")
    print("________________________________________")

# delete() method
# takes index from the user and deletes that particular task
def delete(ind):
        tasks.pop(ind-1)
        print("Removed Task Successfully!!\n")
        print("________________________________________")
        
# show() method
# prints all the tasks on the console
def show():
    if(len(tasks)==0):
         print("No Tasks to show\n")
    else:
        print("YOUR TASKS:")
        for i in range(len(tasks)):
            print(i+1,end=".")
            print(tasks[i])
        print("Shown your Tasks Succesfully!!\n")
    print("________________________________________") 
    
    
# update() method
# takes the index of the task to be update and modifies it
def update(ind):
    tasks.pop(ind-1)
    upd_task=input("Enter your new task : ")
    tasks.insert(ind-1,upd_task)
    print("Updated Task Successfully!!\n")
    print("________________________________________")

# main function
if __name__ == "__main__":
    main()
