a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

if a > b:
    print("O maior número é", a)
else:
    if b > a:
        print("O maior número é", b)
    else:
        print("Os dois números são iguais")
