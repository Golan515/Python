mytuple = ('a','b','c')
print(mytuple[0])
mytuples = 1,2,3
print(mytuples[1])
def returnsmultiplevalues():
    return 1,2,3
result = returnsmultiplevalues()
print(type(result))
def returnsmultiplevalue():
    return (2,3,4)
value = returnsmultiplevalue()
print(type(value))
a,b,c = returnsmultiplevalue()
print(a)
print(b)
print(c)