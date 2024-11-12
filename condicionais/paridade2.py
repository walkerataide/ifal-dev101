def main():
    # solicitar o número
    num = int(input("Digite um número: "))
    # verificar se é par
    if eh_par(num):
        print("par")  # exibir o resultado
    else:
        print("ímpar")

def eh_par(num):
    if num % 2 == 0:
        return True
    else:
        return False


main()
