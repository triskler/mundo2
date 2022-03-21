print("==> Calculadora de progressão aritmetica <==")

data = int(input("Digite o termo inicial: "))
razao = int(input("Digite a razão: "))
num = 10
novo = 0


while num > 0:
    print(f'{data}', end="")
    print(f' => ' if num > 1 else ' => PAUSA!', end="")
    data += razao
    num -= 1
    if num == 0:
        num = int(input(" Quantos termos a mais: "))

