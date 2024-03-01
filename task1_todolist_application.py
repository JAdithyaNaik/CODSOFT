#COMMAND LINE APPLICATION OF TO DO LIST

#Author : Jatoth Adithya Naik
#for    : Intenship (TASK-1)


tasks = []

# main function
def main():
    print("\n***TO DO LIST APP***")
    while True :
        print("1.ADD")
        print("2.DELETE")
        print("3.VIEW")
        print("4.EXIT")
        choice=int(input("Enter your choice : "))
    
        if(choice == 1):
            item = input("Enter the task that you wanna add : ")
            add(item)
        elif(choice == 2):
            if(len(tasks)>0):
                print("YOUR TO DO TASKS : ")
                for i in range(len(tasks)):
                    print(f"{i+1}."+tasks[i])
                index = int(input("Enter the index of the Task that you wanna delete :"))
                delete(index)
            else:
                print("No Tasks to remove\n")
        elif(choice == 3):
            show()
        elif(choice == 4):
            print("Saving & Exiting ......\n")
        else:
            print("Enter valid input , please try again..\n")

# defining the functions i have called
def add(new_item):
    tasks.append(new_item)
    print("Added Task Successfully!!\n")

def show():
    if(len(tasks)==0):
         print("No Tasks to show\n")
    else:
        print("YOUR TASKS:")
        for i in range(len(tasks)):
            print(f"{i+1}."+tasks[i])
        print("Shown your Tasks Succesfully!!\n")
        
def delete(ind):
        tasks.pop(ind-1)
        print("Removed Task Successfully!!\n")
# main(recursion)
if __name__ == "__main__":
    main()
