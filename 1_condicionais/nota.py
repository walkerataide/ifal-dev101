# ENTRADA
# solicitar a pontuação do aluno
pontos = int(input("Pontos: "))

# PROCESSAMENTO
# verificar qual a nota do aluno com base na pontuação
if pontos >= 90 and pontos <= 100:
    print("A")  # SAÍDA - exibir a nota para o usuário
elif pontos >= 80 and pontos < 90:
    print("B")
elif pontos >= 70 and pontos < 80:
    print("C")
elif pontos >= 60 and pontos < 70:
    print("D")
else:
    print("F")
