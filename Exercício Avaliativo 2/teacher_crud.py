from database import Database

class TeacherCrud:

    def __init__(self, database: Database):
        self.database = database

    def create(self, name, ano_nasc, cpf):
        query = "CREATE (teacher:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.database.execute_query(query, parameters)

    def read(self, name):
        query = "MATCH (teacher:Teacher {name: $name}) RETURN teacher"
        parameters = {"name": name}
        return self.database.execute_query(query, parameters)
        
    def delete(self, name):
        query = "MATCH (teacher:Teacher {name: $name}) DETACH DELETE teacher"
        parameters = {"name": name}
        self.database.execute_query(query, parameters)

    def update(self, name, newCpf):
        query = "MATCH (teacher:Teacher {name: $name}) SET teacher.cpf = $newCpf"
        parameters = {"name": name, "newCpf": newCpf}
        self.database.execute_query(query, parameters)