import random


def rolar_dados(num):
    i = 0
    lista = []
    while i < num :
        x = random.randint(1,6)
        lista.append(x)
        i+= 1
    return lista
# print (rolar_dados(5))


def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    novos_dados_rolados = []
    for i in range(len(dados_rolados)):
        if i != dado_para_guardar:
            novos_dados_rolados.append(dados_rolados[i])
        else:
            dado = dados_rolados[i]
            dados_no_estoque.append(dado)
    return [novos_dados_rolados, dados_no_estoque]
# dados_rolados = [1, 3, 2]
# dados_no_estoque = [1, 2]
# dado_para_guardar = 1
# resultado = guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar)
# print(resultado)


def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    novo_estoque = []
    for i in range(len(dados_no_estoque)):
        if i != dado_para_remover:
            novo_estoque.append(dados_no_estoque[i])
        else:
            dado = dados_no_estoque[i]
            dados_rolados.append(dado)
    return [dados_rolados, novo_estoque]
# dados_rolados = [2, 2, 2, 2]
# dados_no_estoque = [1]
# teste = 0

# print(remover_dado(dados_rolados, dados_no_estoque, teste))


