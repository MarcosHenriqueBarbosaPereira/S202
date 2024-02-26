class Professor:
    
    def __init__(self, nome):
        self.nome = nome

    def ministrar_aula(self, assunto):
        print(f'O professor {self.nome} está ministrando uma aula sobre {assunto}')


class Aluno:
    
    def __init__(self, nome):
        self.nome = nome

    def presença(self):
        print(f'O(A) aluno(a) {self.nome} está presente')


class Aula:

    def __init__(self, professor, assunto, alunos = []):
        self.professor = professor
        self.assunto = assunto
        self.alunos = alunos

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_presenca(self):
        print(f'Presença na aula de {self.assunto}, ministrada pelo professor {self.professor.nome}:\n')
        print('Alunos presentes:\n')
        for aluno in self.alunos:
            if aluno != None:
                aluno.presença()


professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
aula = Aula(professor, "Programação Orientada a Objetos")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
aula.listar_presenca()
