from tkinter import Y


game_is_on = True
while game_is_on:

  
        print("welcome to the quiz game")

        answer = input("are you ready to play yes or no ").lower()
        score = 0
        if answer != "yes":
            quit()

        answer = input("what color is the sky ")

        if answer == "blue":
            print("correct")
            score += 1
        else:
            print("wrong")

        answer = input("waht is 2 + 2 =  ")

        if int(answer) == 4:
            print("correct")
            score += 1
        else:
            print("wrong")

        answer = input("how many fingers on a human hand ")

        if int(answer) == 5:
            print("correct")
            score += 1
        else:
            print("wrong")

        answer = input("What’s the hardest rock? ")

        if answer == "diamond":
            print("correct")
            score += 1
        else:
            print("wrong")

        print(f"great you have finished the quiz your score is {score} out of 4 questions")
        game = input("do you want to reset the game yes or no ")

        if game == "no":
            game_is_on = False
       
