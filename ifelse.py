for n in range(1,101):
    if n % 15 == 0:
        print('FizzBuzz')
    else:
        if n % 3 == 0:
            print('Fizz')
        else:
            if n % 5 == 0:
                print('Buzz')
            else:
                print(n)
for i in range(1,101):
    if i % 15 == 0:
        print('fizzbuz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
a = 5
print('fizz' if a % 3 == 0 else a)
fizzbuzz = 'fizzy' if a % 3 == 0 else a
print(fizzbuzz)
'fizz' if a % 3 == 0 else 'Buzz' if n % 5 == 0 else n
'FizzBuzz' if n % 15 == 0 else 'Fizz' if n % 3 == 0 else 'Buzz' if n % 5 == 0 else n
['FizzBuzz' if n % 15 == 0 else 'Fizz' if n % 3 == 0 else 'Buzz' if n % 5 == 0 else n for n in range(1,101)]