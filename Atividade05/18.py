cotacao_dolar = float(input("Digite a cotação atual do dólar: "))
valor_real = float(input("Digite o valor em reais que deseja converter: "))
valor_dolar = valor_real / cotacao_dolar
print(f"Com a cotação atual de US$1,00 = R${cotacao_dolar:.2f}")
print(f"Você irá levar US${valor_dolar:.2f} na viagem.")
