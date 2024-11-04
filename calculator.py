# Pegar os valores do usuário como float
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

# Operador de Soma
print(f"A soma de {x} + {y} é {x + y}")

# Operador de Subtração
print(f"A subtração de {x} - {y} é {x - y}")

# Operador de Multiplicação
print(f"A multiplicação de {x} * {y} é {x * y}")

# Operador de Divisão com arredondamento para 2 casas decimais
print(
    f"A divisão de {x} / {y} é {round(x / y, 2)}"
)  # round() arredonda o valor para o número de casas decimais especificado

# Operador de Módulo (resto da divisão)
print(f"O resto de {x} % {y} é {x % y}")
