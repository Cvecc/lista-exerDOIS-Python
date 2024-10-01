print("Clara Vecchio Machado da Silva\nRA: 1051392421023 \nDSM - 1°Semestre\n")

# Solicita ao usuário a altura
altura = float(input("Digite a altura da pessoa (em metros): "))

# Solicita ao usuário o sexo da pessoa
sexo = input("Digite o sexo da pessoa (homem/mulher): ").strip().lower()

# Calcula o peso ideal com base no sexo
if sexo == "homem":
    peso_ideal = (72.7 * altura) - 58
elif sexo == "mulher":
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = None
    print("Sexo inválido. Por favor, insira 'homem' ou 'mulher'.")

# Exibe o peso ideal, se o sexo for válido
if peso_ideal is not None:
    print(f"O peso ideal para uma pessoa de sexo {sexo} e altura {altura:.2f} m é: {peso_ideal:.2f} kg")
