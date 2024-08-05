immutable_var = True, ['software', 3.14], 295, 'Hi'
print(immutable_var)
# immutable_var[0] = False - нельзя изменять элементы кортежа, так как кортеж является неизменяемым объектом.
immutable_var[1][0] = 'soft' # - изменяемые объекты внутри кортежа изменять можно
print(immutable_var)
mutable_list = [495, 'yes', True, 9.3]
mutable_list[0] = int(mutable_list[-1] - 0.3)
print(mutable_list)