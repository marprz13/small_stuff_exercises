

def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1


program = True

while program:
    try:
        wybor = int(input('Podaj liczbe: '))
    except ValueError:
        print('To nie jest liczba calkowita: ')
        continue


    if collatz(wybor) == 1:
        print('udalo sie')
        program = False
    else:
        continue
