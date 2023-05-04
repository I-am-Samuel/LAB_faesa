a = int(input("digite o valor de a:"))
b = int(input("digite o valor de b:"))
soma = 0
if a < b:
    for i in range(a+1,b):
        soma += i
elif a > b:
    for i in range(b+1,a):
        soma += i
else:
    print(" a e b são iguais. Logo,")
    print("a soma é ", soma)
print("a soma é ", soma)