from database import Database
from schoolCLI import SchoolCLI
from schoolDAO import SchoolDAO

db = Database('bolt://3.235.137.136:7687', 'neo4j', 'expansion-worlds-elapses')
schoolDAO = SchoolDAO(db)
schoolCLI = SchoolCLI(schoolDAO)

db.drop_all()
schoolCLI.run()
