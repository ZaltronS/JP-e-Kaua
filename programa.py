def verifica_categoria(categoria, cartela):
    numeros = ['1','2','3','4','5','6']
    if categoria in numeros:
        categoria = int(categoria)

    if categoria in cartela['regra_simples'] and cartela['regra_simples'][categoria] != -1:
        return 1
    
    elif categoria in cartela['regra_avancada'] and cartela['regra_avancada'][categoria] != -1:
        return 1
    
    elif categoria not in cartela['regra_avancada'] and categoria not in cartela['regra_simples']:
        return 0

from funcoes import *

dados_rolados = rolar_dados(5)
dados_guardados = []

cartela = {
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

def rodada(cartela, dados_rolados, dados_guardados):
    contagem_rolagens = 0

    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    decisao = input()

    while decisao != '0':
        
        if decisao == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())

            resultado = guardar_dado(dados_rolados, dados_guardados, indice)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]

            print(f'Dados rolados: {dados_rolados}')
            print(f'Dados guardados: {dados_guardados}')

        elif decisao == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())

            resultado = remover_dado(dados_rolados, dados_guardados, indice)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]

            print(f'Dados rolados: {dados_rolados}')
            print(f'Dados guardados: {dados_guardados}')

        elif decisao == '3':
            if contagem_rolagens >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados_rolados = rolar_dados(len(dados_rolados))
                contagem_rolagens += 1

            print(f'Dados rolados: {dados_rolados}')
            print(f'Dados guardados: {dados_guardados}')

        elif decisao == '4':
            imprime_cartela(cartela)
            print(f'Dados rolados: {dados_rolados}')
            print(f'Dados guardados: {dados_guardados}')

        else:
            print("Opção inválida. Tente novamente.")

        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        decisao = input()
        
    dados_finais = dados_rolados + dados_guardados

    print("Digite a combinação desejada:")
    categoria = input()

    validacao = verifica_categoria(categoria, cartela)

    while validacao == 1 or validacao == 0:
        if validacao == 1:
            print("Essa combinação já foi utilizada.")
        elif validacao == 0:
            print("Combinação inválida. Tente novamente.")
        categoria = input()
        validacao = verifica_categoria(categoria, cartela)

    faz_jogada(dados_finais, categoria, cartela)

    return cartela

# Programa principal
rodada_atual = 0

imprime_cartela(cartela)
print(f'Dados rolados: {dados_rolados}')
print(f'Dados guardados: {dados_guardados}')

while rodada_atual < 12:
    cartela = rodada(cartela, dados_rolados, dados_guardados)
    
    dados_rolados = rolar_dados(5)
    dados_guardados = []

    if rodada_atual != 11:
        print(f'Dados rolados: {dados_rolados}')
        print(f'Dados guardados: {dados_guardados}')
    
    rodada_atual += 1

# Cálculo da pontuação final
pontuacao_total = 0
pontos_regras_simples = 0

for tipo, valores in cartela.items():
    for pontos in valores.values():
        pontuacao_total += pontos
        if tipo == 'regra_simples':
            pontos_regras_simples += pontos

if pontos_regras_simples >= 63:
    pontuacao_total += 35

imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao_total}")
