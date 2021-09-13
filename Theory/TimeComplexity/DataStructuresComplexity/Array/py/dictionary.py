#dictionaries in python analog of objects in js (associate arrays)

#create
my_dict = {'a': 1, 'b': 2}

# print(my_dict['a']) ## my_dict.a е работает в питоне

#change
my_dict['a'] = 'hello'

#int keys
my_dict[5] = 'test'
my_dict['5'] = 'pest'

#print(my_dict)

#print('a' in my_dict)

#if key not exists


# print(my_dict['f']) #key error f

# print(my_dict.get('f')) #None

print(my_dict.get('f', 'No key'))
