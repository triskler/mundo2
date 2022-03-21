data = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]

while data not in "MF":
    data = str(input("Dados inválidos. Digite um sexo valido [M/F]: ")).upper()[0]

print(f'Sexo {data} Registrado!')
