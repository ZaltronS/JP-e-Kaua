import random
def rolar_dados(num):
    i = 0
    lista = []
    while i < num :
        x = random.randint(1,6)
        lista.append(x)
        i+= 1
    return lista
def guardar_dado(dados,armaz,numero):
    armaz.append(dados[numero])
    dados.pop(numero)
    return[dados,armaz]


