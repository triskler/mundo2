import random

#variaveis
numero = int(input("Digite um numero de 0 a 5: "))
numero_pc = random.randint(0, 5)
escolha = str(input("Par ou Impar [P/I]: ")).strip().upper()
soma = 0
vitoria = 0
tentativa = 1


#Processamento
while vitoria < 3:
    soma = numero + numero_pc
    if soma % 2 == 0:
        if escolha == 'P':
            print(f'Venceu! o Computador escolheu {numero_pc}')
            vitoria += 1
            tentativa += 1
            if vitoria == 3:
                break
            numero = int(input("Digite um numero de 0 a 5: "))
            numero_pc = random.randint(0, 5)
            escolha = str(input("Par ou Impar [P/I]: ")).strip().upper()
        elif escolha == 'I':
            print(f'Perdeu! O computador escolheu {numero_pc}')
            tentativa += 1
            numero = int(input("Digite um numero de 0 a 5: "))
            numero_pc = random.randint(0, 5)
            escolha = str(input("Par ou Impar [P/I]: ")).strip().upper()
        else:
            break
    else:
        if escolha == 'P':
            print(f'Perdeu! O computador escolheu {numero_pc}')
            tentativa += 1
            numero = int(input("Digite um numero de 0 a 5: "))
            numero_pc = random.randint(0, 5)
            escolha = str(input("Par ou Impar [P/I]: ")).strip().upper()
        elif escolha == 'I':
            print(f'Venceu! O computador escolheu {numero_pc}')
            tentativa += 1
            vitoria += 1
            if vitoria == 3:
                break
            numero = int(input("Digite um numero de 0 a 5: "))
            numero_pc = random.randint(0, 5)
            escolha = str(input("Par ou Impar [P/I]: ")).strip().upper()
        else:
            break
print(f'Jogo Finalizado! Foram {tentativa} tentativas para {vitoria} vitórias.')
