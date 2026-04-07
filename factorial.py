def factorial(i):
    if type(i) != int:
        return None 
    if i < 0:
        return None
    if i == 0:
        return 1;       
    return i * factorial(i-1)
num = int(input("Enter a number: "))
print(factorial(num))