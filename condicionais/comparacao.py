x = int(input("Qual o x?"))
y = int(input("Qual o y?"))

if x < y:
    print("x é menor que y")
elif x > y:
    print("x é maior que y")
    if x > 100:
        print("x é maior que 100!")
    elif x < 100:
        print("x é menor que 100...")
    else:
        print("x é igual a 100 😊")
else:
    print("x é igual a y")
