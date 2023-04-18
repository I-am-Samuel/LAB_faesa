nome = input("Digite o nome do aluno(a):")
notaDaProva = float(input("Digite a nota da prova:"))
notaDoTrabalho = float(input("Digite a nota do trabalho:"))
media = (notaDaProva + notaDoTrabalho)/2
if media>=7:
    print(nome,"Aprovado!")
    print("Média:",media)
elif media<7:
    print(nome,"Reprovado!")
    print("Média:",media)