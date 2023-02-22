def perevrimv10(rim):
    all_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'),
                 (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    all_romanword = ['C', 'D', 'I', 'L', 'M', 'V', 'X']

    #на старте числа нет
    rim=str(rim).upper()
    if rim =='N':
        return 0
    elif rim == '' or set(rim).issubset(all_romanword) == False:
        return 'можно вводить только римские числа'

    banword = ['VV',  'LL', 'DD', 'XXXX', 'IIII', 'CCCC', 'MMMM', 'IVI', 'IXI', 'XLX', 'XCX', 'CDC', 'CMC',
               'VIV', 'LXL', 'DCD' ]
    for i in banword:
        if i in rim:
            return 'неправельная запись римcкого числа'

    num = []

    #пока рим цифры есть
    while rim != '':
        #перебираем все пары из словаря
        for i,r in all_roman: #i число, r буква
            #пока наше число больше числа в словаре
            while rim.startswith(r): #стартвиз проверяет что рим начинается с r

                #увеличивать число
                num.append(i)
                #избавиться от вычтиной буквы
                rim=rim[len(r):]#после длины r


    # чтобы меньшее не стояло перед большем
    for i in range(len(num)-1):
        if num[i]<num[i+1]:
            return 'цифры римского числа должны идти в убывающем порядке'


    return sum(num)
                             
