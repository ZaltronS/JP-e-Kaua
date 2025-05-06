def verifica_categoria(cat, cartela):
   
    numeros = ['1','2','3','4','5','6']
    if cat in numeros:
        cat = int(cat)

    if cat in cartela['regra_simples'] and cartela['regra_simples'][cat] != -1:
        return 1
    
    elif cat in cartela['regra_avancada'] and cartela['regra_avancada'][cat] != -1:
        return 1
    
    elif cat not in cartela['regra_avancada'] and cat not in cartela['regra_simples']:
       return 0
    
from funcoes import *

rol = rolar_dados(5)
guard = []

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

def rodada(cartela, rol, guard):
    cont_rolagem = 0

    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    dec = input()

    while dec != '0':
        
        if dec == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())

            funcao = guardar_dado(rol, guard, indice)
            rol = funcao[0]
            guard = funcao[1]

            print(f'Dados rolados: {rol}')
            print(f'Dados guardados: {guard}')

            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            dec = input()

        elif dec == '2':
            
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())

            funcao = remover_dado(rol, guard, indice)
            rol = funcao[0]
            guard = funcao[1]

            print(f'Dados rolados: {rol}')
            print(f'Dados guardados: {guard}')

            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            dec = input() 


        elif dec == '3':
            if cont_rolagem >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                rol = rolar_dados(len(rol))
                cont_rolagem += 1

            print(f'Dados rolados: {rol}')
            print(f'Dados guardados: {guard}')

            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            dec = input()

        elif dec == '4':
            imprime_cartela(cartela)

            print(f'Dados rolados: {rol}')
            print(f'Dados guardados: {guard}')

            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            dec = input()

        else:
            print("Opção inválida. Tente novamente.")
            dec = input()
        

    dados = rol + guard

    print("Digite a combinação desejada:")
    categoria = input()

    test = verifica_categoria(categoria, cartela)

    while test == 1 or test == 0:
        if test == 1:
            print("Essa combinação já foi utilizada.")
            categoria = input()

        elif test == 0:
            print("Combinação inválida. Tente novamente.")
            categoria = input()
        test = verifica_categoria(categoria, cartela)

    faz_jogada(dados, categoria, cartela)


    return cartela

# Programa principal
cont_rod = 0

imprime_cartela(cartela)
print(f'Dados rolados: {rol}')
print(f'Dados guardados: {guard}')

while cont_rod < 12:
    cartela = rodada(cartela, rol, guard)
    
    rol = rolar_dados(5)
    guard = []

    if cont_rod != 11:
        print(f'Dados rolados: {rol}')
        print(f'Dados guardados: {guard}')
    
    cont_rod += 1

# Cálculo da pontuação final
pont = 0
pontos_regras_simples = 0

for regra, valores in cartela.items():
    for pontos in valores.values():
        pont += pontos
        if regra == 'regra_simples':
            pontos_regras_simples += pontos

if pontos_regras_simples >= 63:
    pont += 35

imprime_cartela(cartela)
print(f"Pontuação total: {pont}")