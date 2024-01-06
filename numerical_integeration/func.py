from math import sin, ceil, sqrt, log10, pi, cos

import matplotlib.pyplot as plt
import numpy as np


def integral_value():
    """ Функция запрашивает у пользователя нижний и верхний предел интегрирования
    и количество разбиений

    """
    a = float(input('Введите нижний предел интегрирования:'))
    b = float(input('Введите верхний предел интегрирования:'))
    n = int(input('Введите количество разбиений:'))
    return a, b, n


def integral_value_rem():
    """ Функция запрашивает у пользователя нижний и верхний предел интегрирования
    и точность вычислений

    """
    a = float(input('Введите нижний предел интегрирования:'))
    b = float(input('Введите верхний предел интегрирования:'))
    e = float(input('Введите точность вычислений: '))
    return a, b, e


def integral_value_extend():
    """ Функция запрашивает у пользователя точность вычислений """

    e = float(input('Введите точность вычислений:'))
    return e


def integral_left():
    """ Функция вычисляет приближенное значение определенного интеграла
    методом прямоугольников левых частей

    Для примера берется подынтегральная функция вида: cos(x ** 2 + 0.6) / (1.2 + sin(0.7 * x + 0.2))
    """
    a, b, n = integral_value()
    h = (b - a) / n

    x = a
    s = 0
    while x <= (b - h):
        s = s + (cos(x ** 2 + 0.6) / (1.2 + sin(0.7 * x + 0.2)))
        x = x + h

    print(f'\nИнтеграл равен: {h * s}')


def integral_right():
    """ Функция вычисляет приближенное значение определенного интеграла
    методом прямоугольников правых частей

    Для примера берется подынтегральная функция вида: cos(x ** 2 + 0.6) / (1.2 + sin(0.7 * x + 0.2))
    """
    a, b, n = integral_value()
    h = (b - a) / n

    x = a + h
    s = 0
    while x <= b:
        s = s + (cos(x ** 2 + 0.6) / (1.2 + sin(0.7 * x + 0.2)))
        x = x + h

    print(f'\nИнтеграл равен: {h * s}')


def integral_trap():
    """ Функция вычисляет приближенное значение определенного интеграла
    методом трапеций

    Для примера берется подынтегральная функция вида: cos(x ** 2 + 0.6) / (1.2 + sin(0.7 * x + 0.2))
    """
    a, b, n = integral_value()
    h = (b - a) / n

    f0 = cos(a ** 2 + 0.6) / (1.2 + sin(0.7 * a + 0.2))
    fn = cos(b ** 2 + 0.6) / (1.2 + sin(0.7 * b + 0.2))

    x = a + h
    s = 0
    while x <= (b - h):
        s = s + (cos(x ** 2 + 0.6) / (1.2 + sin(0.7 * x + 0.2)))
        x = x + h

    print(f'\nИнтеграл равен: {h * ((f0 + fn) / 2 + s)}')


def integral_simp():
    """ Функция вычисляет приближенное значение определенного интеграла
    методом парабол(Симпсона)

    Для примера берется подынтегральная функция вида: cos(x ** 2 + 0.6) / (1.2 + sin(0.7 * x + 0.2))
    """
    a, b, n = integral_value()
    h = (b - a) / n
    f0 = cos(a ** 2 + 0.6) / (1.2 + sin(0.7 * a + 0.2))
    fn = cos(b ** 2 + 0.6) / (1.2 + sin(0.7 * b + 0.2))

    x = a + h
    s1 = 0
    while x <= (b - h):
        s1 = s1 + (cos(x ** 2 + 0.6) / (1.2 + sin(0.7 * x + 0.2)))
        x = x + 2 * h

    x = a + 2 * h
    s2 = 0
    while x <= (b - 2 * h):
        s2 = s2 + (cos(x ** 2 + 0.6) / (1.2 + sin(0.7 * x + 0.2)))
        x = x + 2 * h

    print(f'\nИнтеграл равен: {(h / 3) * ((f0 + fn) + 2 * s2 + 4 * s1)}')


