immutable_var = 1, '2', [3, 4]
print(immutable_var)
# immutable_var[0] = 4
# выдает ошибку т. к. кортеж не поддерживает назначение элементов
mutable_list = ['Арбуз', 2, True]
mutable_list[0] = 'Апельсин'
mutable_list[1] = 7
mutable_list[2] = False
print(mutable_list)
