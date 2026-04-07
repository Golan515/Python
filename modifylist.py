mylist = [1,2,3,4,5]
mylist.insert(3,'a new value')
print(mylist)
mylist.remove('a new value')
print(mylist)
mylist.pop()
print(mylist)
mylist.append(6)
print(mylist)
a = [1,2,3,4,5]
b = a.copy()
a.append(6)
print(a)
print(b)