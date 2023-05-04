soma_restos = 0
for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    resto = numero % 3
    soma_restos += resto
print("A soma dos restos da divisão por 3 dos números digitados é:", soma_restos)