#Apresentação
from time import sleep

print("=========>x<========")
print("==> CALCULADORA <===")
print("=========>x<========")

#Variaveis
data1 = int(input("Digite o primeiro numero: "))
data2 = int(input("Digite o segundo numero: "))
print("\033[31m[ 1 ] somar\033[m")
print("\033[32m[ 2 ] multiplicar\033[m")
print("\033[33m[ 3 ] maior numero\033[m")
print("\033[34m[ 4 ] novos numeros\033[m")
print("\033[35m[ 5 ] sair do programa\033[m")
option = int(input("Digite a operação desejada: "))


#Processamento
while option < 1:
    print("Digite uma opção válida! ")
    sleep(1)
    option = int(input("Digite a operação desejada: "))

while option > 5:
    print("Digite uma opção válida! ")
    sleep(1)
    option = int(input("Digite a operação desejada: "))
    print(" ")

while option != 5:
    if option == 1:
        resultado = data1 + data2
        print(f'\033[31mA soma de {data1} e {data2} é {resultado}.\033[m')
        print(" ")
        option = int(input("Digite a operação desejada: "))
    elif option == 2:
        resultado = data1 * data2
        print(f'\033[32mA multiplicação de {data1} por {data2} é {resultado}.\033[m')
        print(" ")
        option = int(input("Digite a operação desejada: "))
    elif option == 3:
        resultado = [data1, data2]
        resultado = max(resultado)
        print(f'\033[33mO maior numero é {resultado}\033[m')
        print(" ")
        option = int(input("Digite a operação desejada: "))
    elif option == 4:
        data1 = int(input("Digite o primeiro numero: "))
        data2 = int(input("Digite o segundo numero: "))
        print("\033[31m[ 1 ] somar\033[m")
        print("\033[32m[ 2 ] multiplicar\033[m")
        print("\033[33m[ 3 ] maior numero\033[m")
        print("\033[34m[ 4 ] novos numeros\033[m")
        print("\033[35m[ 5 ] sair do programa\033[m")
        option = int(input("Digite a operação desejada: "))

print("PROCESSANDO...")
sleep(1.5)
print("Fim do programa! Tenha um bom dia! ")