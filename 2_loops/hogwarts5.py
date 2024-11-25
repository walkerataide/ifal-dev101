estudantes = [
    {"nome": "Hermione", "casa": "Grifinória", "patrono": "Lontra"},
    {"nome": "Harry", "casa": "Grifinória", "patrono": "Veado"},
    {"nome": "Rony", "casa": "Grifinória", "patrono": "Jack Russell terrier"},
    {"nome": "Draco", "casa": "Sonserina", "patrono": None},
]

for estudante in estudantes:
    print(estudante["nome"], estudante["casa"], estudante["patrono"], sep=", ")
