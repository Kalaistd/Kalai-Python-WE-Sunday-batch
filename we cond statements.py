"""
# simple if condition

a=10
if a==10:
    print(a)

a=10
if a==11:
    print(a)


a=int(input("Enter an number:"))
if a==22:
    print("a is even")



#if else

a=10
b=20
if a<b:
    print("correct")                       
else:
    print("wrong")



a=10
b=20
if a>b:
    print("correct")                       
else:
    print("wrong")



x=int(input("Enter a number X:"))
y=int(input("Enter a number Y:"))
if x<y:
    print("Y is greater than")
else:
    print("X is greater than")



x = str(input("Enter a Vowels:"))
if (x=="a" or x=="e" or x=="i" or x=="o" or x=="u"):
    print("Entered text is a vowel")
else:
    print("Entered text is not a vowel")
    



# elif

x=int(input("Enter a mark:"))

if x>80 and x<100:
    print("A Grade")
elif x>50 and x<79:
    print("B Grade")
elif x>40 and x<49:
    print("C Grade")
else:
    print("Fail")

"""

#nested if


x1=int(input("Enter a mark1:"))

if x1>80:
    print("you are eligible for test 2")
    x2=int(input("Enter a mark2:"))
    if x2>90:
        print("you are eligible for CV")
        x3=str(input("Say yes or no:"))
        if x3=="yes":
            print("You are Selected")
        else:
            print("Not Selected")
    else:
        print("you are Not eligible for CV")
else:
    print("you are Not eligible for test 2")
    
            

#==================


x1=int(input("Enter a mark1:"))
x2=int(input("Enter a mark2:"))
x3=str(input("Say yes or no:"))

if x1>80:
    print("you are eligible for test 2")
    if x2>90:
        print("you are eligible for CV")
        if x3=="yes":
            print("You are Selected")
        else:
            print("Not Selected")
    else:
        print("you are Not eligible for CV")
else:
    print("you are Not eligible for test 2")


    
    






    































