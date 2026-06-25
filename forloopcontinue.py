dictionary = {'a':['antelope','aardvark'],'b':['bear','bat']}
for letter, animals in dictionary.items():
	if len(animals) > 1:
	    continue
	print(f'Only one animal{animals}')