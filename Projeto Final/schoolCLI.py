from schoolDAO import SchoolDAO

class SchoolCLI:
    def __init__(self, schoolDAO: SchoolDAO):
        self.schoolDAO = schoolDAO
        self.commands = {
            # CREATE -------------------------------------------------------------------------------------------------------
            "c_prof": self.create_teacher,
            "c_aluno": self.create_student,
            "c_turma": self.create_class,
            "c_disc": self.create_subject,
            "c_prof_disc": self.create_teacher_subject,
            "c_prof_turma": self.create_teacher_class,
            "c_aluno_turma": self.create_student_class,
            "c_aluno_disc": self.create_student_subject,

            # READ ---------------------------------------------------------------------------------------------------------
            # Simple Gets
            "g_prof": self.get_teacher,
            "g_aluno": self.get_student,
            "g_turma": self.get_class,
            "g_disc": self.get_subject,

            # Teacher Gets
            "g_prof_disc": self.get_teacher_subjects,
            "g_prof_turma": self.get_teacher_classes,

            # Student Gets
            "g_aluno_turma": self.get_student_classes,
            "g_aluno_disc": self.get_student_subjects,

            # Class Gets
            "g_turma_aluno": self.get_class_students,
            "g_turma_n_aluno": self.get_number_of_students_in_class,

            # Subjects Gets
            "g_disc_aluno": self.get_subject_students,
            "g_disc_prof": self.get_subject_teacher,
            "g_disc_n_aluno": self.get_number_of_students_in_subject,

            # UPDATE -------------------------------------------------------------------------------------------------------
            "u_prof": self.update_teacher,
            "u_aluno": self.update_student,

            # DELETE -------------------------------------------------------------------------------------------------------
            "d_prof": self.delete_teacher,
            "d_aluno": self.delete_student
        }

    def create_teacher(self):
        cpf = input("Digite o CPF do professor: ")
        nome = input("Digite o Nome do professor: ")
        self.schoolDAO.create_teacher(cpf, nome)
    
    def create_student(self):
        matricula = input("Digite a Matricula do aluno: ")
        nome = input("Digite o Nome do aluno: ")
        self.schoolDAO.create_student(matricula, nome)

    def create_class(self):
        turma = input("Digite o Nome da Turma: ")
        self.schoolDAO.create_class(turma)

    def create_subject(self):
        nome = input("Digite o Nome da Disciplina: ")
        self.schoolDAO.create_subject(nome)

    def create_teacher_subject(self):
        cpf = input("Digite o CPF do professor: ")
        nome = input("Digite o Nome da Disciplina: ")
        self.schoolDAO.create_teacher_subject(cpf, nome)

    def create_teacher_class(self):
        cpf = input("Digite o CPF do professor: ")
        turma = input("Digite o Nome da Turma: ")
        self.schoolDAO.create_teacher_class(cpf, turma)

    def create_student_class(self):
        matricula = input("Digite a Matricula do aluno: ")
        turma = input("Digite o Nome da Turma: ")
        self.schoolDAO.create_student_class(matricula, turma)

    def create_student_subject(self):
        matricula = input("Digite a Matricula do aluno: ")
        nome = input("Digite o Nome da Disciplina: ")
        self.schoolDAO.create_student_subject(matricula, nome)

    def get_teacher(self):
        cpf = input("Digite o CPF do professor: ")
        result = (self.schoolDAO.get_teacher(cpf))
        for record in result:
            print("Nome: " + record["p"]["nome"] + " CPF: " + record["p"]["cpf"])

    def get_student(self):
        matricula = input("Digite a Matricula do aluno: ")
        result = (self.schoolDAO.get_student(matricula))
        for record in result:
            print("Nome: " + record["a"]["nome"] + " Matricula: " + record["a"]["matricula"])

    def get_class(self):
        turma = input("Digite o Nome da Turma: ")
        result = (self.schoolDAO.get_class(turma))
        for record in result:
            print("Nome: " + record["t"]["nome"])

    def get_subject(self):
        nome = input("Digite o Nome da Disciplina: ")
        result = (self.schoolDAO.get_subject(nome))
        for record in result:
            print("Nome: " + record["d"]["nome"])

    def get_teacher_subjects(self):
        cpf = input("Digite o CPF do professor: ")
        result = (self.schoolDAO.get_teacher_subjects(cpf))
        for record in result:
            print("Nome: " + record["d"]["nome"])

    def get_teacher_classes(self):
        cpf = input("Digite o CPF do professor: ")
        result = (self.schoolDAO.get_teacher_classes(cpf))
        for record in result:
            print("Nome: " + record["t"]["nome"])

    def get_student_classes(self):
        matricula = input("Digite a Matricula do aluno: ")
        result = (self.schoolDAO.get_student_classes(matricula))
        for record in result:
            print("Nome: " + record["t"]["nome"])

    def get_student_subjects(self):
        matricula = input("Digite a Matricula do aluno: ")
        result = (self.schoolDAO.get_student_subjects(matricula))
        for record in result:
            print("Nome: " + record["d"]["nome"])

    def get_class_students(self):
        turma = input("Digite o Nome da Turma: ")
        result = (self.schoolDAO.get_class_students(turma))
        for record in result:
            print("Nome: " + record["a"]["nome"] + " Matricula: " + record["a"]["matricula"])

    def get_number_of_students_in_class(self):
        turma = input("Digite o Nome da Turma: ")
        result = (self.schoolDAO.get_number_of_students_in_class(turma))
        print(result[0]["count(a)"])

    def get_subject_students(self):
        nome = input("Digite o Nome da Disciplina: ")
        result = (self.schoolDAO.get_subject_students(nome))
        for record in result:
            print("Nome: " + record["a"]["nome"] + " Matricula: " + record["a"]["matricula"])

    def get_subject_teacher(self):
        nome = input("Digite o Nome da Disciplina: ")
        result = (self.schoolDAO.get_subject_teacher(nome))
        for record in result:
            print("Nome: " + record["p"]["nome"] + " CPF: " + record["p"]["cpf"])

    def get_number_of_students_in_subject(self):
        nome = input("Digite o Nome da Disciplina: ")
        result = (self.schoolDAO.get_number_of_students_in_subject(nome))
        print(result[0]["count(a)"])

    def update_teacher(self):
        cpf = input("Digite o CPF do professor: ")
        novoNome = str(input("Digite o novo Nome do professor: "))
        self.schoolDAO.update_teacher(cpf, novoNome)

    def update_student(self):
        matricula = input("Digite a Matricula do aluno: ")
        novoNome = input("Digite o novo Nome do aluno: ")
        self.schoolDAO.update_student(matricula, novoNome)

    def delete_teacher(self):
        cpf = input("Digite o CPF do professor: ")
        self.schoolDAO.delete_teacher(cpf)

    def delete_student(self):
        matricula = input("Digite a Matricula do aluno: ")
        self.schoolDAO.delete_student(matricula)

    def run(self):
        print("Bem-vindo ao sistema escolar!")
        print("Digite 'exit' para sair ou os seguinte comandos:\n")
        print("CREATE:\n c_prof: Criar Professor\n c_aluno: Criar Aluno\n c_turma: Criar Turma\n c_disc: Criar Disciplina\n c_prof_disc: Criar relacionamento entre Professor e Disciplina\n c_prof_turma: Criar relacionamento entre Professor e Turma\n c_aluno_turma: Criar relacionamento entre Aluno e Turma\n c_aluno_disc: Criar relacionamento entre Aluno e Disciplina\n")
        print("READ:\n g_prof: Buscar Professor\n g_aluno: Buscar Aluno\n g_turma: Buscar Turma\n g_disc: Buscar Disciplina\n g_prof_disc: Buscar Disciplinas de um Professor\n g_prof_turma: Buscar Turmas de um Professor\n g_aluno_turma: Buscar Turmas de um Aluno\n g_aluno_disc: Buscar Disciplinas de um Aluno\n g_turma_aluno: Buscar Alunos de uma Turma\n g_turma_n_aluno: Buscar número de Alunos de uma Turma\n g_disc_aluno: Buscar Alunos de uma Disciplina\n g_disc_prof: Buscar Professor de uma Disciplina\n g_disc_n_aluno: Buscar número de Alunos de uma Disciplina\n")
        print("UPDATE:\n u_prof: Atualizar Professor\n u_aluno: Atualizar Aluno\n")
        print("DELETE:\n d_prof: Deletar Professor\n d_aluno: Deletar Aluno\n")
        while True:
            command = input("Digite o comando: ")
            if command == "exit":
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido!")