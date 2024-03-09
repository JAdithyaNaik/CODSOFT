#COMMAND LINE APPLICATION TO GENERATE RANDOM PASSWORD

#Author : Jatoth Adithya Naik
#for    : Intenship (TASK-3)

# Discription :
# this command appplication generates random password
# user has to give length of the password as input

import random
import string
password = ""
def main():
    
    print("\n\n\t\t\tby @JATOTH ADITHYA NAIK")
    print("________________________________________")
    print("\n\t\t\t***RANDOM PASSWORD GENERATOR APP***\n")
    username = input("\tEnter the user name : ")
    length = inp()
    while True:
        if length.isdigit():
            if length == "0":
                print("\n\t\tInvalid size\n")
                exit()
            gen(length,password)
            # exit()
        else:
            print("\n\t\tInvalid size\n")
            exit()
        choice = rep()
        if(choice == "1"):
            break
        elif(choice == "2"):
            gen(length,password)
            rep()
        elif(choice == "3"):
            print("\n\t\tTHANKS FOR USING....\n")
            exit()
        else:
            print("\n\tInvalid choice\n")
            break

    print("\n\t\tTHANKS FOR USING....\n")

def gen(length,password):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    for i in range(int(length)):
        password+=random.choice(all_chars)
    print("\n\tGenerated password : " ,password+"\n")



def inp():
    return input("\n\tEnter the length of the password : ")



def rep():
    print("""\t1.ACCEPT
\t2.REGENERATE
\t3.EXIT""")
    return input("\n\tEnter your choice : ")



if __name__ == "__main__":
    main()
