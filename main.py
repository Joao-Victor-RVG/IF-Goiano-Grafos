from jogador import Jogador
from torneio import Torneio

# Criando um torneio
torneio = Torneio()

# Inscrevendo jogadores dinamicamente
torneio.inscrever_jogadores()

# Exibindo jogadores
torneio.exibir_jogadores()

# Gerando e exibindo chaves de emparelhamento
emparelhamentos = torneio.gerar_chaves()
print("\n======== Chaveamento ========\n")
for i, (jogador1, jogador2) in enumerate(emparelhamentos, start=1):
    print(f"Partida {i}: {jogador1} vs {jogador2}")
    print("\n=============================")

# Visualizar o grafo de partidas
torneio.visualizar_grafo()