def integral_left_rem():
    """ Функция вычисляет приближенное значение определенного интеграла
    методом прямоугольников левых частей

    Функция используется в связке с calc_remainder_term(),
    где максимум производной взят для 1 / sqrt(x + 2) с пределами 2 и 7

    Для примера берется подынтегральная функция вида: 1 / sqrt(x + 2)
    """
    a, b, e = integral_value_rem()
    n = calc_remainder_term(a, b, e)
    h = (b - a) / n

    x = a
    s = 0
    while x <= (b - h):
        s = s + (1 / sqrt(x + 2))
        x = x + h

    print(f'Интеграл равен: {round(h * s, determine_precision_digits(e))}')


def calc_remainder_term(a, b, e):
    """ Функция вычисляет остаточный член

    Остаточный член вычисляется для дальнейщего использования в
    методе прямоугольников левых частей.

    В примере рассматривается подынтегральная функция 1 / sqrt(x + 2)
    """
    while True:
        ch = input('1. Ввести модуль максимума прозводной подынтегральной функции (m)\n'
                   '2. Пример работы для  a = 2, b = 7, e = 0.1, m = 0.0625 (нажмите 1 или 2)? ')
        if ch == '1':
            m = float(input('Введите модуль максимума прозводной подынтегральной функции: '))
            break
        elif ch == '2':
            a = 2
            b = 7
            e = 0.1
            m = 1 / 16
            break
        else:
            print('Выберите 1 или 2')
            continue

    n = ceil((b - a) ** 2 / (2 * e) * m)
    return n


def determine_precision_digits(e):
    """Функция вычисляет количество значащих цифр исходя из заданной точности"""

    precision = 0
    while e < 1:
        e *= 10
        precision += 1

    return precision


def integral_left_h(a, b, h):
    """Функция вычисления интеграла методом левых частей

    Передается шаг в отличие от функции integral_left для использования в функции
    double_counter с переменным шагом.

    Функция принимает верхний и нижний пределы интегрирования
    и шаг, который меняется в алгоритме двойного пересчета
    """
    x = a
    s = 0

    while x <= b - h:
        s += cos(x ** 2 + 0.6) / (1.2 + sin(0.7 * x + 0.2))
        x += h

    return h * s


def double_counter():
    """Функция вычисляет приближенное значение определенного интеграла методом двойного пересчета"""
    a, b, n = integral_value()
    precision = integral_value_extend()

    e = precision
    h = (b - a) / n
    in_value = 0
    i2n = integral_left_h(a, b, h)
    r = abs(i2n - in_value)
    in_value = i2n
    h /= 2

    while r > e:
        i2n = integral_left_h(a, b, h)
        r = abs(i2n - in_value)
        in_value = i2n
        h /= 2

    print(f'\nИнтеграл равен: {round(i2n, determine_precision_digits(e))}')
    print(f'Шаг равен: {h * 2}')


def integral_value_mult():
    """ Функция запрашивает у пользователя нижний и верхний предел интегрирования
    и шаг интегрирования по оси x и y

    """
    a = float(input("Введите нижний предел интегрирования по оси x: "))
    b = float(input("Введите верхний предел интегрирования по оси x: "))
    c = float(input("Введите нижний предел интегрирования по оси y: "))
    d = float(input("Введите верхний предел интегрирования по оси y: "))
    dx = float(input("Введите шаг интегрирования по оси x: "))
    dy = float(input("Введите шаг интегрирования по оси y: "))

    return a, b, c, d, dx, dy


def multiple_integral():
    """Функция вычисляет приближенное значение кратных интегралов"""
    a, b, c, d, dx, dy = integral_value_mult()

    integral_sum = 0.0
    x = a
    while x < b:
        y = c
        while y < d:
            integral_sum += (x ** 2 + y ** 2) * dx * dy
            y += dy
        x += dx
    print(f'\nИнтеграл равен: {integral_sum}')


# functions for solving differential equations


def eulers_method():
    """
    Функция реализующая метод Эйлера для уравнения y’ = y*(1 - x) на отрезке [0; 1] с
    начальными условиями x0= 0, y0= 1 и осуществляющая вывод графика.
    """

    # Определим функцию, представляющую данное дифференциальное уравнение
    def f(x, y):
        return y * (1 - x)

    # Начальные условия и параметры
    x0, y0 = 0, 1
    xf = 1
    n = 10  # количество разбиений
    h = (xf - x0) / n

    # Массивы для хранения значений
    x_values = [x0]
    y_values = [y0]

    # Метод Эйлера
    for i in range(n):
        y0 = y0 + h * f(x0, y0)
        x0 = x0 + h
        x_values.append(x0)
        y_values.append(y0)

    # Вывод в виде таблицы
    print(" x        y ")
    print("------------")
    for i in range(n + 1):
        print(f"{x_values[i]:.2f}    {y_values[i]:.2f}")

    # Визуализация результатов
    plt.plot(x_values, y_values, 'b', label='Solution')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Решение y\' = y*(1 - x) используя метод Эйлера')
    plt.legend()
    plt.show()


