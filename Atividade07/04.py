cont = 0
soma = 0
numero = 0
while numero >= 0:
    numero = int(input('Digite um número: '))
    if numero >= 0:
        cont += 1
        soma = soma + numero
        media = soma // cont
    elif numero == -1:
        cont -= 1
print('A média é essa: {} '.format(media))
