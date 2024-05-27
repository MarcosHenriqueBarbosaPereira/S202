from database import Database
from query import Query
from teacher_crud import TeacherCrud

db = Database("bolt://44.204.86.97:7687", "neo4j", "ejection-precision-fort")

querys = Query(db)
teacherCrud = TeacherCrud(db)

# questão 1 --------------------------------------------------------------------------------------------------------------------
print(querys.get_teacher("Renzo"))
print(querys.get_teacher_starts_M())
print(querys.get_cities())
print(querys.get_schools_between_150_and_550())

# questão 2 --------------------------------------------------------------------------------------------------------------------
print(querys.get_oldest_and_youngest_teachers_years())
print(querys.get_cities_avg_population())
print(querys.get_city_CEP_37540000())
print(querys.get_teacher_third_character())

# questão 3 --------------------------------------------------------------------------------------------------------------------
teacherCrud.create("Chris Lima", 1956, '189.052.396-66')
teacherCrud.read("Chris Lima")
teacherCrud.update("Chris Lima", '162.052.777-77')

# CLI --------------------------------------------------------------------------------------------------------------------------
print("Bem-vindo ao sistema de professores!")
print("Comandos disponíveis: inserir, buscar, atualizar, remover, sair:\n")
while True:
    command = input("Digite o comando: ")
    if command == "sair":
        break
    elif command == "inserir":
        name = str(input("Digite o nome do professor: "))
        ano_nasc = int(input("Digite o ano de nascimento do professor: "))
        cpf = str(input("Digite o CPF do professor: "))
        teacherCrud.create(name, ano_nasc, cpf)
    elif command == "buscar":
        name = str(input("Digite o nome do professor: "))
        teacherCrud.read(name)
    elif command == "atualizar":
        name = str(input("Digite o nome do professor: "))
        newCpf = str(input("Digite o novo CPF do professor: "))
        teacherCrud.update(name, newCpf)
    elif command == "remover":
        name = str(input("Digite o nome do professor: "))
        teacherCrud.delete(name)
    else:
        print("Comando inválido!")