def runge_kutta_method():
    """
    Функция реализующая метод Рунге-Кутта для уравнения y’ = y*(1 - x) на отрезке [0; 1] с
    начальными условиями x0= 0, y0= 1 и осуществляющая вывод графика.
    """

    # Определим функцию, представляющую данное дифференциальное уравнение
    def f(x, y):
        return y * (1 - x)

    # Начальные условия и параметры
    x0, y0 = 0, 1
    xf = 1
    n = 10  # количество шагов
    h = (xf - x0) / n

    # Массивы для хранения значений
    x_values = [x0]
    y_values = [y0]

    # Метод Рунге-Кутта
    for i in range(n):
        k1 = h * f(x_values[-1], y_values[-1])
        k2 = h * f(x_values[-1] + 0.5 * h, y_values[-1] + 0.5 * k1)
        k3 = h * f(x_values[-1] + 0.5 * h, y_values[-1] + 0.5 * k2)
        k4 = h * f(x_values[-1] + h, y_values[-1] + k3)

        x_values.append(x_values[-1] + h)
        y_values.append(y_values[-1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6)

    # Вывод в виде таблицы
    print(" x        y ")
    print("------------")
    for i in range(n + 1):
        print(f"{x_values[i]:.2f}    {y_values[i]:.2f}")

    # Визуализация результатов
    plt.plot(x_values, y_values, 'b', label='Solution')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Решение y\' = y*(1 - x) используя метод Рунге-Кутта')
    plt.legend()
    plt.show()


def eulers_method2():
    """
    Применяя метод Эйлера функция составляет на отрезке [1; 1,5]
    таблицу значений решения уравнения y’’ + y’/x + y = 0
    с начальными условиями: y(1) = 0.77, y’ (1) = - 0.44.

    Шаг вычисления h = 0.1
    """

    # Определим функцию, представляющую данное дифференциальное уравнение
    def y_derivative(x, y, z):
        return z, (-z / x) - y

    # Начальные условия
    x0 = 1
    y0 = 0.77
    z0 = -0.44
    h = 0.1
    n = 10

    x_values = [x0]
    y_values = [y0]

    # Применение метода Эйлера
    for i in range(n):
        y_der = y_derivative(x_values[-1], y_values[-1], z0)
        y_new = y_values[-1] + h * y_der[0]
        z0 += h * y_der[1]
        x_values.append(x_values[-1] + h)
        y_values.append(y_new)

    # Интегральная прямая
    plt.plot(x_values, y_values, label='Solution')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Решение y’’ + y’/x + y = 0 используя метод Эйлера')
    plt.legend()
    plt.show()

    # Таблица значений
    print(" x    |     y ")
    print("--------------")
    for i in range(len(x_values)):
        print(f"{x_values[i]:.2f}  |  {y_values[i]:.2f}")


def runge_kutta_method2():
    """
    Применяя метод Рунге-Кутта функция составляет на отрезке [1; 1,5]
    таблицц значений решения уравнения y’’ + y’/x + y = 0
    с начальными условиями: y(1) = 0.77, y’ (1) = - 0.44.

    Шаг вычисления h = 0.1
    """

    # Определяем функции, обозначающие данное дифференциальное уравнение
    def f(x, y, z):
        return z, (-z / x) - y

    # Начальные условия и параметры
    x0 = 1
    y0 = 0.77
    z0 = -0.44
    h = 0.1
    n = 10

    x_values = [x0]
    y_values = [y0]

    # Метод Рунге-Кутта
    for i in range(n):
        k1y, k1z = h * z0, h * (-(z0 / x0) - y0)
        k2y, k2z = h * (z0 + 0.5 * k1z), h * (-(z0 + 0.5 * k1z) / (x0 + 0.5 * h) - (y0 + 0.5 * k1y))
        k3y, k3z = h * (z0 + 0.5 * k2z), h * (-(z0 + 0.5 * k2z) / (x0 + 0.5 * h) - (y0 + 0.5 * k2y))
        k4y, k4z = h * (z0 + k3z), h * (-(z0 + k3z) / (x0 + h) - (y0 + k3y))

        y0 += (k1y + 2 * k2y + 2 * k3y + k4y) / 6
        z0 += (k1z + 2 * k2z + 2 * k3z + k4z) / 6
        x0 += h

        x_values.append(x0)
        y_values.append(y0)

    # Интегральная прямая
    plt.plot(x_values, y_values, label='Solution')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Решение y’’ + y’/x + y = 0 используя метод Рунге-Кутта')
    plt.legend()
    plt.show()

    # Таблица значений
    print(" x    |    y ")
    print("-------------")
    for i in range(len(x_values)):
        print(f"{x_values[i]:.2f}  |  {y_values[i]:.2f}")


