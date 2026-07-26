'''#Keyword arguments
def demo(**p):
    for i , j in p.items():
        print(p)
        print(type(p))
        print(i , j)
demo(a=10,b=12,c=22,d=23)



def dane(name,age):
    print(f"I'm {name}, you are {age} years old")
dane('Naveen',26)
'''

#Variable arguments
# def demo(*p):
#     for i in p:
#         print(p)
#         print(type(p))
#         print(i)
# demo("a",10,"b",12,"c",22,"d",23)

#list arguments
# def demo(a):
#     for i in a:
#         pass
#         print(a)
#         print(type(a))
#         print( i )
# a=["apple", 12, "orange", 35]
# demo(a)

# def concat(fn,ln):
#     s = f"{fn} {ln}"
#     return s
# print(concat("Kalai","Selvan"))
# full_name = concat("Praveen","Kumar")
# print(full_name)
#
# def data():
#     pass

# Recursive Function

def fact(num):
    if num==0 or num==1:
        return num
    else:
        return num*(fact(num-1))
print(fact(4))


#return

def demo(x):
   return 5*x
print(demo(10))
print(demo('hi'))

# def demo(x):
#    return 5+x
# print(demo(10))
# print(demo('hi'))

#lambda

a=lambda c, d : c + d
print(a(3,20))
