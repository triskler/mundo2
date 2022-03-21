print("==> Calculadora de progressão aritmética <==")
data = int(input("Digite o termo inicial: "))
razao = int(input("Digite a razão: "))
num = int(input("Numero de termos a calcular: "))


print(f'{data} => ', end="")
while num:
    data += razao
    print(f'{data}', end="")
    print(f' => ' if num > 1 else ' => Acabou!', end="")
    num -= 1