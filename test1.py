# Вводится два числа, определить большее из них

a = int(input("Введите число а - "))
b = int(input("Введите число в - "))

if a > b:
    print(f" а = {a} больше b")

elif a==b:
    print('a = b')

else:
     print(f" b = {b} больше a")