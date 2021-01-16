nome = input("Digite o nome ")
empresa = input("Digite a empresa: ")
qtde_funcionarios = int(input("Digite a quantidade de funcionários: "))
mediaSalario = float(input("Digite a média de salarial: "))

print (nome + "Trabalha na empresa: " + empresa)
print("A empresa possui cerca de: ", qtde_funcionarios, " funcionários")
print("A média salarial é de: " + str(mediaSalario))

print("=============Tipos de dados==============")
print("O tipo de dado da variavel [nome]", type(nome))
print("O tipo de dado da variavel [empresa]", type(empresa))
print("O tipo de dado da variavel [qtde_funcionarios]", type(qtde_funcionarios))
print("O tipo de dado da variavel [mediaSalario]", type(mediaSalario))

