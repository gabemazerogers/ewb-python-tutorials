'''
Hello! What is your name?
Albert
Well, Albert, I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too high.
Take a guess.
2
Your guess is too low.
Take a guess.
4
Good job, Albert! You guessed my number in 3 guesses!
'''


import random

def mean(list):
    sum = 0
    for number in list:
        sum = sum + number
    print sum / len(list)

def mode(list):
    highest_count = 0
    for number in list:
        if(highest_count <= list.count(number)):
            highest_count = number
    print highest_count




def median(list):
    sort = list.sort()
    if((len(list) % 2) == 1):
        midpoint = len(list)/2
        print list[midpoint]
    else:
        print (list[len(list)/2] + list[len(list)/2 - 1])/2.0

median([1,2,3,4])








def guess_a_number():
    user = raw_input("Hello! What is your name?")
    print user

    number = random.randint(1,20)

    tally = 0
    user_guess_correct = False
    while(user_guess_correct == False):
        tally = tally + 1
        user_guess = input("Take a guess. :")

        if(number > user_guess):
            print "Too low."

        elif(number < user_guess):
            print "Too high"

        else:
            print "Good job ", user , " You guessed my number in ", tally, " attempts!"
            user_guess_correct = True
