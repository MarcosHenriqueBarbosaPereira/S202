from bson.objectid import ObjectId
from database import Database

class LivrosDAO:
    def __init__ (self, database: Database):
        self.database = database

    def create_livro(self, titulo:str, autor:str, ano:int, preco:float):                  #CREATE ----------------------------------------
        try:
            res = self.database.collection.insert_one({
                "titulo": titulo,
                "autor": autor,
                "ano": ano,
                "preco": preco
                }
            )
            print(f"Livro inserido com sucesso! ID: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(e)
            return None
        
    def read_livro_by_id(self, livro_id):                           #READ ------------------------------------------
        try:
            res = self.database.collection.find_one({"_id": ObjectId(livro_id)})
            print(f"Livro encontrado: Título: {res['titulo']}, Autor(a): {res['autor']}, Ano de Lançamento: {res['ano']}, Preço: R${res['preco']:0.2f}")
            return res
        except Exception as e:
            print(e)
            return None
        
    def update_livro(self, livro_id, titulo:str, autor:str, ano:int, preco:float):              #UPDATE ------------------------------------------
        try:
            res = self.database.collection.update_one(
                {"_id": ObjectId(livro_id)},
                {"$set": {
                    "titulo": titulo,
                    "autor": autor,
                    "ano": ano,
                    "preco": preco
                }}
            )
            print(f"Livro atualizado com sucesso! {res.modified_count} registros alterados.")
            return res.modified_count
        except Exception as e:
            print(e)
            return None
        
    def delete_livro(self, livro_id):     #DELETE ----------------------------------------
        try:
            res = self.database.collection.delete_one(
                {"_id": ObjectId(livro_id)}
            )
            print(f"Livro removido com sucesso! {res.deleted_count} registros deletados.")
            return res
        except Exception as e:
            print(e)
            return None
