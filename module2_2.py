fist = int(input('Ввведите первое число: '))
second = int(input('Ввведите второе число: '))
third = int(input('Ввведите третье число: '))
if fist == second and fist == third:
        print(3)
elif fist == second or fist == third or second == third:
        print(2)
else:
    print(0)