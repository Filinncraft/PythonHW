# Задача 2: Найдите сумму цифр трехзначного числа.

# num = int(input("Введите трехзначное число: "))
# if num < 99 or num > 999:
#     print("Некорректное число")
# else:
#     count = 0
#     summ = 0
#     while count < 3:
#         summ = summ + num%10
#         num = num//10
#         count = count + 1
#     else:
#         print("Сумма цифр - ", summ)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# s = int(input("Количество журавликов - "))
# if s % 6 == 0:
#     print(f"Катя - {s*2/3}, Петя и Сережа - {s/6}")
# else:
#     print("Недостаточная информация")

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# num = int(input("Введите номер билета - "))   
# if (len(str(num)) == 6):
#     num1 = num // 100000
#     num2 = num // 10000 % 10
#     num3 = num // 1000 % 100 % 10
#     num4 = num // 100 % 1000 % 100 % 10
#     num5 = num // 10 % 10000 % 1000 % 100 % 10
#     num6 = num % 10
#     sum1 = (num1 + num2 + num3)
#     sum2 = (num4 + num5 + num6)
#     if (sum1 == sum2):
#         print('Yes')
#     else:
#         print('No')
# else:
#     print("Введите шестизначное число")

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# n = int(input("Введите ширину - "))
# m = int(input("Введите длину - "))
# k = int(input("Введите количество долек - "))
# if k % n == 0 or k % m == 0:
#     print("Yes")
# else:
#     print("No")

# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх 
# одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# n = int(input("Введите количество монет: "))
# head = 0
# tail = 0
# for i in range(n):
#     x = int(input())
#     if x == 0:
#         head += 1
#     else:
#         tail += 1
# if head > tail:
#     print(tail)
# else:
#     print(head)

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# s = int(input("Введите сумму чисел: "))
# p = int(input("Введите произведение чисел: "))
# for x in range(s):
#     for y in range(p):
#         if s == x + y and p == x * y:
#             print(x, y)

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# n = int(input("Введите число: "))
# count = 1
# while 2 ** count <= n:
#     print(2 ** count)
#     count += 1

# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# from random import randint
# n = int(input("Введите размер массива: "))
# a = [randint(0, 10) for _ in range(n)]
# print(a)
# x = int(input("Введите число: "))
# count = 0
# for i in range(n):
#     if a[i] == x:
#         count +=1
# print(count)


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# from random import randint
# n = int(input("Введите размер массива: "))
# max = 10
# a = [randint(0, max) for _ in range(n)]
# print(a)
# x = int(input("Введите число: "))
# diff = max + 1
# temp = 0
# for i in range(n):
#     if abs(x - a[i]) < diff:
#         diff = abs(x - a[i])
#         temp = a[i]

# print(temp)


# Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; 
# B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# en = {1:'aeioulnstr', 2:'dg', 3:'bcmp', 4:'fhvwy', 5:'k', 8:'jx', 10:'qz'}
# text = input("Your word is: ").lower()
# print(sum([k for i in text for k, v in en.items() if i in v]))