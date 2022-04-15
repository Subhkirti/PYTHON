import random
print("WELCOME TO:-COW BULL GAME")
print("THERE ARE SOME RULES FOR PLAYING:")
print("IF YOUR GUESS IS EQUAL TO THE SECRET NUMBER AND HAVE SAME POSITION, (BULL)")
print("IF YOUR GUESS HAS WRONG POSITION THEN YOU GET, (COW)")
move=str(random.randint(1000,9999))
print()
sec=input("enter four digit number:")
print(move)
i=0
while i<len(move) and len(sec):
    
    if move[i]==sec[i]:
        print("bull",end=" ")
    elif move[i]!=sec[i]:
        print("cow",end=" ")
    i+=1






      
    





    
 



  








