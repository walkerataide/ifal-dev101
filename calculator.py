# Pegar os valores do usuário
base = float(input("digite o primeiro número: "))
expoente = float(input("digite o segundo número: "))

# Calcula e Exibe o resultado
resultado = base**expoente
resultado = f"{resultado:_.2f}"
resultado = resultado.replace(".", ",").replace("_", ".")
print(f"{base} elevado ao {expoente} é {resultado}")



'''
# Pegar os valores do usuário
x = float(input("digite o primeiro número: "))
y = float(input("digite o segundo número: "))

print(f"A soma de {x} + {y} é {x + y}")
print(f"A subtração de {x} + {y} é {x - y}")
print(f"A multiplicação de {x} + {y} é {x * y}")
print(f"A divisão de {x} + {y} é {round(x / y,2)}")# round() arredonda o valor para o inteiro mais próximo
print(f"O resto de {x} + {y} é {x % y}")
'''