x = lambda a , b: a * b
print (x(5,6))


# using a function.

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#using same function to make triple 

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytriple = myfunc(3)

print(mydoubler(11))
print(mytriple(11))