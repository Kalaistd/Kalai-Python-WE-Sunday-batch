"""a = {1: "hai", 2: "hello", 3: "hi"}
b = a.copy()
print(b)

print(a.items())   # dict_items([(1, 'hai'), (2, 'hello'), (3, 'hi')])
print(a.keys())  # Print only keys   # dict_keys([1, 2, 3])

print(a.get(1))  # Get values using keys
print(a.pop(1))  # Pop the value using key
print(a.popitem())  # Delete without keys
print(a.setdefault(4, "tooooo"))  # Set default value in a
print(a.update({3: "kokila"}))  # Update the value in a
print(a)

d = {"hai", "hello", "hii"}
c = "k"
f = dict.fromkeys(c,d)
print(f)
"""

#functions

def add ():
    a=10
    b=13
    c=a+b
    print(c)
add()
add()



#without arguments
def addd():
    a= int (input('Enter the num'))
    b= int (input('Enter the num'))
    c= a + b
    print(c)
addd()#Function call
add()

#with arguments
def sub(a,b):
    c=a-b
    print(c)
sub(33,10)


#positional arguments

def mul(a,b):
    c=a*b
    print(c)
    print('result of multiplication')
mul(10,2)



#default arguments
def mul(a,b=3):
    c=a*b
    print(c)
    print("result of default")
mul(10)
mul(10,5)







    











