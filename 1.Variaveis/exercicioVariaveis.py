'''
"Declaro  para  o  senhor  Gonçalves  Dias  que  o  senhor  Humberto  Delgado esteve  presente  no  evento  SecurityCup  e  gastou  o  valor  de  R$  30,00  
com  a entrada."

Identifique  o  que  pode  ser  variável  no  texto  acima  e  monte  um  projeto  no Python,  
em  um  novo  arquivo  chamado  Variaveis2.

No  final,deverá  exibir  o  texto completo  com  o  valor  das  variáveis. Agora,pare,  siga  para  o  PyCharm  e tente resolver!

'''

responsavel = input("Digite o nome do responsável: ")
participante = input("Digite o nome do participante: ")
evento = input("Digite o nome do evento: ")
valorGasto = float(input("Digite o valor gasto no evento: "))

print("Declaro para o senhor " + responsavel + " que o senhor " + participante + " esteve presente no evento " + evento + " e gastou o valor de R$ " + str(valorGasto) + " com a entrada!")
