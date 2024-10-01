print("Clara Vecchio Machado da Silva\nRA: 1051392421023 \nDSM - 1°Semestre\n")

# Solicita ao usuário dois números inteiros
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Realiza as quatro operações básicas
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

# Verifica se o segundo número não é zero para evitar divisão por zero
if num2 != 0:
    divisao = num1 / num2
else:
    divisao = "Indefinida (não é possível dividir por zero)"

# Exibe os resultados das operações
print(f"\nSoma: {num1} + {num2} = {soma}")
print(f"Subtração: {num1} - {num2} = {subtracao}")
print(f"Multiplicação: {num1} * {num2} = {multiplicacao}")
print(f"Divisão: {num1} / {num2} = {divisao}")
