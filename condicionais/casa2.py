# informar o nome do personagem do Harry Potter
nome = input("Qual seu nome?")

# Verificar qual a casa deste personagem
if nome == "Harry Potter" or nome == "Hermione Granger" or "Rony Weasley":
    print("Grifinória")
elif nome == "Draco Malfoy":
    print("Sonserina")
elif nome == "Luna Lovegood":
    print("Corvinal")
elif nome == "Cedric Diggory":
    print("Lufa-Lufa")
else:
    print("Personagem não encontrado")
