import random
#função para mostrar o mapa e onde esta todos os jogadores :)
def printmap(jogadores, movimentos, metros, tesouros):  
    # mapa como uma lista vazia
    mapa =[]
    
    #para cada posição do mapa se adiciona uma lista(para pode mostra mais de um jogador em uma mesma posição)
    for _ in range(metros+1):
        mapa.append([])
    
    
    # Atribui jogadores às suas respectivas posições no mapa(utilizando a lista movimentos(guarda o valor de onde ele ta)e se usa um enumarete para sabemos em qual indice(jogador) da lista movimento e o valor desse indice(posição desse jogador))
    for i, pos in enumerate(movimentos):
        if 0 <= pos <= metros:
            mapa[pos].append(jogadores[i])  # Adiciona o jogador à lista na posição correspondente do mapa
    
    # Imprime o mapa com jogadores e tesouros
    for i in range(len(mapa)):
        jogadores_na_posicao = ", ".join(mapa[i])
        print(f"{tesouros[i]}-  [{jogadores_na_posicao}]  - {i} metros")
    print()
    print()


#função para decidir quem ganhou o jogo :)
def vencedor(inventario_submarino):
    maior = 0 
    nome_maior = ""
    for nome in inventario_submarino:
        valor = inventario_submarino[nome]
        if valor > maior:
            maior = valor
            nome_maior = nome
    return nome_maior , maior

#função para verificar as possiveis posições dos jogadore no mapa:)
def verifica_posição(movimentos, nova_posicao, metros, i):
    if nova_posicao != 0 :
        if nova_posicao < 0:
            movimentos[i] = 0  # aqui verificamos para manter sempre os jogadores presentes no mapa e se nova posicao for menor que zero ele vai ir para o ponto mais baixo
        elif nova_posicao > metros:
            movimentos[i] = metros # aqui rola a mesma coisa que a parte de cima somente mudamos para se ele tentar passar do mapa automaticamente ele ira ir para o ponto mais alto
        else:
            movimentos[i] = nova_posicao # se ele n entra em nenhum outro if a posição seguira normalmente
    else:
        nova_posicao = 0
    return movimentos[i]

#função para guarda tesouro :)
def guarda(inventario_submarino,chave_sub,inventario_geral,chave_invent):
    inventario_submarino[chave_sub] += inventario_geral[chave_invent]
    inventario_geral[chave_invent] = 0

#função para inicializar o mapa e lista dos movimentos dos jogadores :)
def map_list(quantidade):
    
    jogadores = [] #aqui ta meio confuso mas vou tenta explicar jogadores é uma lista de jogadores onde teriamos ex jogadores[0]= jogador 1 e etc
    
    
    for i in range(quantidade):
        jogadores.append(f"J{i+1}")
    movimentos = [0] * quantidade  # aqui é lista onde vamos guardar o a posição em que os jogadores estão posicionados movimento[0] = 10 então o  jogador 0(jogador 1) esta na posição da lista 10 é util guarda essa lista para verificar algumas coisas futuras como a trick de pular um jogador em que ja esta em uma casa
    
    return jogadores, movimentos

#função para inicializar o mapa dos tesouros e seus calculos :)
def bau(metros):
    tesouros = ["$"]*(metros+1) # definimos a lista de tesouros
    um_terco = (metros + 1) // 3 # um calculo basico para vermos qual indice do mapa é menor que um terco um terco ou maior que 
    for i in range(len(tesouros)):
        if i == 0:
            tesouros[i] = "[Submarino]"
        elif i < um_terco:
            tesouros[i] = "$          "
        elif i < 2 * um_terco:
            tesouros[i] = "$$         "
        else:
            tesouros[i] = "$$$        "
    return tesouros

#função de pega do tesouro :)
def pegar(tesouros,movimentos,i,inventario_geral,chave):
    if tesouros[movimentos[i]] == "$          ":
        # adiciona o valor ao inventário existente
        inventario_geral[chave] += 1
        tesouros[movimentos[i]] = "X          "
        
                
    elif tesouros[movimentos[i]] == "$$         ":
        inventario_geral[chave] += 2
        tesouros[movimentos[i]] = "X          "
        
                
    elif tesouros[movimentos[i]] == "$$$        ":
        inventario_geral[chave] += 4
        tesouros[movimentos[i]] = "X          "
        
                
    elif tesouros[movimentos[i]] == "X          ":
        print("Nesta casa não tinha tesouro")

