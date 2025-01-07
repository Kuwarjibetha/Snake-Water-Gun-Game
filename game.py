import random

'''
snake 1 = water  -1
snake 1 = gun 0

water -1 = snake 1
water -1 = gun 0

gun 0  = snake 1
gun 0  = water -1

'''
computer = random.choice([1,-1,0])
compDict = {1 : "snake", -1: "water" , 0 :"gun"}

user = input("enter your choice : ")
youDict = {"snake": 1 ,"water" : -1 ,"gun": 0}

you = youDict[user]
# computer = computerDict[computer]

print(f"you are select a {compDict[you]} \n Computer select a {compDict[computer]}")

if( computer == you ):
    print("game Draw!")

else:
    if(computer == 1 and you == -1):  # 1--1 = 2
         print("you lose")
    elif(computer == 1 and you == 0): # 1- 0 = 1
        print("you win")
    elif(computer ==-1 and you == 1):  #-1 - 1 = -2
        print("you win")
    elif(computer == -1 and you == 0): #-1 - 0 = -1
        print("you lose")
    elif(computer == 0 and  you == 1): # 0-1=-1
        print("you lose")
    elif(computer ==  0 and you == -1): #0--1=1
        print("you win")
    else:
        print("Something Went Wrong")
        


# logic  when subtract all (compuer - you) are lose common outcomes is -1 and -2

# if( computer == you ):
#     print("game Draw!")
# if((computer - you) == 2 or (computer - you)== -1):
#     print("you loose")
# else:
#     print("you win")
