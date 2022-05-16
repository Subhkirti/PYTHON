import json,os
print("---*WELCOME TO LOGIN/SIGNUP--- For new account press Signup and For already existing account press Login*---")
print("Press 1 to Login:")
print("Press 2 to Signup:")
user=int(input("Press the Button:"))
dic2={}
l=[]
d={}
if user==1:
    name=input("Enter username:")
    password =input("Enter your password:")
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
            print("Please use  atleast one capital letter, Smalll letter, Digit and Special character!! ")
        else:
            if os.path.exists("User.json"):
                with open('User.json','r') as file2:
                    f=file2.read()
                    data=json.loads(f)
                    both=0
                    passw=0
                    u=0
                    info=""
                    for i in data["User"]:
                        for j in i:
                            if name==i["Username"] and password==i["Password"]:
                                both=1
                                info=i
                            elif name!=i["Username"]:
                                u=1
                            elif name==i["Username"] and password!=i["Password"]:
                                passw=1
                    if both==1:
                        print("----*Your Details*----")
                        for k in info:
                            print("   ",k,":--",info[k])
                        print("----*You are Login Successfully!!*-----")
                    elif passw==1:
                        print("You're password is incorrect!!!")
                    elif u==1:
                        print("You're not existing here!!")
            else:
                print("You have not any account!! So, please make an new account..")   
    else:
        print("Password is too short!")   
elif user==2:
    if os.path.exists("User.json"):
        pass
    else:
        f=open("User.json","w+")
        f.close()
    name1=input("Enter your name:")
    passw=input("Enter your Password:(password should contain uppercase, lowercase, digit, special characters!)")
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
            try:
                d['Username']=name1
                d["Password"]=passw
                d['Hobbies']=hobby
                d["Gender"]=Gender
                d["Designation"]=Designation
                d["Date of Birth"]=Birth
                l.append(d)
                dic2["User"]=l
                with open("User.json","r+") as file:
                    read_file= file.read()
                    userdata=json.loads(read_file)
                    for i in userdata:
                        if i =="User":
                            a=userdata[i]
                            a.append(d.copy())
                            dic2["User"]=a
                            json.dumps(dic2,file)
                            file.close()
            except:
                with open("User.json","w") as f:
                    f.write(json.dumps(dic2, indent=4))
                    print("----You are Signup Successfully!!----")
        else:
            print("Please use  atleast one capital letter , Smalll letter, Digit and Special character!! ")
    else:
        print("Password is too short!")
else:
    print("Please press valid button either 1 or 2!!")

