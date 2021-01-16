nome = input("Diite o nome: ")
idade = int(input("DIgite a idade: "))
doenca_infectocontagiosta = input("Suspeita de doença infecto-contagiosa? ").upper()

if idade>=65 and doenca_infectocontagiosta == "SIM":
    print("O paciente "+ nome + " será direcionado para a sala Amarela - COM prioridade")
elif idade <65 and doenca_infectocontagiosta=="SIM":
    print("O paciente "+ nome + " será direcionado para a sala Amarela - SEM prioridade")
elif idade >=65 and doenca_infectocontagiosta == "NAO":
    print("O paciente "+ nome + " será direcionado para a sala Branca - COM prioridade")
elif idade <65 and doenca_infectocontagiosta == "NAO":
    print("O paciente "+ nome + " será direcionado para a sala Branca - SEM prioridade")
else:
    print("Responda a suspeita de doença infectocontagiosa")