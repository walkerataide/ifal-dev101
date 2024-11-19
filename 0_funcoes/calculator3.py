# Função principal que será chamada ao executar o programa
def main():
    print("--- Calculadora Exponencial² 🤖 ---")

    # Solicita ao usuário um número e converte para float
    n = float(input("Qual o Número?"))

    # Calcula o quadrado do número e formata o resultado
    result = formatar(calcular_quadrado(n))
    print(f"O quadrado de {formatar(n)} é {result}")

    # Calcula o cubo do número e formata o resultado
    result = formatar(calcular_cubo(n))
    print(f"O cubo de {formatar(n)} é {result}")


# Função que calcula o quadrado de um número
def calcular_quadrado(n):
    return n * n


# Função que calcula o cubo de um número
def calcular_cubo(n):
    return n**3


# Função que formata o número para exibir com separadores de milhar e vírgulas
def formatar(n):
    n = f"{n:_.2f}"  # Formata o número para ter duas casas decimais e separador de milhar
    return n.replace(".", ",").replace(
        "_", "."
    )  # Substitui pontos por vírgulas e sublinhados por pontos


# Chama a função principal para executar o programa
main()
