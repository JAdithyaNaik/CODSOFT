#COMMAND LINE APPLICATION OF A QUIZ GAME

#Author : Jatoth Adithya Naik
#for    : Intenship (TASK-5)

# Discription :
# this command appplication simulation of a quiz game
# user has to select the correct answer for the question displayed out there
def main():
    # initial score set to 0
    score = 0
    print("\n\n\t\t\tby @JATOTH ADITHYA NAIK")
    print("\n\t\t\t *** QUIZ GAME ***\n")
    # displaying the rules of the quiz
    print('''\tRULES :\n
        1. For Every Correct Answer Score Increases by +5.
        2. For Every Wrong Answer Score Decreases By -3.
        3. For not answering score decreases by -1.
        4. Consists of 5 Questions.
        5. Min.Marks to pass 15
        ''')
    # QUESTION 1
    print(''' QUESTIONS LOADING..... >>>>>>

    I/V) What type of software enables you to communicate with the computer and acts as a coordinator between the hardware and all systems that are runnning ? 
    
        1 . Web application
        2 . Operating system
        3 . Word processor
        4 . Web browser
        ''')
    a1 = user()
    score = calculate("2",a1,score)
   
    # QUESTION 2
    print(''' 
    II/V) What type of storage does a computer use when a user enters data into an online form and before they submit the form ?
    
        1 . Long-term storage
        2 . Cookies
        3 . Short-term storage
        4 . Processing storage
        ''')
    a2 = user()
    score = calculate("3",a2,score)
   

    # QUESTION 3
    print(''' 
    III/V) A computer must translate the data it recieves from the input devices into 0's and 1's so that it can either store or process the data. What is this system of 0's and 1's called ? 
    
        1 . Binary Code
        2 . Scripting System
        3 . Long-term Storage system
        4 . Input and output system
        ''')
    a3 = user()
    score = calculate("1",a3,score)
    

    # QUESTION 4
    print(''' 
    IV/V) Thanks to advances in internet technology,web developers csn now create programs that are hybrid between a software program and a web page. What is this called ? 
    
        1 . Web sites
        2 . Web applications
        3 . Web pages
        4 . Web browsers
        ''')
    a4 =user()
    score = calculate("2",a4,score)
    

    # QUESTION 5
    print(''' 
    V/V) Which language is used to style a HTML file ? 
    
        1 . React
        2 . Java Script
        3 . Java
        4 . CSS
        ''')
    a5 = user()
    score = calculate("4",a5,score)
   


        # prints your final answer
    print("\n\t\t\t\t******* YOUR SCORE = ",score," *******")
    # prints wheather you are passed or failed
    if(score >= 15 ):
        print("\n\t\t******* CONGRATULATIONS......YOU HAVE PASSED THE TEST ********\n")
    else :
        print("\n\t\t ******* BETTER LUCK NEXT TIME......YOU HAVE FAILED THE TEST ********\n")
    print("\n****************************************************************************************************")
    # asking user for wheather he wants to play the game again
    choice = input('''\n\n\t\t  Want to play AGAIN ----> enter (YES / NO)  :  ''')
    choice = choice.lower()
    print("\n****************************************************************************************************\n")
    if(choice == "yes"):
        main()
    else:
        print("\t\tTHANKS FOR TAKING THE QUIZ\n\n")
# calculates the marks,by checking it wheather it is correct or not
def calculate(c_ans,u_ans,score):
    if(c_ans == u_ans):
        score = score+5
        print('''
        Correct answer...!!!   Score = +5
        ''')
    elif(u_ans==" "):
        score = score-1
        print('''
        You have not answered...!!!  Score = -1
        \n
        Correct answer is : ,
        ''',c_ans,)
    else:
        score= score-3
        print("\n\t\tWrong answer..!!!  Score = -3\n\n\t\tCorrect answer is :",c_ans)
    return score

# function for taking input frpom the user
def user():
    a = input("Select the Correct answer (if you want to don't answer , enter SPACE bar): ")
    return a

# main function
if __name__ =="__main__" :
    main()