def main():
    print("--- Calculadora Exponencial² 🤖 ---")
    n = float(input("Qual o Número?"))
    result = formatar(calcular_quadrado(n))
    print(f"O quadrado de {formatar(n)} é {result}")
    result = formatar(calcular_cubo(n))
    print(f"O cubo de {formatar(n)} é {result}")

def calcular_quadrado(n):
    return n * n

def calcular_cubo(n):
    return n**3

def formatar(n):
    n = f"{n:_.2f}"
    return n.replace(".", ",").replace("_", ".")

main()