# ENTRADA
# solicitar a pontuação do aluno
pontos = int(input("Pontos: "))

# PROCESSAMENTO
# verificar qual a nota do aluno com base na pontuação
if 90 <= pontos <= 100:
    print("A")  # SAÍDA - exibir a nota para o usuário
elif 80 <= pontos < 90:
    print("B")
elif 70 <= pontos < 80:
    print("C")
elif 60 <= pontos < 70:
    print("D")
else:
    print("F")
