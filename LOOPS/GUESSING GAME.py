import random

def game():
    rand=random.randrange(9)
    sec=rand
    chance=0
    while chance<=10:
        user=int(input("enter no:"))
        if user<sec:
            print("your no is too low")
        elif user==sec:
            print("Your Guess is Right")
            break
        else:
            print("your no is too High")
        chance+=1
game()
user=input("Do you want to play Again if yes then press 'y'/'n':")
if user=="y":
    game()
