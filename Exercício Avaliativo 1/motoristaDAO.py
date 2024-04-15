from bson.objectid import ObjectId
from database import Database


class MotoristaDAO:
    def __init__ (self, database: Database):
        self.database = database

    def insert_motorista(self, motorista):                  #CREATE ----------------------------------------
        self.database.collection.insert_one({
            "nota": int(motorista.nota),
            "corridas": motorista.corridas
            }
        )
        print("Motorista inserido com sucesso!")

    def add_corrida(self, motorista_id, corrida):           #UPDATE ----------------------------------------
        self.database.collection.update_one(
            {"_id": ObjectId(motorista_id)},
            {"$push": {"corridas": {
                "nota": int(corrida.nota_corrida),
                "distancia": float(corrida.distancia),
                "valor": float(corrida.valor),
                "passageiro": {
                    "nome": str(corrida.passageiro.nome),
                    "documento": str(corrida.passageiro.documento)
                }
            }}}
        )
        print("Corrida adicionada com sucesso!")

    def delete_corrida(self, motorista_id):     #DELETE ----------------------------------------
        self.database.collection.delete_one(
            {"_id": ObjectId(motorista_id)}
        )

        print("Motorista removid0 com sucesso!")

    def get_motoristas_ids(self):                           #READ ------------------------------------------
        return self.database.collection.find({}, {'nota': 1, '_id': 1})
        