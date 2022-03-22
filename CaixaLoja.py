nome = input("Digite o nome do produto:")
preco = float(input("Digite o preço do produto: "))
itens = conta = maior = 0
caro = ''


while True:
    conta += preco
    itens += 1
    if preco > maior:
        maior = preco
        caro = nome
    pausa = input("Quer continuar? [S/N]: ").strip().upper()
    print("==>" * 3)
    if pausa == 'S':
        nome = input("Digite o nome do produto:")
        preco = float(input("Digite o preço do produto: "))
    else:
        break

print(f'O valor total é ${conta}')
print(f'O maior valor foi {maior} do item {caro}.')
print(f'Foram {itens} itens.')
