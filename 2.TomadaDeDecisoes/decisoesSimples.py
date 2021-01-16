nome = input("Diite o nome: ")
idade = int(input("DIgite a idade: "))
prioridade = "NÃO"

if idade>65:
    prioridade = "SIM"
print("O paciente "+ nome + " possui prioridade? " + prioridade)