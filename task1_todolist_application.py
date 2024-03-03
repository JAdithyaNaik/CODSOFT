#COMMAND LINE APPLICATION OF TO DO LIST

#Author : Jatoth Adithya Naik
#for    : Intenship (TASK-1)

# Discription :
# this command appplication is for tracking your tasks
# you can add,delete and view your tasks by choosing respective choices

tasks = []

# main function
def main():
    print("\n\n\t\t\tby @JATOTH ADITHYA NAIK")
    print("________________________________________")
    print("\n\t\t\t***TO DO LIST APP***\n")
    while True :
        print("1.ADD")
        print("2.DELETE")
        print("3.VIEW")
        print("4.EXIT")
        choice=int(input("Enter your choice : "))
        print("\n")
        if(choice == 1):
            item = input("Enter the task that you wanna add : ")
            add(item)
        elif(choice == 2):
            if(len(tasks)>0):
                print("YOUR TO DO TASKS : ")
                for i in range(len(tasks)):
                    print(f"{i+1}."+tasks[i])
                print("NOTE THAT INDEXING STARTS FROM '1' ONLY")
                index = int(input("Enter the index of the Task that you wanna delete :"))
                delete(index)
            else:
                print("No Tasks to remove\n")
        elif(choice == 3):
            show()
        elif(choice == 4):
            print("Saving & Exiting ......\n")
            break;
        else:
            print("Enter valid input , please try again..\n")

# defining the functions i have called
# add() method
def add(new_item):
    tasks.append(new_item)
    print("Added Task Successfully!!\n")
    print("________________________________________")

# show() method
def show():
    if(len(tasks)==0):
         print("No Tasks to show\n")
    else:
        print("YOUR TASKS:")
        for i in range(len(tasks)):
            print(f"{i+1}."+tasks[i])
        print("Shown your Tasks Succesfully!!\n")
    print("________________________________________") 

# delete() method
def delete(ind):
        tasks.pop(ind-1)
        print("Removed Task Successfully!!\n")
        print("________________________________________")




# main(recursion)--used to repeated n no.of times
if __name__ == "__main__":
    main()
