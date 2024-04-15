from motoristaDAO import MotoristaDAO
from passageiro import Passageiro
from motorista import Motorista
from corrida import Corrida

class MotoristaCLI:
    def __init__(self, motoristaDAO: MotoristaDAO):
        self.motoristaDAO = motoristaDAO
        self.commands = {
            "inserir": self.insert_motorista,
            "adicionar_corrida": self.add_corrida,
            "remover_corrida": self.delete_corrida,
            "listar": self.list_motoristas
        }

    def insert_motorista(self):
        nota = int(input("Digite a nota do motorista: "))
        corridas = []
        motorista = Motorista(corridas, nota)
        self.motoristaDAO.insert_motorista(motorista)

    def add_corrida(self):
        motorista_id = str(input("Digite o id do motorista: "))
        nota_corrida = int(input("Digite a nota da corrida: "))
        distancia = float(input("Digite a distancia da corrida: "))
        valor = float(input("Digite o valor da corrida: "))
        nome_passageiro = str(input("Digite o nome do passageiro: "))
        documento_passageiro = str(input("Digite o documento do passageiro: "))

        passageiro = Passageiro(nome_passageiro, documento_passageiro)
        corrida = Corrida(nota_corrida, distancia, valor, passageiro)

        self.motoristaDAO.add_corrida(motorista_id, corrida)

    def delete_corrida(self):
        motorista_id = str(input("Digite o id do motorista: "))
        corrida_id = str(input("Digite o id da corrida: "))

        self.motoristaDAO.delete_corrida(motorista_id, corrida_id)

    def list_motoristas(self):
        motoristas = self.motoristaDAO.get_motoristas_ids()
        for motorista in motoristas:
            print("ID do Motorista:", motorista["_id"], "Nota:", motorista["nota"])

    def run(self):
        print("Bem-vindo ao sistema de motoristas!")
        print("Comandos disponíveis: inserir, adicionar_corrida, remover_corrida, listar, sair:\n")
        while True:
            command = input("Digite o comando: ")
            if command == "sair":
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido!")