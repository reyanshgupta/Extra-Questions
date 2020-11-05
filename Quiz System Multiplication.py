import random
name = input("Welcome! Enter your name~~ ")
mode_choice = int(input("1. Learning Mode \n2. Testing Mode \nEnter your choice here: "))
number = int(input('Enter the number which you have chosen to take the test (between 2 to 12): '))
score = 0
def score():
    if score == 0: 
        print(name,"your score is ",score, ".Start Learning")
    elif score == 1:
        print(name,"your score is ",score, ".You need practise.")
    elif score == 2:
        print(name,"your score is ",score, ".Try Harder.")
    elif score == 3:
        print(name,"your score is ",score, ".Try more again.")
    elif score == 4:
        print(name,"your score is ",score, ".Close, try again.")
    elif score == 5:
        print(name,"your score is ",score, ".Well done")
if mode_choice == 1:
    for i in range(0,4):
        multiply = random.randint(1,12)
        print("Question: ",number,"*",multiply, ": ")
        answer1 = int(input("Answer:"))
        ok1 = number*multiply
        if answer1 == ok1:
            continue
        else: 
            for i in range(0,2):
                multiply = random.randint(1,12)
            print("Question: ",number,"*",multiply, ": ")
            answer1 = int(input("Answer:"))
            ok1 = number*multiply
            if answer1 == ok1:
                break


elif mode_choice == 2:
    for i in range(0,4):
        multiply = random.randint(1,12)
        print("Question: ",number,"*",multiply, ": ")
        answer1 = int(input("Answer:"))
        ok1 = number*multiply
        if answer1 == ok1:
            score += 1
            print("")
        else: 
            print("")
    score()    

    
else:
    print("Wrong Input")