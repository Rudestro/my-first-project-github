def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params() # Без аргументов
print_params(b = 25) # b
print_params(c = [1, 2, 3]) # c
values_list = ['строка', True, 42]  # Разные типы
values_dict = {'a': 10, 'b': 'текст', 'c': False}  # Разные типы значений
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)