maior_altura = 0
while maior_altura >= 0:
    altura = float(input('Digite a altura de uma moça ou 0 para finalizar o programa: '))
    if altura > maior_altura:
        maior_altura = altura
    elif altura == 0:
        print('A maior altura de uma moça é {}'.format(maior_altura))
        break