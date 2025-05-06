import random

def rolar_dados(num):
    i = 0
    lista = []
    while i < num:
        x = random.randint(1, 6)
        lista.append(x)
        i += 1
    return lista

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    novos_dados_rolados = []
    for i in range(len(dados_rolados)):
        if i != dado_para_guardar:
            novos_dados_rolados.append(dados_rolados[i])
        else:
            dado = dados_rolados[i]
            dados_no_estoque.append(dado)
    return [novos_dados_rolados, dados_no_estoque]

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    novo_estoque = []
    for i in range(len(dados_no_estoque)):
        if i != dado_para_remover:
            novo_estoque.append(dados_no_estoque[i])
        else:
            dado = dados_no_estoque[i]
            dados_rolados.append(dado)
    return [dados_rolados, novo_estoque]

def calcula_pontos_regra_simples(lista):
    dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for n in lista:
        if 1 <= n <= 6:
            dic[n] += n
    return dic

def calcula_pontos_soma(dados):
    soma = 0
    for valor in dados:
        soma += valor
    return soma

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

def calcula_pontos_full_house(lista):
    dicionario = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    somadados = 0
    for x in lista:
        dicionario[x] += 1
    if 3 in dicionario.values() and 2 in dicionario.values():
        for y in lista:
            somadados += y
        return somadados
    else:
        return 0

def calcula_pontos_quadra(dados):
    valores_d = []
    for valor in dados:
        if valor not in valores_d:
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
    listanumeros = [1, 2, 3, 4, 5, 6]
    for numeros in listanumeros:
        soma = 0
        for num in lista:
            if num == numeros:
                soma += 1
        if soma >= 5:
            return 50
    return 0

def calcula_pontos_regra_avancada(lista):
    pontos = {
        'cinco_iguais': 0,
        'full_house': 0,
        'quadra': 0,
        'sem_combinacao': 0,
        'sequencia_alta': 0,
        'sequencia_baixa': 0
    }
    pontos['cinco_iguais'] = calcula_pontos_quina(lista)
    pontos['full_house'] = calcula_pontos_full_house(lista)
    pontos['quadra'] = calcula_pontos_quadra(lista)
    pontos['sequencia_alta'] = calcula_pontos_sequencia_alta(lista)
    pontos['sequencia_baixa'] = calcula_pontos_sequencia_baixa(lista)
    pontos['sem_combinacao'] = calcula_pontos_soma(lista)
    return pontos

def faz_jogada(lista, stg, dic):
    pontossimples = calcula_pontos_regra_simples(lista)
    pontosavancado = calcula_pontos_regra_avancada(lista)

    for i, j in pontosavancado.items():
        if i == stg:
            dic['regra_avancada'][i] = j

    for x, y in pontossimples.items():
        if str(x) == stg:
            dic['regra_simples'][x] = y
    return dic

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-" * 25)

    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"{i}:{filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"{i}:{filler}|    |")

    for chave in cartela['regra_avancada']:
        filler = " " * (15 - len(str(chave)))
        if cartela['regra_avancada'][chave] != -1:
            print(f"{chave}:{filler}| {cartela['regra_avancada'][chave]:02} |")
        else:
            print(f"{chave}:{filler}|    |")

    print("-" * 25)

# CHAMADA FINAL PARA O PRAIRIE LEARN – exercício 13
cartela_exemplo = {
    'regra_simples': {
        1: -1,
        2: -1,
        3: -1,
        4: -1,
        5: -1,
        6: -1
    },
    'regra_avancada': {
        'sem_combinacao': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'full_house': -1,
        'quadra': -1,
        'cinco_iguais': -1
    }
}

imprime_cartela(cartela_exemplo)
