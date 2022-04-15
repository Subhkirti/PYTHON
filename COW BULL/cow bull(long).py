import random
print("WELCOME TO:-COW BULL GAME")
print("THERE ARE SOME RULES FOR PLAYING:")
print("IF YOUR GUESS IS EQUAL TO THE SECRET NUMBER AND HAVE SAME POSITION, (BULL)")
print("IF YOUR GUESS HAS WRONG POSITION THEN YOU GET, (COW)")
def cow_bull():
    move=[1,2,3,4,5,6,7,8,9]
    sec=random.sample(move,5)
    print(sec)
    cow=[]
    bull=[]
    i=1
    print("You have 10 Chances!!!Good Luck!")
    while i<=10:
        if sec==bull:
            print("*Congrats! You are the Winner!!*")
            break
        user=int(input("Enter Your no from 0 to 9:"))
        position=int(input("Enter the position:"))
        if user not in sec:
            print("your number is not exist in the list")
        else:
            if user in sec and sec.index(user)==position:
                bull.insert(position,user)
                print("***Bull**",bull)
            
            elif sec.index(user)!=position:
                cow.insert(position,user)
                print("***Cow**",cow)
                
        i+=1 
cow_bull()
user2=input("Do you want to play again(y/n):")
if user2=="y":
    cow_bull()
else:
    print("Ok! Thanks for playing my Game!!")



              
                   
        
        
                   




        

