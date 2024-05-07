from database import Database

class Jogo:
    def __init__(self, database: Database):
        self.database = database

    def create_jogador(self, nome: str, id: int):
        query = "CREATE (jogador:Jogador {nome: $nome, id: $id})"
        self.database.execute_query(query, {"nome": nome}, {"id": id})

    def delete_jogador(self, id: int):
        query = "MATCH (jogador:Jogador {id: $id}) DETACH DELETE jogador"
        self.database.execute_query(query, {"id": id})

    def update_jogador(self, nome: str, id: int):
        query = "MATCH (jogador:Jogador {id: $id}) SET jogador.nome = $nome"
        self.database.execute_query(query, {"nome": nome}, {"id": id})

    def get_jogador(self, id: int):
        query = "MATCH (jogador:Jogador {id: $id}) RETURN jogador"
        return self.database.execute_query(query, {"id": id})
    
    def create_partida(self, id: int):
        query = "CREATE (partida:Partida {id: $id})"
        self.database.execute_query(query, {"id": id})

    def delete_partida(self, id: int):
        query = "MATCH (partida:Partida {id: $id}) DETACH DELETE partida"
        self.database.execute_query(query, {"id": id})

    def update_partida(self, id: int):
        query = "MATCH (partida:Partida {id: $id}) SET partida.id = $id"
        self.database.execute_query(query, {"id": id})