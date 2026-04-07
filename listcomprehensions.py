mylist = [1,2,3,4,5]
print([2*item for item in mylist])
print(mylist)
mylist = list(range(100))
filteredlist = [item for item in mylist if item % 10 ==0]
print(filteredlist)
mystring = 'My name is Narayan. I live in LA'
print(mystring.split('.'))
print(mystring.split())
def cleanword(word):
    return word.replace('.','').lower()
print([cleanword(word) for word in mystring.split()])
print([cleanword(word) for word in mystring.split() if len(cleanword(word)) < 3])
print([[cleanword(word) for word in sentence.split()] for sentence in mystring.split('.')])