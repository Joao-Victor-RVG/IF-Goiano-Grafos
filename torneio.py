import sys
import networkx as nx
from jogador import Jogador
import emparelhamento

class Torneio:
    def __init__(self):
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)


    def gerar_chaves(self):
        if len(self.jogadores) % 2 != 0:
            print("Número ímpar de jogadores. O torneio deve ter um número par de jogadores.")
            sys.exit()
        chaves = emparelhamento.gerar_chaves(self.jogadores)
        return chaves

    def exibir_jogadores(self):
        print("Joadores inscritos:")
        for jogador in self.jogadores:
            print(jogador)
        
    def visualizar_grafo(self):
            # Cria um grafo para visualização das partidas
            grafo = nx.Graph()

            # Adiciona nós e arestas baseados nas chaves geradas
            chaves = self.gerar_chaves()
            for jogador1, jogador2 in chaves:
                grafo.add_edge(jogador1, jogador2)

            # Desenhar o grafo com visualização simples
            import matplotlib.pyplot as plt
            pos = nx.spring_layout(grafo)  # Posicionamento dos nós
            nx.draw(
                grafo, pos,
                with_labels=True,
                node_size=1000,
                node_color="skyblue",
                font_size=10,
                font_weight="bold"
            )
            plt.show()

    def inscrever_jogadores(self):
        while True:
            nome = input("Digite o nome do jogador ('ok' para finalizar): ")
            if nome.lower() == 'ok':
                break
            while True:
                try:
                    nivel_itn = float(input(f"Nível ITN de {nome}: "))
                    if 1.0 <= nivel_itn <= 10.0:
                        break
                    else:
                        print("Por favor, insira um valor ITN entre 1.0 e 10.0.")
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número.")
            jogador = Jogador(nome, nivel_itn)
            self.adicionar_jogador(jogador)
            print(f"Jogador {nome} adicionado com nível ITN {nivel_itn}.\n")
