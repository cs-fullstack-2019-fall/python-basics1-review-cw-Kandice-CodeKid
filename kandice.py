# ### Problem 1:
# Create a program that prints the user input until they enter 'q' to quit.
# 
userInput = input("Enter something")
while (userInput != 'q'):
    print(userInput)
    userInput = input("Enter something")
print(userInput)

#Per Kenn ignore #2





# ### Problem 3:
# Create a program that takes user input in a while loop. If they enter 1, print 1. If they enter 2, print 2. If they enter 3 print 3. If they enter ‘q’ or 0 (your choice), quit. Else, print “ERROR”.
# 
doeInput =input("enter a number or press q or zero to quit")
while (doeInput != 'q' or doeInput != '0'):
    # you while loop is broken but works without your second condition
    if doeInput=="1":
        print(doeInput)
        doeInput =input("enter a number or press q or zero to quit")
    elif doeInput=='2':
        print("2")
        doeInput =input("enter a number or press q or zero to quit")
    elif doeInput =='3':
        print('3')
        doeInput =input("enter a number or press q or zero to quit")
    else:
        print('ERROR')
        doeInput =input("enter a number or press q or zero to quit")

# ### Problem 4:
# Create a program that takes the user input until they enter 'q'. You should store all of their input and separate the input with a comma. Once they enter 'q', print all of the comma separated words they entered.

userInfo = input('enter info or press q to quit     ')
moreUserInfo =""
while userInfo!= 'q':
        moreUserInfo = moreUserInfo + ","+ userInfo
        userInfo = input('enter info or press q to quit   ')
print(moreUserInfo)