import random

supplies = ["długopisy", "zszywacze", "miotacze ognia", "segregatory"]
for index, item in enumerate(supplies):
    print("Indeks " + str(index) + " na liście supplies to: " + supplies[index])

for i, j in enumerate(supplies):
    print(i, j)


print()
print(supplies.index("zszywacze"))
print(random.choice(supplies))

supplies.sort(key=str.lower)
print(supplies)

a = 'imie'

for i in a:
    print(i, end='kopa')
