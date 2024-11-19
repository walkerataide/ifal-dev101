# ENTRADA
# solicitar a pontuação do aluno
pontos = int(input("Pontos: "))

# PROCESSAMENTO
# verificar qual a nota do aluno com base na pontuação
if pontos >= 90:
    print("A")  # SAÍDA - exibir a nota para o usuário
elif pontos >= 80:
    print("B")
elif pontos >= 70:
    print("C")
elif pontos >= 60:
    print("D")
else:
    print("F")
