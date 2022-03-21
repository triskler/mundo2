data = float(input("Digite o peso da pessoa 1: "))
data2 = float(input("Digite o peso da pessoa 2: "))
data3 = float(input("Digite o peso da pessoa 3: "))
data4 = float(input("Digite o peso da pessoa 4: "))
data5 = float(input("Digite o peso da pessoa 5: "))

lista = [data, data2, data3, data4, data5]

maior = max(lista)
menor = min(lista)

print(f'O maior peso foi {maior} e o menor foi {menor}')