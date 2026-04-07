from collections import defaultdict
animals = {'a':'antelope','b':'bat','c':'cat'}
print(animals)
print(animals['a'])
animals['d'] = 'dog'
print(animals)
animals['a'] = 'alligator'
print(animals)
print(animals.keys())
print(animals.values())
list(animals.keys())
animals.get('e','elephant')
print(animals.get('e','elephant'))
print(animals['a'])
print(len(animals))
animals = {'a':['aardvark','antelope'],'b':['bear']}
animals['b'].append('bison')
animals['c'] = ['cat']
if 'c' not in animals:
    animals['c'] = []
animals['c'].append('cat')
print(animals)
animals = defaultdict(list)
print(animals)
animals['e'].append('elephant')
print(animals)
animals['e'].append('emu')
print(animals)