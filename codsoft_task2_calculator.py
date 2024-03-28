#COMMAND LINE APPLICATION OF CALCULATOR

#Author : Jatoth Adithya Naik
#for    : Intenship (TASK-2)

# Discription :
# this command appplication is for performing the arthmetic operations
# you can perform any arthematic operation(add,subtract,multiply,divide,remainder,floor division,power)
# handled exceptions
result =0

def main():
        print("\n\n\t\t\tby @JATOTH ADITHYA NAIK")
        print("________________________________________")
        print("\n\t\t\t***CALCULATOR APP***\n")
        while True :
            # choices for user
            print("1.ADDITION")
            print("2.SUBTRACTION")
            print("3.MULTIPLICATION")
            print("4.DIVISION")
            print("5.MODULUS")
            print("6.FLLOR DIVISION")
            print("7.POWER")
            print("8.EXIT")
            # taking input from the user
            choice =int(input("\nEnter your Choice : "))
            # for exiting 
            if(choice == 8):
                print("\n\n")
                break
            # for checking out of range choices
            elif(choice>8):
                print("\nINVALID CHOICE , PLEASE TRY AGAIN LATER\n")
            else:
                a = float(input("\nEnter the first Number : "))
                b = float(input("Enter the Second Number : "))

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
                    print("\nExiting from Calculator......\n")
                    break;
                else:
                    print("\nINVALID CHOICE , PLEASE TRY AGAIN LATER\n")
            

# defining the functions I have called
#  All methods takes 2 numbers as arguments and prints the result accounding to the choice choosen

# add() method
def add(n,m):
    result = n+m
    print(f"\nAddition of {n} and {m} is : {result}")
    print("________________________________________")

 # sub() method   
def sub(n,m):
    result = n-m
    print(f"\nSubtraction of {n} and {m} is : {result}")
    print("________________________________________")

# mul() method
def mul(n,m):
    result = n*m
    print(f"\nMultiplication of {n} and {m} is : {result}")
    print("________________________________________")

# div() method
def div(n,m):
    if(m == 0):
        print("\nCan't Divide by 'Zero'")
    else:
        result = n/m
        print(f"\nDivision of {n} and {m} is : {result}")
    print("________________________________________")

# mod() method
def mod(n,m):
    if(m == 0):
        print("\nCan't Divide by 'Zero'")
    else:
        result = n%m
        print(f"\nModulus of {n} and {m} is : {result}")
    print("________________________________________")
    
# flr() method
def flr(n,m):
    if(m == 0):
        print("\nCan't Divide by 'Zero'")
    else:
        result = n//m
        print(f"\nFloor Division of {n} and {m} is : {result}")
    print("________________________________________")

# power() method
def power(n,m):
    result = n**m
    print(f"\n{n} to the Power of {m} is : {result}")
    print("________________________________________")

# main function
if __name__ == "__main__":
        main()
        print("\n\t\tThanks for using..........\n")
