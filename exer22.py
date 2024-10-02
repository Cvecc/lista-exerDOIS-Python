print("Clara Vecchio Machado da Silva\nRA: 1051392421023 \nDSM - 1°Semestre\n")

compra1 = float(input("Digite o valor da primeira compra: R$"))
compra2 = float(input("Digite o valor da segunda compra: R$"))
compra3 = float(input("Digite o valor da terceira compra: R$"))

def calcular_desconto(valor):
    if valor > 300:
        desconto = 0.20
    elif valor > 200:
        desconto = 0.15
    elif valor > 100:
        desconto = 0.10
    else:
        desconto = 0
    return valor - (valor*desconto)

valor_desconto1 = calcular_desconto(compra1)
valor_desconto2 = calcular_desconto(compra2)
valor_desconto3 = calcular_desconto(compra3)

valor_total = valor_desconto1 + valor_desconto2 + valor_desconto3
valor_sem_desconto = compra1 + compra2 + compra3

print("\nO valor da compra 1 com desconto é R$"+str(valor_desconto1))
print("O valor da compra 2 com desconto é R$"+str(valor_desconto2))
print("O valor da compra 3 com desconto é R$"+str(valor_desconto3))

print("\nO valor total da compra é R$"+str(valor_sem_desconto))
print("O valor total da compra com desconto é R$"+str(valor_total))