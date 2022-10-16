def number_in_groups(n_customers):
    result = {} # создаем словарь чтобы записывать значения. Ключ - группа, значение - число элементов в группе
    for x in range(0, int(n_customers)):
        sum_of_digits = sum(map(int,str(x)))
        if sum_of_digits in result.keys(): # считаем сумму цифр числа и сравниваем с ключами словаря
            result[sum_of_digits] += 1  # если такое значение есть среди ключей - увеличиваем на 1 
        else:
            result[sum_of_digits] = 1 # если такого значения нет среди ключей - создаём новую запись
    return result # возвращаем словарь
