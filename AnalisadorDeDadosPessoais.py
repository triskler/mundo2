from datetime import date
data = []
print("==> " * 10)
data1 = str(input("Digite o nome:"))
data1_idade = int(input("Digite a idade: "))
data1_sexo = str(input("Digite o sexo [M/F]: ")).upper()
print("==> " * 10)
data2 = str(input("Digite o nome:"))
data2_idade = int(input("Digite a idade: "))
data2_sexo = str(input("Digite o sexo [M/F]: ")).upper()
print("==> " * 10)
data3 = str(input("Digite o nome:"))
data3_idade = int(input("Digite a idade: "))
data3_sexo = str(input("Digite o sexo [M/F]: ")).upper()
print("==> " * 10)
data4 = str(input("Digite o nome:"))
data4_idade = int(input("Digite a idade: "))
data4_sexo = str(input("Digite o sexo [M/F]: ")).upper()

data_nome = [data1, data2, data3, data4]
data_sexo = [data1_sexo, data2_sexo, data3_sexo, data4_sexo]
data_idade = [data1_idade, data2_idade, data3_idade, data4_idade]

media = 0
contadorSexoFem = 0
contadorSexoMasc = 0
contadorMaior = 0
contadorMenor = 0

for i in range(0, len(data_sexo)):
    if data_sexo[i] == "F":
        contadorSexoFem += 1
    elif data_sexo[i] == "M":
        contadorSexoMasc += 1


for i in range(len(data_idade)):
    if data_idade[i] >= 18:
        contadorMaior += 1
    else:
        contadorMenor += 1


for i in range(len(data_idade)):
    media += data_idade[i] / len(data_idade)

print(f'São {contadorMenor} menores de idade.')
print(f'São {contadorMaior} maiores de idade.')
print(f'Destes {contadorSexoMasc} são homens.')
print(f'{contadorSexoFem} são mulheres.')
print(f'A media de idade do grupo é de {media} anos.')

