texto = "Olá, Mundo! Olá IFAL MD!"

# Conta quantas vezes "olá, mundo" aparece no texto (case insensitive)
print(texto.lower().count("olá, mundo"))

# Encontra a posição de "mundo" no texto (case insensitive)
print(texto.lower().find("mundo"))

# Capitaliza a primeira palavra do texto e substitui "mundo" por "IFAL"
texto = texto.capitalize().replace("mundo", "IFAL")
print(texto)

# Solicita o nome do usuário
nome = input("Qual seu nome e último nome?")

# Coloca cada parte do nome com a primeira letra maiúscula
nome = nome.title().split()
nome = " ".join(nome)

# Separa o primeiro nome e o sobrenome
primeiro_nome, sobrenome = nome.split()
print(f"Olá, {nome}")
print(f"Olá, {primeiro_nome} {sobrenome}")

# Remove espaços desnecessários antes e depois do nome (várias formas de fazer isso)
print(nome.strip(), end="")  # Remove espaços antes e depois
print(nome.rstrip(), end="")  # Remove espaços depois
print(nome.lstrip())  # Remove espaços antes

# Diferentes maneiras de formatar o nome
print(nome.title())  # Cada palavra com a primeira letra maiúscula
print(nome.capitalize())  # Apenas a primeira palavra com a primeira letra maiúscula
print(nome.upper())  # Todas as letras maiúsculas
print(nome.lower())  # Todas as letras minúsculas
