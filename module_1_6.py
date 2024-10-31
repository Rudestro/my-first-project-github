my_dict = {'Stas': 1986, 'Marcus': 2001, 'Jack': 2019}
print(my_dict)
print(my_dict['Stas'])
print(my_dict.get('Max'))
my_dict.update({'Ben': 1864, 'Alex': 1999})
print(my_dict)
print(my_dict['Marcus'])
del my_dict['Marcus']
print(my_dict)

my_set = {1, 1, 2, 3, 3, 'a', 'b', 'b'}
print(my_set)
my_set.add('c')
my_set.add(4)
print(my_set)
my_set.remove('b')
print(my_set)