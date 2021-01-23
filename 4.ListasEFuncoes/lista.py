inventario =[]
resposta = "S"

while resposta == "S":
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número Serial: ")))
    inventario.append(input("Departamento: "))

    for elemento in inventario:
        print(elemento)

    resposta = input("Digite \"S\" para continuar: ").upper()