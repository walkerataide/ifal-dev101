# informar o nome do personagem do Harry Potter
nome = input("Qual seu nome?")

# Verificar qual a casa deste personagem
match nome:
    case "Harry Potter":  # Informar ao usuário qual a casa do personagem
        print("Grifinória")
    case "Hermione Granger":
        print("Grifinória")
    case "Rony Weasley":
        print("Grifinória")
    case "Draco Malfoy":
        print("Sonserina")
    case "Luna Lovegood":
        print("Corvinal")
    case "Cedric Diggory":
        print("Lufa-Lufa")
    case _:
        print("Personagem não encontrado")
