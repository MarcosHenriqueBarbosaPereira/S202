from database import Database

class ProductAnalyzer:
    def __init__(self, database: Database):
        self.database = database

    def getTotalSellsPerDay(self):
        return self.database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"data": "$data_compra"}, "quantidade_total": {"$sum": "$produtos.quantidade"}}}
        ])
    
    def getMostSoldProductPerClient(self):
        return self.database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"cliente": "$cliente_id", "produto": "$produtos.descricao"}, "quantidade_total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"quantidade_total": -1}},
            {"$group": {"_id": "$_id.cliente", "produto": {"$first": "$_id.produto"}, "quantidade_total": {"$first": "$quantidade_total"}}}
        ])
    
    def getMostExpensiveBuyer(self):
        return self.database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])
    
    def getProductsSoldMoreThanOne(self):
        return self.database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "quantidade_total": {"$sum": "$produtos.quantidade"}}},
            {"$match": {"quantidade_total": {"$gt": 1}}}
        ])