from database import Database

class Jogo:
    def __init__(self, database: Database):
        self.database = database

    def create_jogador(self, nome: str, id: int):
        query = "CREATE (jogador:Jogador {nome: $nome, id: $id})"
        parameters = {"nome": nome, "id": id}
        self.database.execute_query(query, parameters)

    def delete_jogador(self, id: int):
        query = "MATCH (jogador:Jogador {id: $id}) DETACH DELETE jogador"
        parameters = {"id": id}
        self.database.execute_query(query, parameters)

    def update_jogador(self, nome: str, id: int):
        query = "MATCH (jogador:Jogador {id: $id}) SET jogador.nome = $nome"
        parameters = {"nome": nome, "id": id}
        self.database.execute_query(query, parameters)

    def get_jogador(self, id: int):
        query = "MATCH (jogador:Jogador {id: $id}) RETURN jogador"
        parameters = {"id": id}
        return self.database.execute_query(query, parameters)
    
    def create_partida(self, id: int):
        query = "CREATE (partida:Partida {id: $id})"
        parameters = {"id": id}
        self.database.execute_query(query, parameters)

    def delete_partida(self, id: int):
        query = "MATCH (partida:Partida {id: $id}) DETACH DELETE partida"
        parameters = {"id": id}
        self.database.execute_query(query, parameters)

    def update_partida(self, id: int):
        query = "MATCH (partida:Partida {id: $id}) SET partida.id = $id"
        parameters = {"id": id}
        self.database.execute_query(query, parameters)

    def get_partida_winner(self, id: int):
        query = "MATCH (jogador:Jogador)-[r:JOGOU_EM {vitória: true}]->(partida:Partida {id: $id}) RETURN jogador"
        parameters = {"id": id}
        return self.database.execute_query(query, parameters)
    
    def get_jogador_matches(self, id: int):
        query = "MATCH (jogador:Jogador {id: $id})-[r:JOGOU_EM]->(partida:Partida) RETURN partida"
        parameters = {"id": id}
        return self.database.execute_query(query, parameters)
    
    def create_relacionamento_jogador_partida(self, id_jogador: int, id_partida: int, vitória: bool):
        query = "MATCH (jogador:Jogador {id: $id_jogador}), (partida:Partida {id: $id_partida}) CREATE (jogador)-[r:JOGOU_EM {vitória: $vitória}]->(partida)"
        parameters = {"id_jogador": id_jogador, "id_partida": id_partida, "vitória": vitória}
        self.database.execute_query(query, parameters)