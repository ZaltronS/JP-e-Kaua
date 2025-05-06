import random

def rolar_dados(num):
    lista = []
    for _ in range(num):
        lista.append(random.randint(1, 6))
    return lista

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    novos_dados_rolados = []
    for i in range(len(dados_rolados)):
        if i != dado_para_guardar:
            novos_dados_rolados.append(dados_rolados[i])
        else:
            dados_no_estoque.append(dados_rolados[i])
    return [novos_dados_rolados, dados_no_estoque]

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    novo_estoque = []
    for i in range(len(dados_no_estoque)):
        if i != dado_para_remover:
            novo_estoque.append(dados_no_estoque[i])
        else:
            dados_rolados.append(dados_no_estoque[i])
    return [dados_rolados, novo_estoque]

def calcula_pontos_regra_simples(lista):
    dic = {i: 0 for i in range(1, 7)}
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
    if all(x in valores_d for x in [1, 2, 3, 4]):
        return 15
    if all(x in valores_d for x in [2, 3, 4, 5]):
        return 15
    if all(x in valores_d for x in [3, 4, 5, 6]):
        return 15
    return 0

def calcula_pontos_sequencia_alta(dados):
    valores_d = []
    for valor in dados:
        if valor not in valores_d:
            valores_d.append(valor)
    if all(x in valores_d for x in [1, 2, 3, 4, 5]):
        return 30
    if all(x in valores_d for x in [2, 3, 4, 5, 6]):
        return 30
    return 0

def calcula_pontos_full_house(lista):
    contagem = {}
    for x in lista:
        if x not in contagem:
            contagem[x] = 1
        else:
            contagem[x] += 1
    if sorted(contagem.values()) == [2, 3]:
        return sum(lista)
    return 0

def calcula_pontos_quadra(dados):
    for i in dados:
        repeticoes = 0
        for j in dados:
            if i == j:
                repeticoes += 1
        if repeticoes >= 4:
            return sum(dados)
    return 0

def calcula_pontos_quina(dados):
    for i in dados:
        repeticoes = 0
        for j in dados:
            if i == j:
                repeticoes += 1
        if repeticoes >= 5:
            return 50
    return 0

def calcula_pontos_regra_avancada(lista):
    return {
        'cinco_iguais': calcula_pontos_quina(lista),
        'full_house': calcula_pontos_full_house(lista),
        'quadra': calcula_pontos_quadra(lista),
        'sem_combinacao': calcula_pontos_soma(lista),
        'sequencia_alta': calcula_pontos_sequencia_alta(lista),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(lista)
    }

def faz_jogada(lista, stg, dic):
    simples = calcula_pontos_regra_simples(lista)
    avancado = calcula_pontos_regra_avancada(lista)

    if stg in dic['regra_avancada']:
        dic['regra_avancada'][stg] = avancado[stg]
    elif stg.isdigit():
        numero = int(stg)
        if numero in dic['regra_simples']:
            dic['regra_simples'][numero] = simples[numero]
    return dic

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-" * 25)

    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}:{filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}:{filler}|    |")

    for chave in ['sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']:
        filler = " " * (15 - len(str(chave)))
        if cartela['regra_avancada'][chave] != -1:
            print(f"| {chave}:{filler}| {cartela['regra_avancada'][chave]:02} |")
        else:
            print(f"| {chave}:{filler}|    |")

    print("-" * 25)

# Chamada automática de teste para o Prairie Learn
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
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

imprime_cartela(cartela_exemplo)
