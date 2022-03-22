from time import sleep

data = int(input("Digite o valor a sacar: "))
cedulas_100 = 0
cedulas_50 = 0
cedulas_20 = 0
cedulas_10 = 0
cedulas_5 = 0
cedulas_1 = 0

while data >= 100:
    data -= 100
    cedulas_100 += 1
    if data < 100:
        break

while data >= 50:
    data -= 50
    cedulas_50 += 1
    if data < 50:
        break

while data >= 20:
    data -= 20
    cedulas_20 += 1
    if data < 20:
        break
while data >= 10:
    data -= 10
    cedulas_10 += 1
    if data < 10:
        break
while data >= 5:
    data -= 5
    cedulas_5 += 1
    if data < 5:
        break
while data >= 1:
    data -= 1
    cedulas_1 += 1
    if data == 0:
        break

print("Separando notas...")
sleep(2)

if cedulas_100 >= 1:
    print(f'O saque será em {cedulas_100} notas de $100')
    sleep(1)

if cedulas_50 >= 1:
    print(f'O saque será em {cedulas_50} notas de $50')
    sleep(1)

if cedulas_20 >= 1:
    print(f'O saque será em {cedulas_20} notas de $20')
    sleep(1)

if cedulas_10 >= 1:
    print(f'O saque será em {cedulas_10} notas de $10')
    sleep(1)

if cedulas_5 >= 1:
    print(f'O saque será em {cedulas_5} notas de $5')
    sleep(1)

if cedulas_1 >= 1:
    print(f'O saque será em {cedulas_1} notas de $1')
    sleep(1)

print("Obrigado por utilizar o Banco Rafael, tenha um bom dia!")
