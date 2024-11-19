# informar o nome do personagem do Harry Potter
nome = input("Qual seu nome?")

# Verificar qual a casa deste personagem
match nome.title():
    case "Harry Potter" | "Hermione Granger" | "Rony Weasley":
        print("Grifinória")
    case "Draco Malfoy":
        print("Sonserina")
    case "Luna Lovegood":
        print("Corvinal")
    case "Cedric Diggory":
        print("Lufa-Lufa")
    case _:
        print("Personagem não encontrado")
