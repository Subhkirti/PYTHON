import random
def give_chances(chances):
    user_name=input("Enter Your Name:-\n")
    print("Hello")
    print(user_name)
    print("Welcome To")
    print("Cows And Bulls Game")
    user=input("Are You Ready To Play\n1.Start\n2.Exit\n")
    if user=="start":
        list1=[0,1,2,3,4,5,6,7,8,9]
        list2=random.sample(list1,5)
        bull_list=[]
        cows_list=[]
        print(list2)
        print("You have",chances,"chances")
        j=0
        while j<chances:
            user_choice=int(input("Guess Any Number:-\n"))
            position=int(input("Please Enter Position:-\n"))
            i=0
            cow=0
            bull=0
            while i<len(list2):
                if user_choice in list2:
                    if i==position:
                        bull_list.insert(i,user_choice)
                        bull+=1
                        print("Bulls",bull_list)
                    
                    else:
                        cows_list.insert(i,user_choice)
                        cow+=1
                        
                        print("Cow",cows_list)
                    i+=1
            else:
                print("Your number is not exist in my secret list")
            j+=1
        if list2==bull_list:
            print("Congratulation",user_name,"You are the winner")
        else:
            print("Opps You are the looser")
            ch=int(input("how many chances you want:-"))
            give_chances(ch)
    else:
        print("You Can Move On")
give_chances()