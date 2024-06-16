from database import Database
from schoolCLI import SchoolCLI
from schoolDAO import SchoolDAO

db = Database('bolt://54.227.85.224:7687', 'neo4j', 'leakages-hardcopies-timers')
schoolDAO = SchoolDAO(db)
schoolCLI = SchoolCLI(schoolDAO)

#db.drop_all()
schoolCLI.run()
