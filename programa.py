from funcoes import (
    rolar_dados,
    guardar_dado,
    remover_dado,
    calcula_pontos_regra_simples,
    calcula_pontos_regra_avancada,
    faz_jogada,
    imprime_cartela
)

#programa 13:

def main():
    cartela = {
        'regra_simples': {i: -1 for i in range(1, 7)},
        'regra_avancada': {
            'sem_combinacao': -1,
            'sequencia_baixa': -1,
            'sequencia_alta': -1,
            'full_house': -1,
            'quadra': -1,
            'cinco_iguais': -1
        }
    }

    for rodada in range(12):
        dados_rolados = rolar_dados(5)
        dados_guardados = []
        rerrolagens = 0

        while True:
            print(f"\nDados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            escolha = input()

            if escolha == "1":
                print("Digite o índice do dado a ser guardado (0 a 4):")
                indice = int(input())
                if 0 <= indice < len(dados_rolados):
                    resultado = guardar_dado(dados_rolados, dados_guardados, indice)
                    dados_rolados, dados_guardados = resultado

            elif escolha == "2":
                print("Digite o índice do dado a ser removido (0 a 4):")
                indice = int(input())
                if 0 <= indice < len(dados_guardados):
                    resultado = remover_dado(dados_rolados, dados_guardados, indice)
                    dados_rolados, dados_guardados = resultado

            elif escolha == "3":
                if rerrolagens < 2:
                    quantidade = 5 - len(dados_guardados)
                    dados_rolados = rolar_dados(quantidade)
                    rerrolagens += 1
                else:
                    print("Você já usou todas as rerrolagens.")

            elif escolha == "4":
                imprime_cartela(cartela)

            elif escolha == "0":
                print("Digite a combinação desejada:")
                categoria = input()
                if categoria.isdigit():
                    categoria = int(categoria)
                    if categoria in cartela["regra_simples"]:
                        if cartela["regra_simples"][categoria] == -1:
                            cartela = faz_jogada(dados_guardados + dados_rolados, str(categoria), cartela)
                            break
                        else:
                            print("Essa combinação já foi utilizada.")
                    else:
                        print("Combinação inválida. Tente novamente.")
                elif categoria in cartela["regra_avancada"]:
                    if cartela["regra_avancada"][categoria] == -1:
                        cartela = faz_jogada(dados_guardados + dados_rolados, categoria, cartela)
                        break
                    else:
                        print("Essa combinação já foi utilizada.")
                else:
                    print("Combinação inválida. Tente novamente.")
            else:
                print("Opção inválida. Tente novamente.")

    # Fim do jogo: soma pontuação
    imprime_cartela(cartela)

    total = 0
    soma_simples = 0

    for valor in cartela["regra_simples"].values():
        if valor != -1:
            total += valor
            soma_simples += valor

    for valor in cartela["regra_avancada"].values():
        if valor != -1:
            total += valor

    if soma_simples >= 63:
        total += 35

    print(f"Pontuação total: {total}")

if __name__ == "__main__":
    main()