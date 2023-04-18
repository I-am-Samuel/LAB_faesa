numero = int(input("Digite um número inteiro para calcular o fatorial: "))
fatorial = 1
contador = 1

while contador <= numero:
    fatorial *= contador
    contador += 1

print("O fatorial de", numero, "é", fatorial)
