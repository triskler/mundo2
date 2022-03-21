import random
#Apresentação do jogo
print("\033[36m<=====>" * 5)
print("=======>JOGO DA ADIVINHAÇÃO!<======")
print("===>DIGITE UM NUMERO DE 0 A 10!<===")
print("===========>BOA SORTE!<============")
print("<=====>" * 5)
#Variaveis
data = int(input("\033[35mDigite seu palpite: "))
comp = random.randint(0, 10)
tentativas = 1

while data < 1:
    print("Digite um valor entre 0 e 10!")
    data = int(input("Tente novamente, agora entre 0 e 10: "))

while data > 10:
    print("Digite um valor entre 0 e 10!")
    data = int(input("Tente novamente, agora entre 0 e 10: "))

#Bloco de processamento
while data != comp:
    if data > comp:
        print("\033[34mTente um numero menor!")
        tentativas += 1
        data = int(input("\033[35mTente outra vez! "))
    elif data < comp:
        print("\033[37m==> Tente um numero maior! <==")
        tentativas += 1
        data = int(input("\033[35mTente outra vez! "))

print("ACERTOU!!")

if tentativas == 1 :
    print(f'Você conseguiu em {tentativas} tentativa. Excelente! ')
elif 1 < tentativas <= 3:
    print(f'Você acertou em {tentativas} tentativas. Muito Bom!')
else:
    print("Parabéns!")
