print("==> Sequência de Fibonacci <==")
data = int(input("Digite quantos termos quer mostrar: "))

seq = [0, 1, 1]

while data > 3:
    resultado = seq[-1] + seq[-2]
    seq.append(resultado)
    data -= 1

print(seq)

