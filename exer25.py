print("Clara Vecchio Machado da Silva\nRA: 1051392421023 \nDSM - 1°Semestre\n")

import math

# Solicita ao usuário o tamanho da área a ser pintada em metros quadrados
area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Considera uma folga de 10% na quantidade de tinta
area_com_folga = area * 1.10

# Define as variáveis de cobertura e preços
cobertura_tinta = 6  # 1 litro cobre 6 metros quadrados
litros_necessarios = area_com_folga / cobertura_tinta

lata_litros = 18
lata_preco = 80.00

galao_litros = 3.6
galao_preco = 35.00

# a) Comprar apenas latas de 18 litros
latas_necessarias = math.ceil(litros_necessarios / lata_litros)
preco_apenas_latas = latas_necessarias * lata_preco

# b) Comprar apenas galões de 3,6 litros
galoes_necessarios = math.ceil(litros_necessarios / galao_litros)
preco_apenas_galoes = galoes_necessarios * galao_preco

# c) Misturar latas e galões para obter o menor preço
# Calcula a quantidade de latas completas e depois os galões para o restante
latas_mistura = math.floor(litros_necessarios / lata_litros)
restante_litros = litros_necessarios - (latas_mistura * lata_litros)
galoes_mistura = math.ceil(restante_litros / galao_litros)
preco_mistura = (latas_mistura * lata_preco) + (galoes_mistura * galao_preco)

# Exibe os resultados
print(f"\nSituação A: Comprar apenas latas de 18 litros")
print(f"Quantidade de latas: {latas_necessarias}")
print(f"Preço total: R$ {preco_apenas_latas:.2f}")

print(f"\nSituação B: Comprar apenas galões de 3,6 litros")
print(f"Quantidade de galões: {galoes_necessarios}")
print(f"Preço total: R$ {preco_apenas_galoes:.2f}")

print(f"\nSituação C: Misturar latas e galões (melhor preço)")
print(f"Quantidade de latas: {latas_mistura}")
print(f"Quantidade de galões: {galoes_mistura}")
print(f"Preço total: R$ {preco_mistura:.2f}")
