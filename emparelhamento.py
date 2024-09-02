import networkx as nx

def gerar_chaves(jogadores):
    # Ordenar jogadores pelo nível ITN (do mais forte para o mais fraco)
    jogadores_ordenados = sorted(jogadores, key=lambda x: x.nivel_itn)

    # Criar um grafo bipartido onde jogadores mais fortes ficam em grupos opostos
    grafo = nx.Graph()

    # Adicionar nós ao grafo com base na ordem
    num_jogadores = len(jogadores_ordenados)
    for i in range(num_jogadores // 2):
        jogador_forte = jogadores_ordenados[i]
        jogador_fraco = jogadores_ordenados[num_jogadores - 1 - i]
        # Adicionar arestas entre jogadores fortes e fracos diretamente
        grafo.add_edge(jogador_forte.nome, jogador_fraco.nome, weight=10)

    # Encontrar o emparelhamento máximo considerando o peso
    matching = nx.max_weight_matching(grafo, maxcardinality=True)
    return matching

