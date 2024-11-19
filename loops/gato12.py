while True:
    miaus = int(input("Quantas vezes o gato deve miar? "))
    if miaus > 0:
        break

for _ in range(miaus):
    print("😽 miau")
