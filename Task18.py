# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

N = abs(int(input('Введите количество элементов массива N: ')))
array_A_input = input(f'Введите через пробел {N} элементов массива A[1..N]: ').split()
array_A = list(map(int, array_A_input))
if len(array_A) != N:
    print(f'Введенные элементы массива A[1..N] не соответствуют заданному количеству элементов: {N}')
else:
    X = int(input('Введите число X, с которым необходимо сравнить элементы заданного массива: '))
    min = abs(X - array_A[0])
    index = 0
    index2 = 0
    for i in range(N):
        diff = abs(X - array_A[i])
        if diff < min:
            min = diff
            index = i
            closest_to_x = array_A[index]
        for k in range(N):
            diff2 = abs(X - array_A[k])
            if diff2 == min and array_A[k] != array_A[index]:
                index2 = k
                closest_to_x_2 = array_A[index2]
    if index2 == 0:
        print(f'Ближайшим к X по величине элементом массива является {closest_to_x}')
    else:
        print(f'Ближайшими к X по величине элементами массива являются {closest_to_x} и {closest_to_x_2}')
