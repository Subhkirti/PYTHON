password=input("enter your Password:")
if len(password)>6 and len(password)<=16 and "$" in password and "2"in password and "8" in password and "A" in password and "Z" in password:
    print("strong password!")
else:
    print("Weak password!")
 