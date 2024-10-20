from utilidades_pbl import *
import random
print('Olá sejam Bem-vindos!\n\nAs regras são os seguintes:\nO jogo é projetado para 4 a 6 jogadores.\nO mapa pode ter 15, 30 ou 45 metros de profundidade, escolhido antes do início da partida.\nO tesouro inicial pesa 1kg e dobra a cada ⅓ de profundidade. Por exemplo, em um mapa de 15 metros, os primeiros 5 tesouros valem 1kg, os próximos 5 valem 2kg e os últimos valem 4kg.\nA quantidade de oxigênio varia de 45 a 120 tanques, determinada pelo usuário.\nO consumo de oxigênio é calculado em uma unidade a mais do que o peso em kg dos tesouros carregados pelo mergulhador. Por exemplo, um mergulhador com 15kg de tesouro gastará 16 tanques de oxigênio por turno.\nOs mergulhadores se movem de 0 a 3 unidades de movimento\nOs jogadores podem escolher capturar ou não os tesouros.\nUm mergulhador não pode pegar um tesouro já capturado por outro.\nOs tesouros podem ser depositados no submarino para reduzir o consumo de oxigênio.\nUm mergulhador pode carregar mais de um tesouro consigo.\nO ganhador sera decidido pela quantidade de tanques no submarino.\nÉ possivel passar a vez se necessario.\nQuando o numero de tanques chega a 0 o jogo acabara imediatamente.\n$ = 1kg\n$$ = 2kg\n$$$ = 4kg\nX = não tem tesouro')
print('')
print('---------------------------------------------------------------------')
#Aqui seria apenas as regras do jogo em um  print simples

# configuração do jogo
quantidade, metros, tanques = dados() #essa função recolhe os dados que o jogador quer como numero de jogadores profundidade e tal

# Inicializa jogadores & inventario dos jogadores e o return de algumas funçoes que utilizaremos 
jogadores, movimentos = map_list(quantidade)  #essa função retorna algumas coisas importantes pro jogo como a lista de jogadores, a lista onde vai fica armazenado a onde eles estão 
tesouros = bau(metros) 
inventario_geral = mochila(quantidade) # essa função vai cria o iventario que vai ser utilizado pelos jogadores no mapa
inventario_submarino = submarino(quantidade) # essa função vai criar o inventario dos jogadores so que no submarino 


# Jogo principal onde acorre a maioria das operações em um while para se repetir ate que os tanques chegem a zero
while tanques > 0:
    for i in range(quantidade): #um for para medir os turnos dos jogadores (i = 0 jogador 1 e assim por diante...)
        print()
        print("="*100)
        print()
        printmap(jogadores, movimentos, metros, tesouros)# mostrar o mapa para os jogadores e suas informações
        print(inventario_geral)
        print(inventario_submarino)
        print(f"Tanques restantes: {tanques}")
        chave_invent = f"mochila_do_jogador_{i+1}" #define qual espaço do dicionario(inventario do jogadores) vamos utilizar de acordo com i do turno
        chave_sub = f"submarino_do_jogador{i+1}"  #define em qual espaço do dicionario(inventario do jogadores so que no submarino) vamos utilizar caso um jogador queira guardar
        decisao = decisão(tesouros,movimentos,i,jogadores,inventario_geral,chave_invent) # decidir oq vai fazer no seu turno 
        if decisao == 1:
            movimento, nova_posicao = gerar_novaposicao(decisao,movimentos,i)# ir para a proxima casa 
            movimentos[i] = verifica_posição(movimentos, nova_posicao, metros, i) #verificar se casa que ele vai pode ser ocupada ou não
            tanques  = gasto(movimento, tanques,inventario_geral,chave_invent,movimentos,nova_posicao,i)
            if tanques <= 0: # para finalizar assim que os tanques cheguem a zero e n continuar rodando o resto dos turnos
                break
            print(f"Jogador {jogadores[i]} avançou {movimento} casas")
        elif decisao == 2:
            movimento, nova_posicao = gerar_novaposicao(decisao,movimentos,i) 
            movimentos[i] = verifica_posição(movimentos, nova_posicao, metros, i) 
            tanques  = gasto(movimento, tanques,inventario_geral,chave_invent,movimentos,nova_posicao,i)
            if tanques <= 0: 
                break
            print(f"Jogador {jogadores[i]} recuou {movimento} casas")
        elif decisao == 3:
            pegar(tesouros,movimentos,i,inventario_geral,chave_invent)
            # função para pega os tesouros no mapa e amarzena eles no sugmarino
        elif decisao == 4:
            pass #caso ele queira passar a vez
        elif decisao == 5:
            guarda(inventario_submarino,chave_sub,inventario_geral,chave_invent)
            # uma função para guarda os tesouros no submarino 

ganhador , maior_tesouros = vencedor(inventario_submarino) # função para definir qual jogador ganhou ou vai ganhar o jogo

print(f"Jogo terminado! ")
print(f"O iventario com maior valor foi o {ganhador} com {maior_tesouros} kg de tesouros no submarino 🏅🏅")
