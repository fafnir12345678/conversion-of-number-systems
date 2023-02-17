def perevrimv10(rim):
    all_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    all_romanword = ['M', 'CM','D','CD','C','XC','L','XL', 'X','IX','V','IV','I']
    #на старте числа нет
    rim=str(rim).upper()
    if rim=='N':
        return 0
    elif rim=='' or set(rim).issubset(all_romanword)==False:
        return 'можно вводить только римские числа'
    rimlist=[]
    num=[]
    #пока рим цифры есть
    while rim !='':
        #перебираем все пары из словаря
        for i,r in all_roman: #i число, r буква
            #пока наше число больше числа в словаре
            while rim.startswith(r): #стартвиз проверяет что рим начинается с r

                #создание массива с не переведенными цифрами
                rimlist.append(r)

                #увеличивать число
                num.append(i)
                #избавиться от вычтиной буквы
                rim=rim[len(r):]#после длины r

    #чтобы не было недопустимых повторений
    for i in range(len(rimlist)):
        try:
            if (rimlist[i]=='V' or rimlist[i]=='IV' or rimlist[i]=='V' or rimlist[i]=='IX' or rimlist[i]=='XL' or \
                    rimlist[i]=='L' or rimlist[i]=='XC' or rimlist[i]=='CD' or rimlist[i]=='D' or rimlist[i]=='CM') and rimlist[i]==rimlist[i+1]:
                        return 'римские цифры не кратные 10 не могут повторятся '
        except IndexError:
            None

        try:
            if len(rimlist)>=4:
                    if (rimlist[i] == 'X' or rimlist[i] == 'I' or rimlist[i] == 'C' or rimlist[i] == 'M') and \
                        rimlist[i]==rimlist[i+1]==rimlist[i+2]==rimlist[i+3]:
                            return 'римские цифры равные 1 или кратные 10 не могут повтрятся больше 3 раз'
        except IndexError:
            None


    # чтобы меньшее не стояло перед большем
    for i in range(len(num)-1):
        if num[i]<num[i+1]:
            return 'цифры римского числа должны идти в убывающем порядке'


    return(sum(num))
                             
