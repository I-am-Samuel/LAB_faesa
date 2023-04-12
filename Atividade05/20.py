#calculadora
n1 = float(input("Digite um úmero"))
operacao = int(input("Escolha a operação: 1-Soma 2-Subtração 3-Multiplicação 4-Divisão"))
n2 = float(input("Digite outro úmero"))
if operacao == 1:
    soma = n1+n2
    print(soma)

elif operacao == 2:
    subtracao = n1-n2
    print(subtracao)

elif operacao == 3:
    multiplicacao = n1*n2
    print(multiplicacao)

elif operacao == 4:
    divisao = n1/n2
    print(divisao)

else:
    print("Opção inválida!")