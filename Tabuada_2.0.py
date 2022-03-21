print("============/ /=============")
print("==> Programa de tabuadas <==")
print("============/ /=============")

data = int(input("Digite um numero para ver sua tabuada: "))

while data > 0:
    print("==/ /==" * 5)
    print(f'{data} x 1 = {data}')
    print(f'{data} x 2 = {data * 2}')
    print(f'{data} x 3 = {data * 3}')
    print(f'{data} x 4 = {data * 4}')
    print(f'{data} x 5 = {data * 5}')
    print(f'{data} x 6 = {data * 6}')
    print(f'{data} x 7 = {data * 7}')
    print(f'{data} x 8 = {data * 8}')
    print(f'{data} x 9 = {data * 9}')
    print(f'{data} x 10 = {data * 10}')
    print("==/ /==" * 5)
    data = int(input("Digite um numero para ver sua tabuada: "))
    if data <= 0:
        break