import random
NUMDIGITS = 3
MAXGUESS = 10 
numDigits = NUMDIGITS
def getSecretNum():
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = []
    for i in range(NUMDIGITS):
        secretNum.append(numbers[i])
    print(secretNum,"its a secret secretNum")
    return secretNum
def getClues( ):
    num = getSecretNum()
    print(num,"its a secretNum")
    guess = []
    index=0
    while index<len(num):
        user=int(input("guess your number="))
        guess.append(user)
        index+=1
        
    if guess == num:
        return 'You got it!'
    clue = []
    i = 0
    while i<len(guess):
        if guess[i] == num[i]:
            clue.append('Fermi')
        elif guess[i] in num:
            clue.append('Pico')
        if len(clue) == 0:
            return 'None'
        i+=1
    return ' '.join(clue)

def playAgain():
    while True:
        if play=="Yes" or play=="yes":
            getClues()
        else:
            print("you dont want ot play more ")
            break
play = input("Do you want to play again? Yes or No?")
playAgain()
