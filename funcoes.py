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
# print(remover_dado(dados_rolados, dados_no_estoque, teste)

def calcula_pontos_regra_simples(lista):
    dic = {1:0, 2:0, 3:0 , 4:0, 5:0, 6:0}
    for n in lista:
        if 1<= n <= 6 :
            dic[n] += n
    return dic

def calcula_pontos_soma(dados):
    soma = 0
    for valor in dados:
        soma+= valor
    return soma
# print(calcula_pontos_soma([2, 3, 4, 5, 2]))
def calcula_pontos_sequencia_baixa(dados):
    valores_d = []
    for valor in dados:
        if valor not in valores_d:
            valores_d.append(valor)

    if 1 in valores_d and 2 in valores_d and 3 in valores_d and 4 in valores_d:
        return 15
    if 2 in valores_d and 3 in valores_d and 4 in valores_d and 5 in valores_d:
        return 15
    if 3 in valores_d and 4 in valores_d and 5 in valores_d and 6 in valores_d:
        return 15

    return 0

def calcula_pontos_sequencia_alta(dados):
    valores_d = []
    for valor in dados:
        if valor not in valores_d:
            valores_d.append(valor)

    if 1 in valores_d and 2 in valores_d and 3 in valores_d and 4 in valores_d and 5 in valores_d:
        return 30
    if 2 in valores_d and 3 in valores_d and 4 in valores_d and 5 in valores_d and 6 in valores_d:
        return 30

    return 0


def calcula_pontos_full_house (lista):
    dicionario = {1:0, 2:0, 3:0, 4:0,5:0, 6 :0 }
    somadados = 0
    for x in lista:
        dicionario[x] +=1
    if 3 in dicionario.values() and 2 in dicionario.values() :
        for y in lista :
            somadados += y
        return somadados
    else:
        return 0


def calcula_pontos_quadra(dados):
    valores_d = []
    for valor in dados:
        if valor not in valores_d:  #uso not in
            valores_d.append(valor)

    for i in valores_d:
        repeticoes = 0
        for j in dados:
            if j == i:
                repeticoes += 1
        if repeticoes >= 4:
            soma = 0
            for n in dados:
                soma += n
            return soma

    return 0

def calcula_pontos_quina(lista):
    listanumeros = [1,2,3,4,5,6]
    for numeros in listanumeros:
        soma = 0
        for num in lista:
            if num == numeros:
                soma += 1 
        if soma >= 5:
            return 50
    return 0
  

