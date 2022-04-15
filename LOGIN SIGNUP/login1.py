import json
print("WELCOME TO LOGIN/SIGNUP")
print("Press 1 to Login:")
print("Press 2 to Signup:")
user=int(input("Press the Button:"))
# Login
if user==1:
    l=[]
    name1=input("Enter your name:")
    passw=input("Enter your Password:(password should contain uppercase, lowercase,digit,special characters!)")
    upper,lower,digit,special=0,0,0,0
    if len(passw)>=6:
        for i in passw:
            if (i.isupper()):
                upper=1
            if (i.isdigit()):
                digit=1
            if (i.islower()):
                lower=1
            if(i=='@'or i=='$' or i=='_' or i=='#' or i=="!" or i=="%" or i=="^" or i=="&" or i=="*" or i=="(" or i==")"):
                special=1
        total=upper+digit+lower+special  
        if total==4:
            hobby=input("Enter your Hobbies:")
            Designation=input("Enter your Designation:")
            Birth=input("enter your Date of Birth:")
            Gender=input("Enter your Gender:")
            d={}
            d['Username']=name1
            d["Password"]=passw
            d['Hobbies']=hobby
            d["Gender"]=Gender
            d["Designation"]=Designation
            d["Date of Birth"]=Birth
            l.append(d)
            with open("Kirti.json","a") as file:
                
                json.dump(l,file,indent=4)
            print("----You are Login Successfully!!----")
        else:
            print("Please use  atleast one capital letter , Smalll letter, Digit and Special character!! ")
    else:
        print("Password is too short!")
      
# Signup
elif user==2:
    name=input("Enter username:")
    password =input("Enter strong password:")
    
    upper,lower,digit,special=0,0,0,0
    if len(password)>=6:
        for i in password:
            if (i.isupper()):
                upper=1
            if (i.isdigit()):
                digit=1
            if (i.islower()):
                lower=1
            if(i=='@'or i=='$' or i=='_' or i=='#' or i=="!" or i=="%" or i=="^" or i=="&" or i=="*" or i=="(" or i==")"):
                special=1
        total=upper+digit+lower+special 
        if total!=4:
            print("Please use  atleast one capital letter , Smalll letter, Digit and Special character!! ")
        else:
            password2=input("Conform Password:")
            if password!=password2:
                print("Please enter correct pasword!")
            else:
                hobby=input("Enter your Hobbies:")
                Designation=input("Enter your Designation:")
                Birth=input("enter your Date of Birth:")
                Gender=input("Enter your Gender:")
        
                d={}
                d['Username']=name
                d["Password"]=password
                d['Hobbies']=hobby
                d["Gender"]=Gender
                d["Designation"]=Designation
                d["Date of Birth"]=Birth
                k=json.dumps(d,indent=1)
                f1=open("kirti.json","a")
                f1.writelines(k)
                f1.close()
                
                print("***Congrats",name,"You are signed up successfully***")
    else:
        print("Password is too short!")   

