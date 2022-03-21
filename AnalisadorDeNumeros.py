print("| === | === | === | === | ")
print("=== Somador de numeros ===")
print("| === | === | === | === | ")


data = int(input("Digite um numero: "))
soma = 0
while data != 999:
    soma += data
    data = int(input("Digite um numero: "))
print(f'A soma dos numeros é {soma}')