def system_of_differential_equations():
    """
    Функция для решения системы дифференциальных уравнений
    dy/dt = - 2x + 5z
    dy/dt = sin(t – 1)x – y + 3z
    dz/dt = - x +2z

    Начальные условия: x(0) = 2, y(0) = 1, z(0) = 1
    Составляет таблицу значений функций x(t), y(t), z(t) на отрезке [0; 0.3] с шагом h = 0.003.
    Использован метод Эйлера.
    """

    # Определим функции, представляющие систему уравнений
    def dx_dt(x, y, z):
        return -2 * x + 5 * z

    def dy_dt(t, x, y, z):
        return np.sin(t - 1) * x - y + 3 * z

    def dz_dt(x, z):
        return -x + 2 * z

    # Начальные условия и параметры
    a = 0
    b = 0.3
    h = 0.03
    n = int((b - a) / h)

    t = a
    x = 2  # x(0) = 2
    y = 1  # y(0) = 1
    z = 1  # z(0) = 1

    # Массивы для хранения значений
    t_values = [t]
    x_values = [x]
    y_values = [y]
    z_values = [z]

    # Применение метода Эйлера
    for i in range(n):
        x += h * dx_dt(x, y, z)
        y += h * dy_dt(t, x, y, z)
        z += h * dz_dt(x, z)
        t += h

        t_values.append(t)
        x_values.append(x)
        y_values.append(y)
        z_values.append(z)

    # Визуализация результатов
    print(" t    |   x    |   y    |   z")
    print("-------------------------------")
    for i in range(n + 1):
        print(f"{t_values[i]:.2f}  |  {x_values[i]:.2f}  |  {y_values[i]:.2f}  |  {z_values[i]:.2f}")


# functions for solving nonlinear equations


def dichotomy_method():
    """
    Эта функция реализует метод деления отрезка пополам для нахождения корня уравнения
    на отрезке [a, b] с заданной точностью.

    В качестве примера находится корень уравнения 2x^4 - 8x^3 + 8x^2 - 1 на отрезке [-1; 0]
    """

    def y(x):
        return (2 * x ** 4) - (8 * x ** 3) + (8 * x ** 2) - 1

    a = -1
    b = 0
    try:
        h = float(input('Введите значение точности: '))
    except ValueError:
        print('Точность должна быть записана в десятичном виде, взято значение по умолчанию')
        h = 0.001

    # Находим середину отрезка
    x = (a + b) / 2
    while abs(b - a) >= 2 * h:
        # При попадании в полосу шумов завершаем итерационный процесс
        if abs(y(x)) < h:
            break
        if y(a) * y(x) < 0:
            b = x
        elif y(x) * y(b) < 0:
            a = x
        else:
            print('Ошибка!')
            return None
        x = (a + b) / 2

    print(f'Приближенное значение x с точностью {h} равно', round(x, int(abs(log10(h)))))


def chord_method():
    """
    Эта функция реализует метод хорд для нахождения корня уравнения
    на отрезке [a, b] с заданной точностью.

    В качестве примера находится корень уравнения 2x^4 - 8x^3 + 8x^2 - 1 на отрезке [-1; 0]
    """

    def y(x):
        return (2 * x ** 4) - (8 * x ** 3) + (8 * x ** 2) - 1

    a = -1
    b = 0
    try:
        e = float(input('Введите значение точности: '))
    except ValueError:
        print('Точность должна быть записана в десятичном виде, взято значение по умолчанию')
        e = 0.001

    # Уравнение для точки пересечения прямой с осью абсцисс (x=х0,у=0)
    x = a - ((b - a) / (y(b) - y(a))) * y(a)
    # Заканчиваем процесс уточнения корня, когда расстояние между очередными приближениями
    # станет меньше заданной точности
    while abs(b - x) >= e:
        # При попадании в полосу шумов завершаем итерационный процесс
        if abs(y(x)) < e:
            break
        if y(a) * y(x) < 0:
            b = x
        elif y(x) * y(b) < 0:
            a = x
        else:
            print('Ошибка!')
            return None
        x = a - ((b - a) / (y(b) - y(a))) * y(a)

    print(f'Приближенное значение x с точностью {e} равно', round(x, int(abs(log10(e)))))


