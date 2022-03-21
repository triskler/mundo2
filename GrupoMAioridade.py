from datetime import date

data1 = int(input("Digite o ano de nascimento da pessoa 1: "))
data2 = int(input("Digite o ano de nascimento da pessoa 2: "))
data3 = int(input("Digite o ano de nascimento da pessoa 3: "))
data4 = int(input("Digite o ano de nascimento da pessoa 4: "))
data5 = int(input("Digite o ano de nascimento da pessoa 5: "))

lista = [data1, data2, data3, data4, data5]
atual = date.today().year
maior = 0
menor = 0


for i in range(0, len(lista)):
    conta = atual - lista[i]
    if conta >= 18:
        maior += 1
    else:
        menor += 1

print(data5)
print(f'Neste grupo, temos {menor} pessoas menores de 18 anos.')
print(f'Temos neste grupo, temos {maior} pessoas maiores de 18 anos.')



