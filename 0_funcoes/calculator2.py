# Solicita os valores do usuário como float
base = float(input("Digite o primeiro número: "))
expoente = float(input("Digite o segundo número: "))

# Calcula a potência (base elevada ao expoente)
resultado = base**expoente

# Formata o resultado para ter duas casas decimais e substitui pontos por vírgulas
resultado = (
    f"{resultado:_.2f}"  # Formatação com separador de milhar e duas casas decimais
)
resultado = resultado.replace(".", ",").replace("_", ".")

# Exibe o resultado formatado
print(f"{base} elevado ao {expoente} é {resultado}")