def newton_method():
    """
    Эта функция реализует метод касательных (Ньютона) для нахождения корня уравнения
    на отрезке [a, b] с заданной точностью.

    В качестве примера находится корень уравнения 2x^4 - 8x^3 + 8x^2 - 1 на отрезке [-1; -0.1]
    """

    def y(x):
        return (2 * x ** 4) - (8 * x ** 3) + (8 * x ** 2) - 1

    def derivative_y(x):
        return (8 * x ** 3) - (24 * x ** 2) + (16 * x)

    a = -1
    b = -0.1
    try:
        h = float(input('Введите значение точности: '))
    except ValueError:
        print('Точность должна быть записана в десятичном виде, взято значение по умолчанию')
        h = 0.001

    # Середину отрезка, на котором есть корень, принимаем за приближение корня
    x = (a + b) / 2
    # Заканчиваем процесс уточнения корня, когда расстояние между очередными приближениями
    # станет меньше заданной точности
    while abs(b - x) >= h:
        # При попадании в полосу шумов завершаем итерационный процесс
        if abs(y(x)) < h:
            break
        b = x
        # Приближенное значение корня, за которое принимаем точку пересечения касательной с осью
        x = b - (y(b) / derivative_y(b))

    print(f'Приближенное значение x с точностью {h} равно', round(x, int(abs(log10(h)))))


# functions for solving nonlinear equations

# Коэффициенты a для разложения в ряд Чебышева
coefficients = [0.9999998, 1.0000000, 0.5000063, 0.1666674, 0.0416350, 0.0083298, 0.0014393, 0.0002040]


# Функция для вычисления значения e^x приблизительно с помощью ряда Чебышева
def my_e(x=1, accuracy=2 * 10 ** (-7)):
    a = [0.9999998, 1, 0.5000063, 0.1666674, 0.041635, 0.0083298, 0.0014393, 0.000204]
    sum = 0
    for k in range(len(a)):
        sum += a[k] * (x ** k)
        if abs(a[k] * (x ** k)) < accuracy:
            break
    print(f"Приблизительное значение e^x с использованием ряда Чебышева: {round(sum, 7)}")


def my_sin(x=pi / 2, accuracy=10 ** (-9)):
    a = [1.000000002, -0.166666589, 0.008333075, -0.000198107, 0.000002608]
    sum = 0
    for k in range(len(a)):
        U = a[k] * x ** (2 * k + 1)
        sum += U
        if abs(U) < accuracy:
            break
    print(f"Приблизительное значение sin(x) с использованием ряда Чебышева: {round(sum, int(abs(log10(accuracy))))}")


def print_result_sqrt():
    def my_sqrt(x, y0, accuracy=10 ** (-9)):
        U = 1
        while abs(U) > accuracy:
            y1 = (y0 + x / y0) / 2
            U = y1 - y0
            y0 = y1
        return y1

    print(f"Приблизительное значение квадратного корня 14,76 равно: {round(my_sqrt(14.76, 3.8), 9)}")
    print(f"Приблизительное значение квадратного корня 0,142 равно: {round(my_sqrt(0.142, 0.4), 9)}")


def print_result_rsqrt():
    def rsqrt(x, y0, accuracy=0.00001):
        U = 1
        y1 = 0
        while abs(U) > accuracy:
            y1 = (y0 / 2) * (3 - x * y0 * y0)
            U = y1 - y0
            y0 = y1
        return y1

    print(f"Приблизительное обратное значение квадратного корня 17,32 равно: {round(rsqrt(17.32, 0.24), 6)}")
    print(f"Приблизительное обратное значение квадратного корня 0,464 равно: {round(rsqrt(0.464, 1.5), 6)}")
