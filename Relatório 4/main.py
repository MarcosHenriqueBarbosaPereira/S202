from database import Database
from helper.writeAJson import writeAJson
from productAnalyzer import ProductAnalyzer

db = Database(database="mercado", collection="compras")
#db.resetDatabase()

analyzer = ProductAnalyzer(db)

writeAJson(analyzer.getTotalSellsPerDay(), "Total de vendas por dia")

writeAJson(analyzer.getMostSoldProductPerClient(), "Produto mais vendido por cliente")

writeAJson(analyzer.getMostExpensiveBuyer(), "Cliente que mais gastou")

writeAJson(analyzer.getProductsSoldMoreThanOne(), "Produtos vendidos mais de uma vez")