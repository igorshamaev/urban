first = int(input('Введите число №1:'))
second = int(input('Введите число №2:'))
third = int(input('Введите число №3:'))
if first == second and second == third:
    print(3, '(Все введённые числа равны)')
elif first == second or first == third or second == third:
    print(2, '(Равны только два из введённых чисел)')
else:
    print(0, '(Равных чисел нет)')