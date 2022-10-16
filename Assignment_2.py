def number_in_groups_mith_1_id(n_customers, n_first_id):
    result = {} # создаем словарь чтобы записывать значения. Ключ - группа, значение - число элементов в группе
    for x in range(int(n_first_id), int(n_customers) + int(n_first_id)): # цикл по всем значения id
        sum_of_digits = sum(map(int,str(x)))
        if sum_of_digits in result.keys(): # считаем сумму цифр числа и сравниваем с ключами словаря
            result[sum_of_digits] += 1 # если такое значение есть среди ключей - увеличиваем на 1
        else:
            result[sum_of_digits] = 1 # если такого значения нет среди ключей - создаём новую запись
    return dict(sorted(result.items())) # возвращаем отсортированный по ключам словарь 
