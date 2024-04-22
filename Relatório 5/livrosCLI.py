from livrosDAO import LivrosDAO

class LivrosCLI:
    def __init__ (self, livrosDAO: LivrosDAO):
        self.livrosDAO = livrosDAO
        self.commands = {
            "inserir": self.create_livro,
            "buscar": self.read_livro,
            "atualizar": self.update_livro,
            "remover": self.delete_livro
        }

    def create_livro(self):
        titulo = str(input("Digite o título do livro: "))
        autor = str(input("Digite o autor do livro: "))
        ano = int(input("Digite o ano do livro: "))
        preco = float(input("Digite o preço do livro: "))
        self.livrosDAO.create_livro(titulo, autor, ano, preco)

    def read_livro(self):
        livro_id = str(input("Digite o ID do livro: "))
        self.livrosDAO.read_livro_by_id(livro_id)

    def update_livro(self):
        livro_id = str(input("Digite o ID do livro: "))
        titulo = str(input("Digite o novo título do livro: "))
        autor = str(input("Digite o novo autor do livro: "))
        ano = int(input("Digite o novo ano do livro: "))
        preco = float(input("Digite novo o preço do livro: "))
        self.livrosDAO.update_livro(livro_id, titulo, autor, ano, preco)

    def delete_livro(self):
        livro_id = str(input("Digite o ID do livro: "))
        self.livrosDAO.delete_livro(livro_id)

    def run(self):
        print("Bem-vindo ao sistema de livros!")
        print("Comandos disponíveis: inserir, buscar, atualizar, remover, sair:\n")
        while True:
            command = input("Digite o comando: ")
            if command == "sair":
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido!")