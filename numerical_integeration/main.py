import func


while True:

    print('\nВыберите задачу:\n')
    print('\t1. Численное интегрирование\n'
          '\t2. Дифференциальные уравнения\n'
          '\t3. Нелинейные уравнения\n'
          '\t4. Элементарные функции\n'
          '\t5. Завершение\n')

    num = int(input('Введите цифру:'))

    if num == 1:
        while True:
            print('\nВыберите вид интеграла:\n')
            print('\t1. С постоянным шагом\n'
                  '\t2. С переменным шагом\n'
                  '\t3. Кратные интегралы\n'
                  '\t4. Назад\n')

            num = int(input('Введите цифру:'))

            if num == 1:
                while True:
                    print('\nВыберите метод:\n')
                    print('\t1. Левых частей\n'
                          '\t2. Правых частей\n'
                          '\t3. Трапеций\n'
                          '\t4. Симпсона \n'
                          '\t5. Назад\n')

                    num1 = int(input('Введите цифру:'))

                    if num1 == 1:
                        a, b, n = func.integral_value()
                        func.integral_left(a, b, n)
                    elif num1 == 2:
                        a, b, n = func.integral_value()
                        func.integral_right(a, b, n)
                    elif num1 == 3:
                        a, b, n = func.integral_value()
                        func.integral_trap(a, b, n)
                    elif num1 == 4:
                        a, b, n = func.integral_value()
                        func.integral_simp(a, b, n)
                    elif num1 == 5:
                        break
                    else:
                        print('Выберите пункт меню')

            if num == 1: continue  # Чтобы не печаталось else: print('Выберите пункт меню') в коцне цикла

            if num == 2:
                while True:
                    print('\nВыберите метод:\n')
                    print('\t1. Первый алгоритм\n'
                          '\t2. Второй алгоритм\n'
                          '\t3. Назад\n')

                    num1 = int(input('Введите цифру:'))

                    if num1 == 1:
                        a, b, e = func.integral_value_rem()
                        i = func.integral_left_rem(a, b, func.calc_remainder_term(a, b, e))
                        print(f'Интеграл равен: {round(i, func.determine_precision_digits(e))}')
                    elif num1 == 2:
                        a, b, n = func.integral_value()
                        func.double_counter(a, b, n, func.integral_value_extend())
                    elif num1 == 3:
                        break
                    else:
                        print('Выберите пункт меню')

            if num == 2: continue  # Чтобы не печаталось else: print('Выберите пункт меню') в коцне цикла

            if num == 3:
                a, b, c, d, dx, dy = func.integral_value_mult()
                func.multiple_integral(a, b, c, d, dx, dy)

            elif num == 4:
                break

            else:
                print('Выберите пункт меню')

    elif num == 2:
        print('Coming soon...')


        def diff():
            pass

    elif num == 3:
        print('Coming soon...')


        def nonlinear():
            pass

    elif num == 4:
        print('Coming soon...')


        def elementary_functions():
            pass

    elif num == 5:
        print('Завершение')
        break

    else:
        print('Выберите пункт меню')
