#COMMAND LINE APPLICATION TO GENERATE RANDOM PASSWORD

#Author : Jatoth Adithya Naik
#for    : Intenship (TASK-3)

# Discription :
# this command appplication generates random password
# user has to give length of the password as input
import random
import string

def main():
    print("\n\n\t\t\tby @JATOTH ADITHYA NAIK")
    print("________________________________________")
    print("\n\t\t\t***RANDOM PASSWORD GENERATOR APP***\n")
    username = input("\tEnter the user name : ")
    length = input("\n\tEnter the length of the password : ")
    while True:
        password = ""
        if length.isdigit():
            if length == "0":
                print("\n\t\tInvalid size\n")
                exit()
            else:
                gen(length,password)
                break
        else:
            print("\n\t\tInvalid size\n")
            exit()


    while True:
        choice = rep()
        match choice:
            case "1" :
                print("\n\t\tTHANKS FOR USING....\n")
                exit()
            case "2" :
                gen(length,password)
            case "3" :
                print("\n\t\tTHANKS FOR USING....\n")
                exit()
            case _ :
                print("\n\tInvalid choice\n")
                break

    print("\n\t\tTHANKS FOR USING....\n")

def gen(length,password):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    for i in range(int(length)):
        password+=random.choice(all_chars)
    print("\n\tGenerated password : " ,password+"\n")
    

def rep():
    print("""\t1.ACCEPT\n\t2.REGENERATE\n\t3.EXIT""")
    return input("\n\tEnter your choice : ")


main()