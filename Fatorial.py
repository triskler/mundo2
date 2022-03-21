from time import sleep

print("==> " * 7)
print("Calculadora de fatoriais")
print("==> " * 7)

#Variaveis
data = int(input("Digite um numero: "))
resultado = 1
print(f'O fatorial de {data}')

#Processamento
print("CALCULANDO...")
sleep(2)
print(f'{data}! = ', end="")

while data > 0:
    print(f'{data}', end="")
    print(" x " if data > 1 else " = ", end="")
    resultado *= data
    data -= 1


print(f'{resultado}')


'''
from math import factorial

data = input("Digite o valor para calcular seu fatorial: )
fac = factorial(data)
print(f'O fatorial de {data} é {fac}')

'''



