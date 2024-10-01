print("Clara Vecchio Machado da Silva\nRA: 1051392421023 \nDSM - 1°Semestre\n")

#Compras acima de 300,00 fornece 20% de desconto
#200,00 desconto de 15%
#acima de 100,00 desconto de 10%

compra1 = float(input("Digite o valor da primeira compra: R$ "))
compra2 = float(input("Digite o valor da segunda compra: R$ "))
compra3 = float(input("Digite o valor da terceira compra: R$ "))

def calcular_desconto(valor):
    if valor > 300:
        desconto = 0.20
    elif valor > 200:
        desconto = 0.15
    elif valor > 100:
        desconto = 0.10
    else:
        desconto = 0.0
    return valor - (valor * desconto), desconto * 100


valor_desconto1, desconto1 = calcular_desconto(compra1)
valor_desconto2, desconto2 = calcular_desconto(compra2)
valor_desconto3, desconto3 = calcular_desconto(compra3)

print("Compra 1: R$", compra1, "- Desconto de", desconto1,"% - Valor com desconto: R$",valor_desconto1)
print(f"Compra 2: R$ {compra2:.2f} - Desconto de {desconto2:.0f}% - Valor com desconto: R$ {valor_desconto2:.2f}")
print(f"Compra 3: R$ {compra3:.2f} - Desconto de {desconto3:.0f}% - Valor com desconto: R$ {valor_desconto3:.2f}")

# Calcula o valor total das compras e o valor total com desconto
valor_total = compra1 + compra2 + compra3
valor_total_com_desconto = valor_desconto1 + valor_desconto2 + valor_desconto3

# Exibe o valor total e o valor total com desconto
print(f"\nValor total das compras: R$ {valor_total:.2f}")
print(f"Valor total com desconto: R$ {valor_total_com_desconto:.2f}")