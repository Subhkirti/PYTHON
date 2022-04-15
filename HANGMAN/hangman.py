import random
print("WELCOME TO HANGMAN GAME")
print("YOU HAVE 10 CHANCES TO GUESS A NUMBER")
def hangman():
    words=["canada","italy","america","india","russia","france"]
    word=random.choice(words)
    chance=10
    sec=set("abcdefghijklmnopqrstuvwxyz")
    guess=" "
    while len(word)!=0:
        main=""
        for l in word:
            if l in guess:
                main=main+l
            else:
                main=main+"_ "
        if main==word:
            print(main)
            print("You win!!")
            user1=input("Do You want to play Again if YES then type 'y' otherwise 'n'")
            if user1=="y":
                print("**Good luck!**")
                hangman()
            else:
                print("Thanks for playing!!")
                break
        
        print("Word is:",main)
        g=input("Guess the character now: ")
        if g in sec:
            guess=guess+g
        else:
            print("Invalid character")
        if g not in word:
            chance=chance-1  
            print("You have only",chance,"chances!!")
            if chance==9:
                print("|")
                print("|")
                print("|")
                print("|_________")
            elif chance==8:
                print("|")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|_________")
            elif chance==7:
                print(" _______")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|_________")
            elif chance==6:
                print(" _______")
                print("|      |")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|____________")
            elif chance==5:
                print(" _______")
                print("|      |")
                print("|      0")
                print("|")
                print("|")
                print("|")
                print("|____________")
            elif chance==4:
                print(" _______")
                print("|      |")
                print("|      0")
                print("|")
                print("|")
                print("|")
                print("|____________")
            elif chance==3:
                print(" _______")
                print("|      |")
                print("|      0")
                print("|")
                print("|")
                print("|")
                print("|____________")
            elif chance==2:
                print(" _______")
                print("|      |")
                print("|      0")
                print("|     \|/")
                print("|")
                print("|")
                print("|____________")
            elif chance==1:
                print(" _______")
                print("|      |")
                print("|      0")
                print("|     \|/")
                print("|      |")
                print("|     /|")
                print("|____________")  
            elif chance==0:
                print(" _______")
                print("|      |")
                print("|      0")
                print("|     \|/")
                print("|      |")
                print("|     /|/")
                print("|____________")  
                print("you loose the game")
                print("your chances are finish")
        if chance==0:
            user=input("Do You want to play Again if YES then type 'y' otherwise 'n'")
            if user=="y":
                print("*Good luck!*")
                hangman()
            else:
                print("Thanks for playing!!")
                break
hangman()

    
