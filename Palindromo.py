data = input("Digite uma frase: ").strip().upper()
separado = data.split()
reverso = ''
junto = ''.join(separado)
for i in range(len(junto) - 1, -1, -1):
    reverso += junto[i]
if junto == reverso:
    print(f'\033[0;32mA frase {data} é um PALINDROMO!')
    print(f'{junto} == {reverso}')
else:
    print(f'\033[0;31mA frase {data} NÃO é um PALINDROMO!')
    print(f'{junto} != {reverso}')



