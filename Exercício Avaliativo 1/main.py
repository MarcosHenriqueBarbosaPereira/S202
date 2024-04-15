from database import Database
from motoristaDAO import MotoristaDAO
from motoristaCLI import MotoristaCLI

db = Database(database="atlas-cluster", collection="Motoristas")
motoristaDAO = MotoristaDAO(db)
motoristaCLI = MotoristaCLI(motoristaDAO)

motoristaCLI.run()