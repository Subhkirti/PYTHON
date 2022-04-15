ch=input("enter a character:")
if ch>="a" and ch<="z" or ch>="A" and ch<="Z":
    print("Character is a alphabet!")
elif ch>="0" and ch<="9":
    print("Character is a digit!")
else:
    print("Character is a special character!")