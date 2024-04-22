from database import Database
from livrosCLI import LivrosCLI
from livrosDAO import LivrosDAO

db = Database(database="Relatorio_5", collection="livros")
livrosDAO = LivrosDAO(db)
livrosCLI = LivrosCLI(livrosDAO)

livrosCLI.run()