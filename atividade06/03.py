nome1 = input("Digite o nome:")
nome2 = input("Digite o nome:")
nome3 = input("Digite o nome:")
finalista1 = int(input("Digite a pontuação:"))
finalista2 = int(input("Digite a pontuação:"))
finalista3 = int(input("Digite a pontuação:"))
if finalista1 > finalista2 and finalista3:
    print("O finalista {} tem a maior pontuação, com {} de score".format(nome1, finalista1))
elif finalista2 > finalista1 and finalista3:
    print("O finalista {} tem a maior pontuação, com {} de score".format(nome2, finalista2))
elif finalista3 > finalista1 and finalista2:
    print("O finalista {} tem a maior pontuação, com {} de score".format(nome3, finalista3))
else: 
    print("Finalista com a mesma pontuação")