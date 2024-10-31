immutable_var = (1, 2, 'a', 'b')
print(immutable_var)
mutable_list = [1, 2, 'a', 'b']
print(mutable_list)
mutable_list[0] = 4
print(mutable_list)
print('Изменить значения элементов кортежа в Pycharm нельзя, потому что кортежи являются неизменяеми объектами, после создания которых их элементы нельзя изменить, добавить или удалить.')