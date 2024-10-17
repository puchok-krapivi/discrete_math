import random

massivi = {'A': [-42, -40, -35, -26, -3, -2, 4, 9, 17, 18, 36, 37, 38, 39, 40, 44, 45, 46, 47, 48, 49, 50],
           'B': [-42, -40, -35, -28, -21, -3, 2, 4, 9, 40, 47],
           'C': [-42, -40, -35, -26, 47]}
check_1 = 0
actions = ['!', '+', '-', '&']
actions_sk = ['!', '+', '-', '&', '(', ')']
universum = [-50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31,
             -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10,
             -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
             20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46,
             47, 48, 49, 50]
alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']

while check_1 == 0:
    print('**************************************************')
    print('ВЫБОР ДЕЙСТВИЯ')
    print('1 - Создать множество')
    print('2 - Показать множества')
    print('3 - Действия с множествами')
    print('4 - Формула')
    print('5 - Выход')
    number = input()
    if number == '1':
        print('Как вы хотите создать множество?')
        print('1 - Задать вручную')
        print('2 - Рандомно')
        print('3 - По правилу')
        vvod = input()
        while vvod != '1' and vvod != '2' and vvod != '3':
            print('Нет такого варианта')
            print('Как вы хотите создать множество?')
            print('1 - Задать вручную')
            print('2 - Рандомно')
            print('3 - По правилу')
            vvod = input()
        if vvod == '1':
            print('Введите название множества')
            name = input()
            print('Введите содержимое через пробел')
            massiv = input().split(' ')
            new_massiv = []
            for elem in massiv:
                new_massiv.append(int(elem))
            massiv = new_massiv
            massiv.sort()
            massivi[name] = massiv
            print('Готово: ' + name + ' - ' + str(massivi[name]))
        elif vvod == '2':
            print('Введите название множества')
            name = input()
            print('Какой длины будет множество?')
            print('1 - Задать вручную')
            print('2 - Рандомно')
            vvod = input()
            while vvod != '1' and vvod != '2':
                print('Нет такого варианта')
                print('Как вы хотите создать множество?')
                print('1 - Задать вручную')
                print('2 - Рандомно')
                vvod = input()
            if vvod == '1':
                print('Укажите длину множества')
                vvod = int(input())
                massivi[name] = []
                while vvod < 0 or vvod > len(universum):
                    print('Длина не может быть меньше 1 и длина множества не может быть больше универсума')
                    print('Укажите длину множества')
                    vvod = int(input())
                else:
                    while len(massivi[name]) < vvod:
                        random_number = random.choice(universum)
                        if random_number not in massivi[name]:
                            massivi[name].append(random_number)
                    massivi[name].sort()
                    print('Готово: ' + name + ' - ' + str(massivi[name]))
            elif vvod == '2':
                massivi[name] = []
                random_len = random.randint(1, len(universum))
                while len(massivi[name]) < random_len:
                    random_number = random.choice(universum)
                    if random_number not in massivi[name]:
                        massivi[name].append(random_number)
                massivi[name].sort()
                print('Готово: ' + name + ' - ' + str(massivi[name]))
        elif vvod == '3':
            print('По какому правилу вы хотите задать множество?')
            print('1 - Нечетные')
            print('2 - Четные (кратные 2)')
            print('3 - Своя кратность')
            vvod = input()
            while vvod != '1' and vvod != '2' and vvod != '3':
                print('По какому правилу вы хотите задать множество?')
                print('1 - Нечетные')
                print('2 - Четные (кратные 2)')
                print('3 - Своя кратность')
                vvod = input()
            if vvod == '1':
                print('Введите название множества')
                name = input()
                massivi[name] = []
                print('Какой длины будет множество?')
                print('1 - Задать вручную')
                print('2 - Рандомно')
                vvod = input()
                while vvod != '1' and vvod != '2':
                    print('Нет такого варианта')
                    print('Как вы хотите задать длину множества?')
                    print('1 - Задать вручную')
                    print('2 - Рандомно')
                    vvod = input()
                if vvod == '1':
                    print('Укажите длину множества')
                    vvod = int(input())
                    while vvod < 0:
                        print('Длина не может ьыть меньше 1')
                        print('Как вы хотите создать множество?')
                        print('Укажите длину множества')
                        vvod = int(input())
                    while vvod > len(universum) // 2:
                        print('Желаемая длина множества больше максимальной')
                        print('Укажите длину множества')
                        vvod = int(input())
                    else:
                        while len(massivi[name]) < vvod:
                            random_number = random.choice(universum)
                            if random_number % 2 == 1:
                                if random_number not in massivi[name]:
                                    massivi[name].append(random_number)
                        massivi[name].sort()
                        print('Готово: ' + name + ' - ' + str(massivi[name]))
                elif vvod == '2':
                    massivi[name] = []
                    random_len = random.randint(1, len(universum) // 2)
                    while len(massivi[name]) < random_len:
                        random_number = random.choice(universum)
                        if random_number % 2 == 1:
                            if random_number not in massivi[name]:
                                massivi[name].append(random_number)
                    massivi[name].sort()
                    print('Готово: ' + name + ' - ' + str(massivi[name]))
            elif vvod == '2':
                print('Введите название множества')
                name = input()
                massivi[name] = []
                print('Какой длины будет множество?')
                print('1 - Задать вручную')
                print('2 - Рандомно')
                vvod = input()
                while vvod != '1' and vvod != '2':
                    print('Нет такого варианта')
                    print('Как вы хотите задать длину множества?')
                    print('1 - Задать вручную')
                    print('2 - Рандомно')
                    vvod = input()
                if vvod == '1':
                    print('Укажите длину множества')
                    vvod = int(input())
                    while vvod < 0:
                        print('Длина не может ьыть меньше 1')
                        print('Как вы хотите создать множество?')
                        print('Укажите длину множества')
                        vvod = int(input())
                    while vvod > len(universum) // 2:
                        print('Желаемая длина множества больше максимальной')
                        print('Укажите длину множества')
                        vvod = int(input())
                    else:
                        while len(massivi[name]) < vvod:
                            random_number = random.choice(universum)
                            if random_number % 2 == 0:
                                if random_number not in massivi[name]:
                                    massivi[name].append(random_number)
                        massivi[name].sort()
                        print('Готово: ' + name + ' - ' + str(massivi[name]))
                elif vvod == '2':
                    massivi[name] = []
                    random_len = random.randint(1, len(universum) // 2)
                    while len(massivi[name]) < random_len:
                        random_number = random.choice(universum)
                        if random_number % 2 == 0:
                            if random_number not in massivi[name]:
                                massivi[name].append(random_number)
                    massivi[name].sort()
                    print('Готово: ' + name + ' - ' + str(massivi[name]))
            elif vvod == '3':
                print('Введите название множества')
                name = input()
                massivi[name] = []
                print('Какому числу должны быть кратны элементы множества?')
                kratnost = int(input())
                while kratnost > 51 or kratnost < -51:
                    print('Невозможно')
                    print('Какому числу должны быть кратны элементы множества?')
                print('Какой длины будет множество?')
                print('1 - Задать вручную')
                print('2 - Рандомно')
                vvod = input()
                while vvod != '1' and vvod != '2':
                    print('Нет такого варианта')
                    print('Как вы хотите задать длину множества?')
                    print('1 - Задать вручную')
                    print('2 - Рандомно')
                    vvod = input()
                if vvod == '1':
                    print('Укажите длину множества')
                    vvod = int(input())
                    while vvod < 0:
                        print('Длина не может ьыть меньше 1')
                        print('Как вы хотите создать множество?')
                        print('Укажите длину множества')
                        vvod = int(input())
                    while vvod > len(universum) // kratnost:
                        print('Желаемая длина множества больше максимальной')
                        print('Укажите длину множества')
                        vvod = int(input())
                    else:
                        while len(massivi[name]) < vvod:
                            random_number = random.choice(universum)
                            if random_number % kratnost == 0:
                                if random_number not in massivi[name]:
                                    massivi[name].append(random_number)
                        massivi[name].sort()
                        print('Готово: ' + name + ' - ' + str(massivi[name]))
                elif vvod == '2':
                    massivi[name] = []
                    random_len = random.randint(1, len(universum) // kratnost)
                    while len(massivi[name]) < random_len:
                        random_number = random.choice(universum)
                        if random_number % kratnost == 0:
                            if random_number not in massivi[name]:
                                massivi[name].append(random_number)
                    massivi[name].sort()
                    print('Готово: ' + name + ' - ' + str(massivi[name]))
    elif number == '2':
        for elem in massivi:
            print(str(elem) + ' -  ' + str(massivi[elem]))
    elif number == '3':
        print('ВЫБОР ДЕЙСТВИЯ С МНОЖЕСТВАМИ')
        print('1 - Объединение')
        print('2 - Пересечение')
        print('3 - Разность')
        print('4 - Симметрическая разность')
        print('5 - Дополнение до универсума')
        action = input()
        if action == '1':
            print('Укажите первое множество, которое хотите объеденить')
            massiv_1 = input()
            while massiv_1 not in massivi:
                print('Нет такого множества')
                print('Укажите первое множество, которое хотите объеденить')
                massiv_1 = input()
            print('Укажите второе множество, которое хотите объеденить')
            massiv_2 = input()
            while massiv_2 not in massivi:
                print('Нет такого множества')
                print('Укажите второе множество, которое хотите объеденить')
                massiv_2 = input()
            print('Укажите третье множество, в которое нужно записать результат объединения')
            massiv_3 = input()
            massivi[massiv_3] = massivi[massiv_1].copy()
            for elem in massivi[str(massiv_2)]:
                if elem not in massivi[str(massiv_1)]:
                    massivi[massiv_3].append(elem)
                massivi[massiv_3].sort()
            print('Готово')
            print('Исходное множество ' + massiv_1 + ' - ' + str(massivi[massiv_1]))
            print('Исходное множество ' + massiv_2 + ' - ' + str(massivi[massiv_2]))
            print('Итоговое множество ' + massiv_3 + ' - ' + str(massivi[massiv_3]))
        elif action == '2':
            print('Укажите первое множество, которое хотите пересечь')
            massiv_1 = input()
            while massiv_1 not in massivi:
                print('Нет такого множества')
                print('Укажите первое множество, которое хотите пересечь')
                massiv_1 = input()
            print('Укажите второе множество, которое хотите пересечь')
            massiv_2 = input()
            while massiv_2 not in massivi:
                print('Нет такого множества')
                print('Укажите второе множество, которое хотите пересечь')
                massiv_2 = input()
            print('Укажите третье множество, в которое нужно записать результат пересечения')
            massiv_3 = input()
            massivi[massiv_3] = []
            for elem in massivi[massiv_1]:
                if elem in massivi[massiv_2]:
                    massivi[massiv_3].append(elem)
            massivi[massiv_3].sort()
            print('Готово')
            print('Исходное множество ' + massiv_1 + ' - ' + str(massivi[massiv_1]))
            print('Исходное множество ' + massiv_2 + ' - ' + str(massivi[massiv_2]))
            print('Итоговое множество ' + massiv_3 + ' - ' + str(massivi[massiv_3]))
        elif action == '3':
            print('Укажите первое множество, из которого хотите вычесеть')
            massiv_1 = input()
            while massiv_1 not in massivi:
                print('Нет такого множества')
                print('Укажите первое множество, из которого хотите вычесеть')
                massiv_1 = input()
            print('Укажите второе множество, которое хотите вычесть')
            massiv_2 = input()
            while massiv_2 not in massivi:
                print('Нет такого множества')
                print('Укажите второе множество, которое хотите вычесть')
                massiv_2 = input()
            print('Укажите третье множество, в которое нужно записать результат вычитания')
            massiv_3 = input()
            massivi[massiv_3] = []
            for elem in massivi[massiv_1]:
                if elem not in massivi[massiv_2]:
                    massivi[massiv_3].append(elem)
            massivi[massiv_3].sort()
            print('Готово')
            print('Исходное множество ' + massiv_1 + ' - ' + str(massivi[massiv_1]))
            print('Исходное множество ' + massiv_2 + ' - ' + str(massivi[massiv_2]))
            print('Итоговое множество ' + massiv_3 + ' - ' + str(massivi[massiv_3]))
        elif action == '4':
            print('Укажите первое множество')
            massiv_1 = input()
            while massiv_1 not in massivi:
                print('Нет такого множества')
                print('Укажите первое множество')
                massiv_1 = input()
            print('Укажите второе множество')
            massiv_2 = input()
            while massiv_2 not in massivi:
                print('Нет такого множества')
                print('Укажите второе множество')
                massiv_2 = input()
            print('Укажите третье множество, в которое нужно записать результат')
            massiv_3 = input()
            massivi[massiv_3] = massivi[massiv_1].copy()
            for elem in massivi[massiv_2]:
                if elem in massivi[massiv_3]:
                    massivi[massiv_3].remove(elem)
                else:
                    massivi[massiv_3].append(elem)
            massivi[massiv_3].sort()
            print('Готово')
            print('Исходное множество ' + massiv_1 + ' - ' + str(massivi[massiv_1]))
            print('Исходное множество ' + massiv_2 + ' - ' + str(massivi[massiv_2]))
            print('Итоговое множество ' + massiv_3 + ' - ' + str(massivi[massiv_3]))
        elif action == '5':
            print('Укажите множество, которое хотите дополнить до универсума')
            massiv_1 = input()
            while massiv_1 not in massivi:
                print('Нет такого множества')
                print('Укажите множество, которое хотите дополнить до универсума')
                massiv_1 = input()
            print('Укажите второе множество, в которое нужно записать результат')
            massiv_2 = input()
            massivi[massiv_2] = []
            for elem in universum:
                if elem not in massivi[massiv_1]:
                    massivi[massiv_2].append(elem)
            massivi[massiv_2].sort()
            print('Готово')
            print('Исходное множество ' + massiv_1 + ' - ' + str(massivi[massiv_1]))
            print('Итоговое множество ' + massiv_2 + ' - ' + str(massivi[massiv_2]))
        else:
            print('Нет такого варианта')
    elif number == '4':
        print('Напишите формулу')
        print('Условные обозначения:')
        print('объединение - +')
        print('разность - -')
        print('дополнение - !')
        print('симметрическая разность - &')
        print('Пример написания формулы - !A+(B-C)')
        print('Пример написания формулы - !A+B-C')
        formula = input()
        formula_mod = []
        massivi['answer'] = []
        massivi['answer_sk'] = []
        sk = 0
        while ('(' in formula and ')' not in formula) or (')' in formula and '(' not in formula):
            print('Неверно введены скобки)')
            print('Напишите формулу')
            print('Условные обозначения:')
            print('объединение - +')
            print('разность - -')
            print('дополнение - !')
            print('симметрическая разность - &')
            print('Пример написания формулы - !A+(B-C)')
            formula = input()
        if '(' in formula and ')' in formula:
            i1, i2 = 0, 0
            while i2 < len(formula) + 1:
                if formula[i1:i2] in actions_sk:
                    formula_mod.append(formula[i1:i2])
                    i1 += 1
                    i2 += 1
                elif formula[i1:i2] in massivi:
                    formula_mod.append(formula[i1:i2])
                    i1 += 1
                    i2 += 1
                else:
                    i2 += 1
            formula_mod_sk = formula_mod[formula_mod.index('(') + 1:formula_mod.index(')')]
            formula_mod = formula_mod[:formula_mod.index('(')] + formula_mod[formula_mod.index(')') + 1:]
            formula_mod.append('answer_sk')
            print('Введенная формула: ' + formula)
            i1, i2 = 0, 0
            while 1 < len(formula_mod_sk):
                if formula_mod_sk[i1] == '!':
                    massiv_1 = formula_mod_sk[i1 + 1]
                    massiv_2 = 'answer_sk'
                    for elem in universum:
                        if elem not in massivi[massiv_1]:
                            massivi[massiv_2].append(elem)
                    massivi[massiv_2].sort()
                    formula_mod_sk[i1 + 1] = massiv_2
                    formula_mod_sk.pop(i1)
                    i1 = 0
                elif formula_mod_sk[i1] == '+':
                    massiv_1 = formula_mod_sk[i1 - 1]
                    massiv_2 = formula_mod_sk[i1 + 1]
                    massiv_3 = 'answer_sk'
                    massivi[massiv_3] = massivi[massiv_1]
                    for elem in massivi[str(massiv_2)]:
                        if elem not in massivi[str(massiv_1)]:
                            massivi[massiv_3].append(elem)
                    massivi[massiv_3].sort()
                    formula_mod_sk[i1 - 1] = massiv_3
                    formula_mod_sk.pop(i1)
                    formula_mod_sk.pop(i1)
                    i1 = 0
                elif formula_mod_sk[i1] == '-':
                    massiv_1 = formula_mod_sk[i1 - 1]
                    massiv_2 = formula_mod_sk[i1 + 1]
                    massiv_3 = 'answer_sk'
                    massivi[massiv_3] = massivi[massiv_1].copy()
                    for elem in massivi[massiv_2]:
                        if elem in massivi[massiv_1]:
                            massivi[massiv_3].remove(elem)
                    massivi[massiv_3].sort()
                    formula_mod_sk[i1 - 1] = massiv_3
                    formula_mod_sk.pop(i1)
                    formula_mod_sk.pop(i1)
                    i1 = 0
                elif formula_mod_sk[i1] == '&':
                    massiv_1 = formula_mod_sk[i1 - 1]
                    massiv_2 = formula_mod_sk[i1 + 1]
                    massiv_3 = 'answer_sk'
                    massivi[massiv_3] = massivi[massiv_1].copy()
                    for elem in massivi[massiv_2]:
                        if elem in massivi[massiv_1]:
                            massivi[massiv_3].remove(elem)
                        else:
                            massivi[massiv_3].append(elem)
                    massivi[massiv_3].sort()
                    formula_mod_sk[i1] = massiv_3
                    formula_mod_sk.pop(i1)
                    formula_mod_sk.pop(i1)
                    i1 = 0
                else:
                    i1 += 1
                sk = 1
        if '(' not in formula_mod and ')' not in formula_mod:
            i1, i2 = 0, 0
            if sk != 1:
                while i2 < len(formula) + 1:
                    if formula[i1:i2] in actions:
                        formula_mod.append(formula[i1:i2])
                        i1 += 1
                        i2 += 1
                    elif formula[i1:i2] in massivi:
                        formula_mod.append(formula[i1:i2])
                        i1 += 1
                        i2 += 1
                    else:
                        i2 += 1
                print('Введенная формула: ' + formula)
            i1, i2 = 0, 0
            while 1 < len(formula_mod):
                if formula_mod[i1] == '!':
                    massiv_1 = formula_mod[i1 + 1]
                    massiv_2 = 'answer'
                    for elem in universum:
                        if elem not in massivi[massiv_1]:
                            massivi[massiv_2].append(elem)
                    massivi[massiv_2].sort()
                    formula_mod[i1 + 1] = massiv_2
                    formula_mod.pop(i1)
                    i1 = 0
                elif formula_mod[i1] == '+':
                    massiv_1 = formula_mod[i1 - 1]
                    massiv_2 = formula_mod[i1 + 1]
                    massiv_3 = 'answer'
                    massivi[massiv_3] = massivi[massiv_1]
                    for elem in massivi[str(massiv_2)]:
                        if elem not in massivi[str(massiv_1)]:
                            massivi[massiv_3].append(elem)
                    massivi[massiv_3].sort()
                    formula_mod[i1 - 1] = massiv_3
                    formula_mod.pop(i1)
                    formula_mod.pop(i1)
                    i1 = 0
                elif formula_mod[i1] == '-':
                    massiv_1 = formula_mod[i1 - 1]
                    massiv_2 = formula_mod[i1 + 1]
                    massiv_3 = 'answer'
                    massivi[massiv_3] = massivi[massiv_1].copy()
                    for elem in massivi[massiv_2]:
                        if elem in massivi[massiv_1]:
                            massivi[massiv_3].remove(elem)
                    massivi[massiv_3].sort()
                    formula_mod[i1 - 1] = massiv_3
                    formula_mod.pop(i1)
                    formula_mod.pop(i1)
                    i1 = 0
                elif formula_mod[i1] == '&':
                    massiv_1 = formula_mod[i1 - 1]
                    massiv_2 = formula_mod[i1 + 1]
                    massiv_3 = 'answer'
                    massivi[massiv_3] = massivi[massiv_1].copy()
                    for elem in massivi[massiv_2]:
                        if elem in massivi[massiv_1]:
                            massivi[massiv_3].remove(elem)
                        else:
                            massivi[massiv_3].append(elem)
                    massivi[massiv_3].sort()
                    formula_mod[i1] = massiv_3
                    formula_mod.pop(i1)
                    formula_mod.pop(i1)
                    i1 = 0
                else:
                    i1 += 1
            print('Результат выполнения: ' + str(massivi['answer']))
            massivi.pop('answer')
            massivi.pop('answer_sk')
    elif number == '5':
        check_1 = 1
        print('bb')
        break
    else:
        print('Нет такого варианта')
