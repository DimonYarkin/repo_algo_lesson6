"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""

from memory_profiler import profile
@profile
def wrapper(length):
    def factorial(n):
        if n == 0: return 1
        return n*factorial(n-1)
    print(f'Факториал числа {length} равен {factorial(length)}')
'''
Для профилирование рекурсии необходимо поместить рекурсию в функцию обертку 
для чтобы была создана только одна таблица вызывов

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    10     17.3 MiB     17.3 MiB           1   @profile
    11                                         def wrapper(length):
    12     18.2 MiB      0.9 MiB         502       def factorial(n):
    13     18.2 MiB      0.0 MiB         501           if n == 0: return 1
    14     18.2 MiB      0.0 MiB         500           return n*factorial(n-1)
    15     18.2 MiB      0.0 MiB           1       print(f'Факториал числа {length} равен {factorial(length)}')


'''



@profile
def factorial(n):
    if n == 0: return 1
    return n * factorial(n - 1)
'''
Результат профилирования без обертки

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    17     17.5 MiB     17.5 MiB           1   @profile
    18                                         def factorial(n):
    19     17.5 MiB      0.0 MiB           1       if n == 0: return 1
    20                                             return n * factorial(n - 1)


Filename: /media/dimon/hrcdisk/geekbraens/Урок 6/Урок 6. Практическое задание/task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    17     17.5 MiB     17.5 MiB           2   @profile
    18                                         def factorial(n):
    19     17.5 MiB      0.0 MiB           2       if n == 0: return 1
    20     17.5 MiB      0.0 MiB           1       return n * factorial(n - 1)


Filename: /media/dimon/hrcdisk/geekbraens/Урок 6/Урок 6. Практическое задание/task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    17     17.5 MiB     17.5 MiB           3   @profile
    18                                         def factorial(n):
    19     17.5 MiB      0.0 MiB           3       if n == 0: return 1
    20     17.5 MiB      0.0 MiB           2       return n * factorial(n - 1)


Filename: /media/dimon/hrcdisk/geekbraens/Урок 6/Урок 6. Практическое задание/task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    17     17.5 MiB     17.5 MiB           4   @profile
    18                                         def factorial(n):
    19     17.5 MiB      0.0 MiB           4       if n == 0: return 1
    20     17.5 MiB      0.0 MiB           3       return n * factorial(n - 1)


Filename: /media/dimon/hrcdisk/geekbraens/Урок 6/Урок 6. Практическое задание/task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    17     17.5 MiB     17.5 MiB           5   @profile
    18                                         def factorial(n):
    19     17.5 MiB      0.0 MiB           5       if n == 0: return 1
    20     17.5 MiB      0.0 MiB           4       return n * factorial(n - 1)


Filename: /media/dimon/hrcdisk/geekbraens/Урок 6/Урок 6. Практическое задание/task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    17     17.5 MiB     17.5 MiB           6   @profile
    18                                         def factorial(n):
    19     17.5 MiB      0.0 MiB           6       if n == 0: return 1
    20     17.5 MiB      0.0 MiB           5       return n * factorial(n - 1)



Process finished with exit code 0



'''

wrapper(500)
factorial(5)


