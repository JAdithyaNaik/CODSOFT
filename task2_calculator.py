#COMMAND LINE APPLICATION OF CALCULATOR

#Author : Jatoth Adithya Naik
#for    : Intenship (TASK-2)

# Discription :
# this command appplication is for performing the arthmetic operations
# you can perform any arthematic operation(add,subtract,multiply,divide,remainder,floor division,power)

result =0

def main():
    print("\n\n\t\t\tby @JATOTH ADITHYA NAIK")
    print("________________________________________")
    print("\n\t\t\t***CALCULATOR APP***\n")
    while True :
        print("1.ADDITION")
        print("2.SUBTRACTION")
        print("3.MULTIPLICATION")
        print("4.DIVISION")
        print("5.MODULUS")
        print("6.FLLOR DIVISION")
        print("7.POWER")
        print("8.EXIT")
        a = int(input("\nEnter the first Operand :"))
        b = int(input("\nEnter the Second Operand :"))
        choice =int(input("Enter your Choice:"))

        if(choice == 1):
            add(a,b)
        elif(choice == 2):
            sub(a,b)
        elif(choice == 3):
            mul(a,b)
        elif(choice == 4):
            div(a,b)
        elif(choice == 5):
            mod(a,b)
        elif(choice == 6):
            flr(a,b)
        elif(choice == 7):
            power(a,b)
        elif(choice == 8):
            print("\nExiting\n")
            break;
        else:
            print("\nINVALID CHOICE , PLEASE TRY AGAIN LATER\n")


# defining the functions i have called
# add() method
def add(n,m):
    result = n+m
    print(f"Addition of {n} and {m} is : {result}")

 # sub() method   
def sub(n,m):
    result = n-m
    print(f"Subtraction of {n} and {m} is : {result}")

# mul() method
def mul(n,m):
    result = n*m
    print(f"Multiplication of {n} and {m} is : {result}")

# div() method
def div(n,m):
    result = n/m
    print(f"Division of {n} and {m} is : {result}")

# mod() method
def mod(n,m):
    result = n%m
    print(f"Modulus of {n} and {m} is : {result}")

# flr() method
def flr(n,m):
    result = n//m
    print(f"Floor Division of {n} and {m} is : {result}")
    
# power() method
def power(n,m):
    result = n**m
    print(f"{n} to the Power of {m} is : {result}")
    


    
# main(recursion)--used to repeated n no.of times
if __name__ == "__main__":
    main()
