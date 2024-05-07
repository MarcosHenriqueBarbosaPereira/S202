from database import Database
from jogo import Jogo

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.204.86.97:7687", "neo4j", "ejection-precision-fort")
db.drop_all()

# cria uma instância da classe Jogo, passando a instância da classe Database
jogo = Jogo(db)

# cria 10 jogadores
for i in range(10):
    jogo.create_jogador(f"Jogador {i}", i)

# cria 5 partidas
for i in range(5):
    jogo.create_partida(i)

# cria relacionamentos entre jogadores e partidas (cada partida com 2 jogadores)

# jogadores 0, 1, 2, 3 e 4 venceram as partidas 0, 1, 2, 3 e 4, respectivamente
for i in range(5):
    jogo.create_relacionamento_jogador_partida(i, i, True)

# jogadores 5, 6, 7, 8 e 9 perderam as partidas 0, 1, 2, 3 e 4, respectivamente
for i in range(5, 10):
    jogo.create_relacionamento_jogador_partida(i, i - 5, False)

# recupera o jogadore que venceu cada partida
for i in range(5):
    print(f"Jogador que venceu a partida: {i}")
    resultado = jogo.get_partida_winner(i)
    if resultado:
        print(resultado[0]["jogador"]["nome"])
    else:
        print("Partida não finalizada")

# recupera as partidas de cada jogador
for i in range(10):
    print(f"Partidas do jogador: {i}")
    resultado = jogo.get_jogador_matches(i)
    for record in resultado:
        print(record["partida"]["id"])






