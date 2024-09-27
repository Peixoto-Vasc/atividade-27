# Solicite ao usuário que insira o nome de até 7 convidados.
# Armazene os nomes em uma lista.
# Permita ao usuário remover um convidado da lista, caso necessário.
# Exiba a lista final de convidados.

# Digite o nome do convidado 1: João
# Digite o nome do convidado 2: Maria
# ...
# Digite o nome do convidado 7: Pedro
# Deseja remover algum convidado da lista? (sim/não): sim
# Digite o nome do convidado a ser removido: Maria
convidado=[]
for i in range(7):
    convidados=(input(f"digite o numero do convidado {i+1}"))
    convidado.append(convidados)
    
    

pergunta=(input(f"deseja remover digite sim ou nao:"))
if pergunta == "sim":
    remov= str(input("qual nome voce que remover?"))
    convidado.remove(remov)
    print(convidado)
else:
    print("beleza") 