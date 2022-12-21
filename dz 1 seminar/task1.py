# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

print("Введите день недели")
n = int(input())
if n < 8:
    if n == 1:
        print('Понедельник! Этот день не является выходным.')
    elif n == 2:
        print('Вторник! Этот день не является выходным.')
    elif n == 3:
        print('Среда! Этот день не является выходным.')
    elif n == 4:
        print('Четверг! Этот день не является выходным.')
    elif n == 5:
        print('Пятница! Этот день не является выходным.')
    elif n == 6:
        print('Суббота! Этот день выходной.')
    elif n == 7:
        print('Воскресенье! Этот день выходной.')
else:
    print('Такого дня недели не существует!')
