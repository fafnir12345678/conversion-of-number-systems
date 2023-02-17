def perev10vrim(num):
    # формируем словарь из всех римских чисел и новых комбинаций
    all_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

    # на старте в римском числе ничего нет
    try:
        num=int(num)
        if num==0:
            return 'N'
    except ValueError:
        return 'можно вводить только числа'


    rim = ''
    # пока наше число больше нуля
    while num > 0:
        # перебираем все пары из словаря
        for i, r in all_roman: # i число, r буква
            # пока наше число больше или равно числу из словаря
            while num >= i:
                # добавляем соответствующую букву в римское число
                rim += r
                # вычитаем словарное число из нашего числа
                num -= i

    return rim
