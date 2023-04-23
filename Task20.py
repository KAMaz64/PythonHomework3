# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; 
# J, X – 8 очков; 
# Q, Z – 10 очков. 
# А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы.

# *Пример:*

# ноутбук
#     12

english = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP', 4:'FHVWY', 5:'K', 8:'JZ', 10:'QZ'}
eng = {1:'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 0:'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'}
russian = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ', 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФЩЪ', 0:'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
rus = {0:'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1:'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'}

N = abs(int(input('Выберите раскладку для новой игры (0 - Английская; 1 - Русская): ')))
word = input('Введите слово: ').upper()
if N == 0:
    if sum([points for letter in word for points, sublist in eng.items() if letter in sublist]) != len(word):
        print('Нарушение правил игры!')
    else:
        print('За это слово вы получаете', sum([points for letter in word for points, sublist in english.items() if letter in sublist]), 'очков')
elif N == 1:
    if sum([points for letter in word for points, sublist in rus.items() if letter in sublist]) != len(word):
        print('Нарушение правил игры!')
    else:
        print('За это слово вы получаете', sum([points for letter in word for points, sublist in russian.items() if letter in sublist]), 'очков')