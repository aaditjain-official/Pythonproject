import math
def func_hi(name,age):
    print("Hello ! "+name+" . You are "+str(age)+".")


#func_hi("Aadit",16)
#func_hi("Kevin",27)
def square(n):
    return "The square of "+str(n)+" is "+str(n*n)

def cube1(n):
    return math.pow(n,3)


def cube2(n):
    return ("The Cube of " +str(n)+ " is " +str(n*n*n))

#print(cube1(7))
#print(cube2(3))
#print(cube2(6))
#print(cube2(9))
#print(cube2(12))

for i in range(1,101):
    print(square(i))



