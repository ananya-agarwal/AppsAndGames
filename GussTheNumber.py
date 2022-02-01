'''
Q. Develop a guessing game which would ask the user to guess a number between a given range say 0 to 60. 
    Let the function choose a number between 0 and 60 say 25
    and tell the user if his/her guess was right or above or below.
    Constarint is that he gets only numbered chances say 15 and
    then display the number of turns taken by the user to guess the number. 
'''
chances = 15
number = 25
i = 1
print("Hey user!! Take a guess between a number from 0 to 60. ")
while i <= chances:
    user = int(input())
    if user > 60 or user < 0:
        print("The number should be between 0 and 60!!")
        i+=1
    else:
        if user > number:
            print("Try a number BELOW")
            i+=1
        elif user < number:
            print("Try a number ABOVE")
            i+=1
        else:
            print("You found it!!")
            print("It took you",i,"chances")
            exit()