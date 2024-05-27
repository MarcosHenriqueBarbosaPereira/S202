from database import Database

class Query:

    def __init__(self, database: Database):
        self.database = database

    def get_teacher(self, nome: str):
        query = "MATCH (teacher:Teacher {nome: $nome}) RETURN teacher.cpf, teacher.ano_nasc"
        parameters = {"nome": nome}
        return self.database.execute_query(query, parameters)
    
    def get_teacher_starts_M(self):
        query = "MATCH (teacher:Teacher) WHERE teacher.name STARTS WITH 'M' RETURN teacher.name"
        return self.database.execute_query(query)
    
    def get_cities(self):
        query = "MATCH (city:City) RETURN city.name"
        return self.database.execute_query(query)
    
    def get_schools_between_150_and_550(self):
        query = "MATCH (school:School) WHERE school.number >= 150 and school.number <= 550 RETURN school.name, school.address, school.number"
        return self.database.execute_query(query)
    
    def get_oldest_and_youngest_teachers_years(self):
        query = "MATCH (teacher:Teacher) RETURN max(teacher.ano_nasc), min(teacher.ano_nasc)"
        return self.database.execute_query(query)
    
    def get_cities_avg_population(self):
        query = "MATCH (city:City) avg(city.populacao)"
        return self.database.execute_query(query)
    
    def get_city_CEP_37540000(self):
        query = "MATCH (city:City {cep: 37540000}) RETURN REPLACE(city.name, 'a', 'A')"
        return self.database.execute_query(query)
    
    def get_teacher_third_character(self):
        query = "MATCH (teacher:Teacher) RETURN SUBSTRING(teacher.name, 2, 1)"
        return self.database.execute_query(query)