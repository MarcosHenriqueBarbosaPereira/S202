from database import Database

class SchoolDAO:
    def __init__(self, db: Database):
        self.database = db

    # CREATE -------------------------------------------------------------------------------------------------------
    # Simple Creates
    def create_teacher(self, cpf:str, nome:str):
        query = "CREATE (p:Professor {cpf: $cpf, nome: $nome})"
        parameters = {"cpf": cpf, "nome": nome}
        self.database.execute_query(query, parameters)
        print("Professor criado com sucesso!")
    
    def create_student(self, matricula:str, nome:str):
        query = "CREATE (a:Aluno {matricula: $matricula, nome: $nome})"
        parameters = {"matricula": matricula, "nome": nome}
        self.database.execute_query(query, parameters)
        print("Aluno criado com sucesso!")
    
    def create_class(self, nome:str):
        query = "CREATE (t:Turma {nome: $nome})"
        parameters = {"nome": nome}
        self.database.execute_query(query, parameters)
        print("Turma criada com sucesso!")
    
    def create_subject(self, nome:str):
        query = "CREATE (d:Disciplina {nome: $nome})"
        parameters = {"nome": nome}
        self.database.execute_query(query, parameters)
        print("Disciplina criada com sucesso!")
    
    # Teacher Creates
    def create_teacher_subject(self, cpf:str, nome:str):
        query = "MATCH (p:Professor {cpf: $cpf}), (d:Disciplina {nome: $nome}) CREATE (p)-[:LECIONA]->(d)"
        parameters = {"cpf": cpf, "nome": nome}
        self.database.execute_query(query, parameters)
        print("Relacionamento Professor e Disciplina criado com sucesso!")
    
    def create_teacher_class(self, cpf:str, nome:str):
        query = "MATCH (p:Professor {cpf: $cpf}), (t:Turma {nome: $nome}) CREATE (p)-[:POSSUI]->(t)"
        parameters = {"cpf": cpf, "nome": nome}
        self.database.execute_query(query, parameters)
        print("Relacionamento Professor e Turma criado com sucesso!")
    
    # Student Creates
    def create_student_class(self, matricula:str, nome:str):
        query = "MATCH (a:Aluno {matricula: $matricula}), (t:Turma {nome: $nome}) CREATE (a)-[:FREQUENTA]->(t)"
        parameters = {"matricula": matricula, "nome": nome}
        self.database.execute_query(query, parameters)
        print("Relacionamento Aluno e Turma criado com sucesso!")
    
    def create_student_subject(self, matricula:str, nome:str):
        query = "MATCH (a:Aluno {matricula: $matricula}), (d:Disciplina {nome: $nome}) CREATE (a)-[:MATRICULADO]->(d)"
        parameters = {"matricula": matricula, "nome": nome}
        self.database.execute_query(query, parameters)
        print("Relacionamento Aluno e Disciplina criado com sucesso!")

    # READ ---------------------------------------------------------------------------------------------------------
    # Simple Gets
    def get_teacher(self, cpf:str):
        query = "MATCH (p:Professor {cpf: $cpf}) RETURN p"
        parameters = {"cpf": cpf}
        return self.database.execute_query(query, parameters)

    def get_student(self, matricula:str):
        query = "MATCH (a:Aluno {matricula: $matricula}) RETURN a"
        parameters = {"matricula": matricula}
        return self.database.execute_query(query, parameters)
    
    def get_class(self, turma:str):
        query = "MATCH (t:Turma {nome: $nome}) RETURN t"
        parameters = {"nome": turma}
        return self.database.execute_query(query, parameters)
    
    def get_subject(self, nome:str):
        query = "MATCH (d:Disciplina {nome: $nome}) RETURN d"
        parameters = {"nome": nome}
        return self.database.execute_query(query, parameters)
    
    # Teacher Gets
    def get_teacher_subjects(self, cpf:str):
        query = "MATCH (p:Professor {cpf: $cpf})-[:LECIONA]->(d:Disciplina) RETURN d"
        parameters = {"cpf": cpf}
        return self.database.execute_query(query, parameters)
    
    def get_teacher_classes(self, cpf:str):
        query = "MATCH (p:Professor {cpf: $cpf})-[:POSSUI]->(t:Turma) RETURN t"
        parameters = {"cpf": cpf}
        return self.database.execute_query(query, parameters)
    
    # Student Gets
    def get_student_classes(self, matricula:str):
        query = "MATCH (a:Aluno {matricula: $matricula})-[:FREQUENTA]->(t:Turma) RETURN t"
        parameters = {"matricula": matricula}
        return self.database.execute_query(query, parameters)
    
    def get_student_subjects(self, matricula:str):
        query = "MATCH (a:Aluno {matricula: $matricula})-[:MATRICULADO]->(d:Disciplina) RETURN d"
        parameters = {"matricula": matricula}
        return self.database.execute_query(query, parameters)
    
    # Class Gets
    def get_class_students(self, turma:str):
        query = "MATCH (t:Turma {nome: $nome})<-[:FREQUENTA]-(a:Aluno) RETURN a"
        parameters = {"nome": turma}
        return self.database.execute_query(query, parameters)
    
    def get_number_of_students_in_class(self, turma:str):
        query = "MATCH (t:Turma {nome: $nome})<-[:FREQUENTA]-(a:Aluno) RETURN count(a)"
        parameters = {"nome": turma}
        return self.database.execute_query(query, parameters)
    
    # Subject Gets
    def get_subject_teacher(self, nome:str):
        query = "MATCH (d:Disciplina {nome: $nome})<-[:LECIONA]-(p:Professor) RETURN p"
        parameters = {"nome": nome}
        return self.database.execute_query(query, parameters)
    
    def get_subject_students(self, nome:str):
        query = "MATCH (d:Disciplina {nome: $nome})<-[:MATRICULADO]-(a:Aluno) RETURN a"
        parameters = {"nome": nome}
        return self.database.execute_query(query, parameters)
    
    def get_number_of_students_in_subject(self, nome:str):
        query = "MATCH (d:Disciplina {nome: $nome})<-[:MATRICULADO]-(a:Aluno) RETURN count(a)"
        parameters = {"nome": nome}
        return self.database.execute_query(query, parameters)
    
    # UPDATE -------------------------------------------------------------------------------------------------------
    def update_teacher(self, cpf:str, nome:str):
        query = "MATCH (p:Professor {cpf: $cpf}) SET p.nome = {nome: $nome}"
        parameters = {"cpf": cpf, "nome": nome}
        self.database.execute_query(query, parameters)
        print("Professor atualizado com sucesso!")

    def update_student(self, matricula:str, nome:str):
        query = "MATCH (a:Aluno {matricula: $matricula}) SET a.nome = {nome: $nome}"
        parameters = {"matricula": matricula, "nome": nome}
        self.database.execute_query(query, parameters)
        print("Aluno atualizado com sucesso!")

    # DELETE -------------------------------------------------------------------------------------------------------
    def delete_teacher(self, cpf:str):
        query = "MATCH (p:Professor {cpf: $cpf}) DETACH DELETE p"
        parameters = {"cpf": cpf}
        self.database.execute_query(query, parameters)
        print("Professor deletado com sucesso!")

    def delete_student(self, matricula:str):
        query = "MATCH (a:Aluno {matricula: $matricula}) DETACH DELETE a"
        parameters = {"matricula": matricula}
        self.database.execute_query(query, parameters)
        print("Aluno deletado com sucesso!")
