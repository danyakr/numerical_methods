import func


while True:

    print('\nВыберите задачу:\n')
    print('\t1. Численное интегрирование\n'
          '\t2. Дифференциальные уравнения\n'
          '\t3. Нелинейные уравнения\n'
          '\t4. Элементарные функции\n'
          '\t5. Завершение\n')

    num = int(input('Введите цифру: '))

    if num == 1:
        while True:
            print('\nВыберите вид интеграла:\n')
            print('\t1. С постоянным шагом\n'
                  '\t2. С переменным шагом\n'
                  '\t3. Кратные интегралы\n'
                  '\t4. Назад\n')

            num = int(input('Введите цифру: '))

            if num == 1:
                while True:
                    print('\nВыберите метод:\n')
                    print('\t1. Левых частей\n'
                          '\t2. Правых частей\n'
                          '\t3. Трапеций\n'
                          '\t4. Симпсона \n'
                          '\t5. Назад\n')

                    num1 = int(input('Введите цифру: '))

                    if num1 == 1:
                        func.integral_left()
                    elif num1 == 2:
                        func.integral_right()
                    elif num1 == 3:
                        func.integral_trap()
                    elif num1 == 4:
                        func.integral_simp()
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

                    num1 = int(input('Введите цифру: '))

                    if num1 == 1:
                        func.integral_left_rem()
                    elif num1 == 2:
                        func.double_counter()
                    elif num1 == 3:
                        break
                    else:
                        print('Выберите пункт меню')

            if num == 2: continue  # Чтобы не печаталось else: print('Выберите пункт меню') в коцне цикла

            if num == 3:
                func.multiple_integral()

            elif num == 4:
                break

            else:
                print('Выберите пункт меню')

    elif num == 2:
        while True:
            print('\nВыберите метод:\n')
            print('\t1. Метод Эйлера\n'
                  '\t2. Метод Рунге-Кутта\n'
                  '\t3. Метод Эйлера для уравнений второго порядка\n'
                  '\t4. Метод Рунге-Кутта для уравнений второго порядка\n'
                  '\t5. Системы дифференциальных уравнений\n'
                  '\t6. Назад\n')

            num = int(input('Введите цифру: '))

            if num == 1:
                func.eulers_method()
            elif num == 2:
                func.runge_kutta_method()
            elif num == 3:
                func.eulers_method2()
            elif num == 4:
                func.runge_kutta_method2()
            elif num == 5:
                func.system_of_differential_equations()
            elif num == 6:
                break
            else:
                print('Выберите пункт меню')

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