# função para definir a mochila/inventario dos jogadores :)
def mochila(quantidade):
    inventario_geral = {}
    for i in range(quantidade):
        chave = (f"mochila_do_jogador_{i+1}")
        valor = 0
        inventario_geral[chave] = valor
    return inventario_geral

#submarino inventario(cria o inventario de cada jogador no submarino ):)
def submarino(quantidade):
    submarino_inven = {}
    for i in range(quantidade):
        chave = (f"submarino_do_jogador{i+1}")
        valor = 0
        submarino_inven[chave] = valor
    return submarino_inven

# perguntas e algumas verificações sobre o jogo para balancear ele :)
def decisão(tesouros,movimentos,i,jogadores,inventario_geral,chave):
    p = 0
    if tesouros[movimentos[i]] == "X          ": #se na casa em que o jogador pois para pegar o tesouro for X ele n podera pega nada e nem perde o turno ent vai pergunta ate ele decidi algo valido
        while p == 0:
            decisao = int(input(f"Jogador {jogadores[i]}, escolha: 1 para avançar, 2 para recuar, 3 para pegar o tesouro, 4 para passar a vez: "))
            if decisao == 3:
                print("não tem tesouros nessa casa")
            elif decisao not in [1,2,3,4]:
                print("coloque um numero valido")
            else:
                 p += 1
    elif tesouros[movimentos[i]] == "[Submarino]": #aqui o jogador teria a opção de guarda os tesouros que ele tem, porem se ele n tiver nada ou querer pega algum tesouro na casa do submarino, o progama vai pergunta ate ele desejar algo valido
        while p == 0:
            decisao = int(input(f"Jogador {jogadores[i]}, escolha: 1 para avançar, 2 para recuar, 3 para pegar o tesouro, 4 para passar a vez,5 para guarda os tesouros no submarino: "))
            if decisao == 3:
                print("não tem tesouros nessa casa")
            elif decisao == 5 and inventario_geral[chave] == 0:
                    print("voce não tem tesouros para guarda")
            elif decisao not in [1,2,3,4,5]:
                print("coloque um numero valido")
            else:
                p += 1
    else:
        while p == 0:
            decisao = int(input(f"Jogador {jogadores[i]}, escolha: 1 para avançar, 2 para recuar, 3 para pegar o tesouro, 4 para passar a vez: "))
            if decisao not in [1,2,3,4]:
                print("coloque um numero valido")
            else:
                p += 1

    return decisao
# função para gerar uma nova posição
def gerar_novaposicao(decisao,movimentos,i):
    movimento = random.randint(0, 3)
    if decisao == 1:
        nova_posicao = movimentos[i] + movimento
    elif decisao == 2:
        nova_posicao = movimentos[i] - movimento
    return movimento, nova_posicao
#gastar tanques :)
def gasto(movimento, tanques,inventario_geral,chave_invent,movimentos,nova_posiçao,i):
    if nova_posiçao == movimentos[i] and movimento != 0:
        tanques_gastos = inventario_geral[chave_invent]+1
        tanques -= tanques_gastos
    return tanques    
#função para recolher os dados que o jogador deseja ex tanques quantos jogadores e etc :)
def dados():
    quantidade = 0
    while quantidade not in [4, 5, 6]:
            quantidade = int(
                input('Escolha quantos jogadores irão jogar, entre 4 e 6: '))
            if quantidade in [4, 5, 6]:
                print(f"Então teremos {quantidade} de jogadores")
                # termina o while apos a escolha de quantidade de jogadores
            else:
                print("invalido, escolha um numero entre as opções")

        # verificar metros
    metros = 0
    while metros not in [15, 30, 45]:
            metros = int(input('O mapa pode ter 15, 30 ou 45 metros de profundidade, qual deseja?'))
            if metros in [15, 30, 45]:
                print(f"Então o mapa tera {metros}m")
                # termina o while apos a escolha
            else:
                print("invalido, escolha um numero entre as opções")

        # verificar quantidade de tanques
    tanques = 0
    while not 45 <= tanques <= 120:
            tanques = int(input('Escolha quantos tanques terão: entre 45 a 120: '))
            if 45<= tanques <= 120:
                print(f"Foi escolhido {tanques} tanques")
            else:
                print('invalido, escolha um numero entre as opções')

    return quantidade, metros, tanques