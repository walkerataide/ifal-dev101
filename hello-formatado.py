# Solicita ao usuário que digite seu nome
nome = input("Qual seu nome?")

# Solicita ao usuário que digite sua turma
turma = input("Qual sua turma?")

# Utilizando f-string para concatenar strings
print(f"Olá {nome} da turma {turma}")

# Utilizando múltiplos parâmetros na função print
print("Olá", nome, "da turma", turma)

# Utilizando o operador de concatenação (+) para juntar strings
print("Olá" + nome + "da turma" + turma)
